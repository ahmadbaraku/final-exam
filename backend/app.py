products = [
    [1, 'Programming Skills', 68],
    [2, 'AI Development', 104],
    [3, 'Networking Systems', 77],
    [4, 'Cyber Security', 62],
    [5, 'Data Structure', 48]
]

print('List of books:')
for book in products:
    print(str(book[0]) + "- " + book[1] + ' , Price: ' + str(book[2]) + ' $')

f_num = int(input('Choose book number to get amount with tax: '))
if f_num == 1:
    print('The book price is: ' + str(products[0][2] * 1.15))
elif f_num == 2:
    print(products[1][2] * 1.15)
elif f_num == 3:
    print(products[2][2] * 1.15)
elif f_num == 4:
    print(products[3][2] * 1.15)
elif f_num == 5:
    print(products[4][2] * 1.15)
else:
    print('Your choose is not in the list of books')