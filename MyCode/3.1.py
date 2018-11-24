#3.1 P93 重量计算
weight =eval(input("输入你的体重(kg)："))
for i in range(1,11):
    print("第{:2}年，地球上体重为：{:5}kg，月球上体重为：{:5.2f}kg".format(i,weight,weight*0.165))
    weight+=0.5
