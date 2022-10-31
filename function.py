# from unittest import result


def double_it(num):
    result = num * 2
    print(result)

# double_it(40)

def add(num1,num2):
    total = num1+num2
    #print(total)
    return total

# add(40,50)
sum = add(56,23)
print(sum)

def multiply (num1,num2):
    result = num1*num2
    return result

output = multiply(25,6)
print(output)

final_number = add(sum,output)
print('final number',final_number)

