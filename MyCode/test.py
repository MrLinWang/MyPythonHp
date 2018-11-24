
import urllib.request
import jieba

city_info=urllib.request.urlopen( urllib.request.Request('http://pv.sohu.com/cityjson')).read().decode('gb2312')
city_name = city_info.split('=')[1].split(':')[3].split('"')[1]
city_name = jieba.lcut(city_name)[-1]
print (city_info)   #看输出结构  
print (city_name)   #看ip地址