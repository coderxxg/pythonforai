print("hello world")
print("i am learning ai")
name = "rohan"
long_string="""My name is rohan 
and i work in IT """
print(long_string)
age = 27
is_incorporate = True
print(age)
#comments
"""
comments big ones

Data types
Numbers
1. Integer 
2. float 
string 
boolean
"""

total = 5+5
print(total)
can_vote = age>=20
print(can_vote)
temperature = 30
if temperature >30:    
    print("its very hot")
if temperature > 25:
    print("its hot")
else:
    print("its nice weather")
#Dict is like phone book 
person= {
    "name":'rohan',
    "age": 25 ,
    "city": "Bhilwara"
}

person["name"]="Dave"
print(person)
#list is like grocery list with curly bracket
#add
list = {"name",27,"name"}
print(list)
#tuple is like imutable 
empty =()
point=(3,5)
colours = ("red","green","blue")
print(colours)

#sets is bag of unique marble 
unique_bag= set(list)
print(unique_bag) 
# testing gits
print("checkgit")
# functions 
def greet(name):
    print(f"hello!!,{name}")
pass

greet(name="dave")

def add_return(a,b):
    return a + b 

add_return(a=2,b=3)

