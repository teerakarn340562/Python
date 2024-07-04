# Name = ["beam","golf","fiat","nick","peace"]
# for i in Name:
#     print(i)

def sum_func(valuse_1,valuse_2):
    print(valuse_1,"+",valuse_2,"=",valuse_1+valuse_2)

def delete_func(valuse_3,valuse_4):
    print(valuse_3,"-",valuse_4,"=",valuse_3-valuse_4)

def multiply_func(valuse_5,valuse_6):
    print(valuse_5,"*",valuse_6,"=",valuse_5*valuse_6)

def divide_func(valuse_7,valuse_8):
    print(valuse_7,"/",valuse_8,"=",valuse_7/valuse_8)
func = int(input("1: function sum\n2: function delete\n3: function multiply\n4: function divide\nClect_function : "))
if func == 1:
    valuse_1 = int(input("1 : "))
    valuse_2 = int(input("2 : "))
    print("Function Sum")
    sum_func(valuse_1,valuse_2)
elif func == 2:
    valuse_3 = int(input("1 : "))
    valuse_4 = int(input("2 : "))
    print("Function Delete")
    delete_func(valuse_3,valuse_4)
elif func == 3:
    valuse_5 = int(input("1 : "))
    valuse_6 = int(input("2 : "))
    print("Function Multiply")
    multiply_func(valuse_5,valuse_6)
elif func == 4:
    valuse_7 = int(input("1 : "))
    valuse_8 = int(input("2 : "))
    print("Function Divide")
    divide_func(valuse_7,valuse_8)
else:
    print("Error")
# dsfsdf

# def addvolumn():
#     print("เพิ่มเสียง")
# def delvolunm():
#     print("ลดเสียง")
# def turn_off_TV():
#     print("ปิด TV")
# addvolumn()
# delvolunm()
