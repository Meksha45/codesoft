print("1.\t add")
print("2.\t diff")
print("3.\t mutli")
print("4.\t div")
choice=int(input("enter your choice="))
if(choice==1):
   a=int(input("enter a number="))
   b=int(input("enter a number="))
   sum=a+b
   print(sum)
elif(choice==2):
   a=int(input("enter a number="))
   b=int(input("enter a number="))
   diff=a-b
   print(diff)
elif(choice==3):
   a=int(input("enter a number="))
   b=int(input("enter a number="))
   mutli=a*b
   print(mutli)
elif(choice==4):
   a=int(input("enter a number="))
   b=int(input("enter a number="))
   div=a/b
   print(div)
