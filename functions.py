''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parameters vs Arguments
(3) Keyword vs Default Arguments
(4) Scope
'''

print("======= define vs call =========")
# build in function > print() input() len() type() str()
# function - reusable block of code
# instead of block {} in JAVA, Python uses indentation!

# define - build - parameters

def greet(a):
    print(f"How do you do, {a}?")

def greeting(b):
    print(f"greeting is executed")
    return f"Hello, {b}!"

# call - execute
result1 = greet('Goga')
print("result1:", result1)

result2 = greeting('Artikov')
print("result2:", result2)


print("======= keyword and default arguments =========")

# define 
def give_greet(name, age):
    print ("give_greet is executed")
    return f"Hi, {name}! You are {age} years old."

# call
result3 = give_greet(name="Goga", age=30) # keyword arguments
print("result3:", result3)

result4 = give_greet("John", 23)
print("result4:", result4)

print("======= scope =========")
b = 100

# define
def calculate(a, b):
    c= a + b
    print(f"the c value is: {c}")

# call
calculate(5, 50)