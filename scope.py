balance = 580

def total_cost(price,quantity):
    global balance
    cost = price*quantity
    #balance = 100
    #remaining = balance-cost
    #balance = remaining
    #print(remaining)
    balance = balance - cost
    return cost

print(f'balance: outside before:{balance}')

pay = total_cost(10,3)
print(f' Please pay:{pay}')

print(f'balance: outside after:{balance}')

# def f1():
#     global x
#     x+=1
#     print(x)
# x=12
# print("x")