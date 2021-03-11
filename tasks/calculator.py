#Opted for use of eval() as it's significantly less code than selecting the operation conditionally.
#I'm aware of the security risks of eval() but in this context it's fine.
def calculator(a, b, operator):
    operation = "%s%s%s" % (a, operator, b)
    return int(eval(operation))

# In case you were looking to see it done manually, I've included that below.
def calculator2(a, b, operator):
    if operator == "+":
        return int(a + b)
    elif operator == "-":
        return int(a - b)
    elif operator == "*":
        return int(a * b)
    elif operator == "/":
        return int(a / b)

print(calculator(2, 4, "+")) # Should print 6 to the console
print(calculator(10, 3, "-")) # Should print 7 to the console
print(calculator(4, 7, "*")) # Should print 28 to the console
print(calculator(100, 2, "/")) # Should print 50 to the console
