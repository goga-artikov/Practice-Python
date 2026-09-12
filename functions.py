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
