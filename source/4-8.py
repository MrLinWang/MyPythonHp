try:
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx = eval(input("请输入一个整数: "))
    print(alp[idx])
except NameError:
    print("输入错误，请输入一个整数!")  
except:
    print("其他错误")
