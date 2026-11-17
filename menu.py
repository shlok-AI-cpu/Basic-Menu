print('hey customer')
name = input('please enter your name: ')
print(f'welcome to the xyz cafe, {name}!')
print('please select your order from the menu below ')
menu = {
    '1': {'item': 'Coffee', 'price': 49.5},
    '2': {'item': 'Tea', 'price': 20.0},
    '3': {'item': 'Juice', 'price': 30.0},
    '4': {'item': 'Sandwich', 'price': 50.0},
    '5': {'item': 'Salad', 'price': 30.0},
    '6': {'item': 'pastry', 'price': 39.5},
    '7': {'item': 'chilli potato', 'price': 79.5},
    '8': {'item': 'burger', 'price': 39.5},
    '9': {'item': 'pizza', 'price': 130.0},
    '10': {'item': 'pasta', 'price': 55.5},
    '11': {'item': 'veg maggie', 'price': 45.0},
    '12': {'item': 'momos', 'price': 40.0}
}
print("menu:")
for key, value in menu.items():
    print(f"{key}. {value['item']}: ₹{value['price']}")
grand_total = 0
while True:

    input1 = input(
        'Enter item number (1-12) or type no to finish: '
    ).lower()

    if input1 == 'no':
        break

    if input1 in menu:

        item = menu[input1]['item']
        price = menu[input1]['price']

        input2 = input('Enter quantity: ')

        quantity = int(input2)

        if quantity <= 0:
            print('Please enter a valid quantity.')
            continue

        total_price = price * quantity

        print(f'You ordered {quantity} {item}(s).')
        print(f'Item total: ₹{total_price}')
        grand_total = total_price + grand_total
    else:
        print('Invalid choice. Please select a valid option.')
        


print(f'Thank you for your order, {name}!')
print(f'The total amount to be paid is: ₹{grand_total}')
print('Have a great day and meal!')

