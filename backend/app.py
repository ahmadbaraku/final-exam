products = [
    ['apple', 10],
    ['orange', 5],
    ['banana', 12],
    ['date', 20],
    ['strawberry', 16]
]

for fruit in products:
    print("Fruit: "+fruit[0]+ ", amount: "+ str(fruit[1]))

f_num = input('Choose fruit number to get amount with tax: ')
print(f_num)