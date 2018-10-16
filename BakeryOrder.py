## LESSON REQUIREMENTS
## Write a short script
## A numbered list of baked goods is displayed for sale
## Each item has 5 in stock when the program starts
## User can enter the ID (1, 2, 3, etc.) of the item they want
## User can enter how much of the item they want
## Stock for each item decreases as they are ordered
# If no more of an item is available, the user is told their order cannot be fulfilled.
## HINTS:
## Use if statements to handle different cases
## Use a while loop to run the program continuously
## You can choose whatever items you want, but you should probably have a variable for each item’s stock

#>>>>>>>BAKERY<<<<<<<<

#CREATE MENU
menu = '1) Blueberry Muffins, 2) Banana Muffins 3) Cinnamon Rolls 4) Cherry Pastries, 5) Kolaches'

#CREATE INVETORY FOR MENU ITEMS USING LIST METHOD
inventory = ['1', '1', '1', '1', '1','2', '2', '2', '2', '2','3', '3', '3', '3', '3','4', '4', '4', '4', '4','5', '5', '5', '5', '5']

#WHILE LOOP TO CONTINUOUSLY RUN PROGRAM FOR BLUEBERRY MUFFINS

while len(inventory):

    print('On our menu today we have:', menu)

    #PRINT MESSAGE TO END USER ASKING WHAT THEY WOULD LIKE TODAY
    print("To place your order, enter the menu number of the item you'd like.")

    #TAKE CUSTOMER ORDER
    order = input('What can we make for you today? ')

    #TAKE CUSTOMER DESIRED QUANITY
    quantity = input('How many would you like? ')
    quantity = int(quantity)

    #FOR LOOP TO CHECK CUST REQUEST
    item_count = 0

    for item in inventory:
        if item == order:
            item_count = item_count+1

    print('available inventory', item_count)
    print('quantity', quantity)

    #IF STATEMENTS
    if quantity > item_count:
        print ("We're sorry but your order cannot be fufilled.")

    if quantity <= item_count:
        print('Thanks so much for your order, it will be right out.')

        if order == '1' and \
        quantity == 1:
            inventory.remove(order)

        if order == '2' and \
        quantity ==1:
            inventory.remove(order)

        if order == '3' and \
        quantity ==1:
            inventory.remove(order)

        if order == '4' and \
        quantity ==1:
            inventory.remove(order)

        if order == '5' and \
        quantity ==1:
            inventory.remove(order)

        if order == '1' and \
        quantity == 2:
            inventory.remove(order)
            inventory.remove(order)

        if order == '2' and \
        quantity == 2:
            inventory.remove(order)
            inventory.remove(order)

        if order == '3' and \
        quantity == 2:
            inventory.remove(order)
            inventory.remove(order)

        if order == '4' and \
        quantity == 2:
            inventory.remove(order)
            inventory.remove(order)

        if order == '5' and \
        quantity == 2:
            inventory.remove(order)
            inventory.remove(order)

        if order == '1' and \
        quantity == 3:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '2' and \
        quantity == 3:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '3' and \
        quantity == 3:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '4' and \
        quantity == 3:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '5' and \
        quantity == 3:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '1' and \
        quantity == 4:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '2' and \
        quantity == 4:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '3' and \
        quantity == 4:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '4' and \
        quantity == 4:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '5' and \
        quantity == 4:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '1' and \
        quantity == 5:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '2' and \
        quantity == 5:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '3' and \
        quantity == 5:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '4' and \
        quantity == 5:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if order == '5' and \
        quantity == 5:
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)
            inventory.remove(order)

        if not inventory:
            print("Our food is amazing and we're out for the day. Try again tomorrow!")

    print(inventory)


