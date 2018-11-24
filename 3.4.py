num = input("请输入一个5位数字：")
for i in range(1,4):
    flag=True
    if num[i]!=num[-(i+1)]:
        print("不是回文数")
        flag=False
        break
if flag==True:
    print("是回文数")
