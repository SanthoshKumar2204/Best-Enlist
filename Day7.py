def greet(x):
	print("Hello "+x)
x=input()
greet(x)

#Multiple input
def greet(x):
  print("Hello "+ str(x))
greet('Santhosh')
greet('Kumar')

# Two Arguements
def team(World):
  print(India + " vs " + NewZealand)
team("Dhoni" , "Kane")

def ipl(*team):
  print(team)
ipl("Csk ","Rcb "," Mi")

def student(B,A,C):
  print(A)
student("Akshaya","Banu","Charu") #order of the arguments matters
student(A="Akshaya",B="Banu",C="Charu") # Assigning by key Value
#order of the arguments does not matter



def math(num1,num2):
  print("Addition of two numbers",num1+num2)
  print("Subtraction of two numbers",num1-num2)
  print("Multplication of two numbers",num1*num2)
  print("Division of two numbers",num1/num2)
num1=float(input("input the number one: "))#input from user for num1
num2=float(input("input the number one: "))#input from user for num2
math(num1,num2)





