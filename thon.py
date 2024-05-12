# n=int(input("enter for n"))
# for i in range(n):
#     for j in range(i+1):
#         print(i,end=" ")
#     print()     


# class computer:
#     def config(self):
#         print("i5,16gb,1tb")
# a='7'        
# print(type(a))
# com1=computer()
# print(type(com1))   


# class computer:
#     def config(self):
#         print("i5,16gb,1tb")
# com1=computer()        
# com2=computer()
# com3=computer()
# computer.config(com1)  
# computer.config(com2)
# computer.config(com3)
# com1.config()
# com2.config()

# class box:
#     def open(self):
#         a="hello world"
#         print(a)
# ob1=box()
# ob1.open()      
# box.open(ob1)    

#the class constructor(__init__)

# class computer:
#     def __init__(self):              #init use is itself is called
#         print("hi init")
# com1=computer()      

# class computer:
#     def __init__(self,andr,mac):  #here the self is object com1
#         self.andr=andr
#         self.mac=mac
#     def brand(self):
#         print("the computers are",self.andr,self.mac)
# com1=computer("samsung",3)
# com2=computer("apple",2)
# com1.brand()
# com2.brand() #def brand calls

