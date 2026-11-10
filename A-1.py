items = ['pencil', 'pen', 'eraser', 'note', 'glue']
stock_count = [10, 35, 5, 10, 0]

inventory = {item: count for item, count in zip(items, stock_count)}
print("Total Inventory: ", inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print("The items in stock are: ", in_stock_items)

chosen_item = input("What product would you like to buy?: ")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print("That particular item is not available or not in stock. ")
    exit()

prices = [5, 10, 50, 20, 25]
markup = int(input("Enter the markup amount to add to the price of items: "))

marked_up_prices = list(map(lambda p: p + markup, prices))
print("After marking up the prices: ", marked_up_prices)

