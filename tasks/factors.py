#I think this method is best as it takes into account that when i is a factor, number/i is also a factor.
#This means it's only neccesary to loop until √number, because all factors beyond that will already be included.
def factors(number):
    result = []
    i = 1
    if number < 0:
        return "Please enter a positive number!"
    while i*i <= number:
        if i != 1:
            if number % i == 0:
                result.append(i)
                if number//i != i:
                    result.append(number//i)
        i += 1
    return sorted(result)

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “[]” (an empty list) to the console
