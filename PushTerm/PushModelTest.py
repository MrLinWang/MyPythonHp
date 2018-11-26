import pymysql
import jieba
from gensim.models import word2vec
import os

#创建停用词表
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords 

# 对句子进行分词  
def seg_sentence(sentence,separator):  
    sentence_seged = jieba.cut(sentence.strip())  
    #stopwords = stopwordslist('./test/stopwords.txt')  # 这里加载停用词的路径 
    #停用词表
    stopwords = set('的,是,，,、,和,与,对,。,；,并,其,在,等,从,中'.split(','))
    outstr = ''  
    for word in sentence_seged:  
        if word not in stopwords:  
            if word != '\t':  
                outstr += word  
                outstr += separator 
    return outstr

#连接数据库得到数据
def MySQLConnect():
    #建立连接通道，建立连接填入（连接数据库的IP地址，端口号，用户名，密码，要操作的数据库，字符编码）
    conn = pymysql.connect(
        host="172.21.15.167",
        port=3306,
        user='root',
        password='passw0rd',
        database="guide_push_lin"
        ) 

    # 创建游标，操作设置为字典类型，返回结果为字典格式！不写默认是元组格式！
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    #操作数据库的sql语句
    sql="select result_abstract from report_data"

    #向数据库发送操作单条操作指令
    cursor.execute(sql)

    #注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：
    #cursor.scroll(1,mode='relative')  # 相对当前位置移动
    #cursor.scroll(2,mode='absolute') # 相对绝对位置移动
    #接收数据有三种方式：
    #res = cursor.fetchone()  #接收返回的第一行数据 
    #ret = cursor.fetchmany(n) #接收返回的n行数据
    #req = cursor.fetchall() #接收返回的所有数据

    res = cursor.fetchall()

    cursor.close()

    return res


res = MySQLConnect()

#line = res[0]['result_abstract']
lines = []
for i in range(len(res)):
    line = res[i]['result_abstract']
    lines.append(seg_sentence(line,"/").split("/"))


#print(lines)

model = word2vec.Word2Vec(lines, hs=1,min_count=1,window=5,size=100)  
#model.save("word2vec.model")
#model.wv.save_word2vec_format('mymodel.txt',binary = False)

req_count = 5

print(model.wv.similar_by_word(u'信息',topn = 10))