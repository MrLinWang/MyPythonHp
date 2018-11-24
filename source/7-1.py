textFile = open("7.1.txt","rt") #t 表示文本文件方式
print(textFile.readline())
textFile.close()
binFile = open("7-1.txt","rb") #r 表示二进制文件方式
print(binFile.readline())
binFile.close()
