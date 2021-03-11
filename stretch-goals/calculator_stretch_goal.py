#This is my preferred solution, with a couple of alternatives included as comments.
def calculator(a, b, operator):
    operation = "%s%s%s" % (a, operator, b)
    calc = int(eval(operation))
    binary = format(calc, 'b')
    #binary = bin(calc).replace("0b", "")
    #binary = "{0:b}".format(calc)
    return int(binary)

#In case you were looking to see it done manually, I've included that below.
def list_to_str(list1):
    string_list = [str(value) for value in list1]
    return "".join(string_list)
    
def convert_to_binary(dec):
    binary = []
    while dec > 0:
        binary.append(dec % 2)
        dec = int(dec/2)
    binary.reverse()
    return int(list_to_str(binary))

def calculator2(a, b, operator):
    if operator == "+":
        calc = int(a + b)
        return convert_to_binary(calc)
    elif operator == "-":
        calc = int(a - b)
        return convert_to_binary(calc)
    elif operator == "*":
        calc = int(a * b)
        return convert_to_binary(calc)
    elif operator == "/":
        calc = int(a / b)
        return convert_to_binary(calc)

print(calculator(2, 4, "+")) # Should print 110 to the console
print(calculator(10, 3, "-")) # Should print 111 to the console
print(calculator(4, 7, "*")) # Should output 11100 to the console
print(calculator(100, 2, "/")) # Should print 110010 to the console
