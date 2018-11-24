#p94 3.6 文本进度条
import time
scale = 20
print("Begin")
for i in range(scale+1):
    a,b = '**' * i , '..' * (scale - i)
    c = (i/scale)*100
    print("\r%{:^3.0f}[{}->{}]".format(c,a,b),end = "")
    time.sleep(0.1)
print("Over")
          
