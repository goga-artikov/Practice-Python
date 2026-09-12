# dunder __builtins__, __init__

message = "PYTHON: Everthing is object !"
print(message)

result = type(message)
print("result:", result);

''' In Python, there are builtin tools:
(1) types > int float str list dict
(2) functions > print() input() len() type() str()
(3) constants > True False None
'''

print(__builtins__)