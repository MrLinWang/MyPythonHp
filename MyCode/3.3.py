#P93 3.3 天天向上续
i=1
power=1
while i<=365:
    for j in range(1,8):
        if i%10==0:
            i+=1
            break
        if j>3:
            power*=1.01
        i+=1
print("{}".format(power))
