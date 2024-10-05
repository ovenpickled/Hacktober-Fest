None1 = "some_value"
if None == "some_value":
    print("This shouldn't work, None is a keyword!")
True1 = 1
if True: 
    print("This will cause an error because 'True' is a reserved keyword.")

x=5
def for1(x):
    return x * 2

result = for1(5)
print(result)  

if result > 5:
    print("You can't use 'return' as a variable name!")

class1 = "AdvancedPython"
print("This won't work because 'class' is a reserved keyword in Python.")

