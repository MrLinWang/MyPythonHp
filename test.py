length = input()
if length[-1]=='m':
    print("{:.3f}in".format(eval(length[0:-1])*39.37))
elif length[-1]=='n':
    print("{:.3f}m".format(eval(length[0:-2])/39.37))
