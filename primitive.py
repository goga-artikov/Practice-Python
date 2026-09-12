print("==================");
# in JAVA, variable is a name storage location
# in Python, variable is named reference

count = 100
count_type = type(count)
print("count:", count)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count() #method of int class
result2 = count.numerator #state
print(result1, result2)

print("========= string =========");

course = "AI Python Full Stack"
result = type(course)
print(f"the result (1): {result}")

result = course.title() #method
print(f"the result (2): {result}")

result = course.upper() #method
print(f"the result (3): {result}")

result = course.replace("FullStack", "MasterClass") #method of str class
print(f"the result (4): {result}")

print("========= boolean =========")
# functions > type() input() bool() str()
y = input("give your value for y")
print("y:", y, "type(y):", type(y))

# truthy vs falsy values
# truthy > true 100 -100 "mit"
# falsy > false 0 "" None

test_falsy = "" or False or None or 0
print(f"the result (5): {test_falsy}")

test_truthy = "mit" or True or 100 or -100
print(f"the result (6): {test_truthy}") 