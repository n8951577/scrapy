#def main():
f = open("file_write.txt","w+")  #open a file in write mode
f.write("hai")
f.close()

#append
f1 = open("file_append.txt","a+")
f1.write("Hello welcome to the world of Python")
f1.close()

#In Read mode
f = open("file_write.txt","r")
f1 = f.read()
print(f1)

#if __name__== "__main__":
 #   main()