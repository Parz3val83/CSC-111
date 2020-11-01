user_input = ''

while user_input != 'q':
    try:
        money = float(input("Enter the amount of money : "))
        if money < 0:
            raise Exception('Invalid amount.')

        item_price = float(input("Enter the price of the item: "))
        if item_price < 0:
            raise Exception('Invalid amount.')

        number_of_items = int(money/item_price)
        print('The number of items that you can purchase is :', number_of_items)
        
    except ZeroDivisionError:
        print('Cannot enter 0. Enter a natural integer.')
    except ValueError:
        print('Cannot Enter a string.') 
    user_input = input("Enter any key ('q' to quit): ")
