print("======= Iterable objects & RANGE =========")
# Iterable objects > string dictionary list tuple list range map filter

range_obj = range(10)  # range object
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")

print("======= Dictionary =========")
# Dictionary is JSON object
person = {"name": "Goga", "age": 30, "marriage": True}
person_obj = dict(name="Goga", age=30, marriage=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# method: get() > return value of key or None if key not found
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)  # default value if key not found
print(f"the name: {name}, hobby: {hobby}, and balance: {balance}")

del person_obj["marriage"]  # delete key-value pair
for key in person_obj:
    print(f"the key: {key}, value: {person_obj.get(key)}")