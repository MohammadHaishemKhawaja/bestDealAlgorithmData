##AMOUNT OF TIMES USER RESTARTS
times = []
##VARIABLE TO RESTART LOOP
i = 0
while i < 3:
    ##PRICE SHIPPING AND AMOUNT OF ITEMS
    price = input ("Enter price of Item: ")
    shipping = input ("Enter price of Shipping: ")
    amount = input ("Enter amount of Items: ")
    ##CALCULATION 
    results = (float(price)) + (float(shipping)) / (float(amount))
    ##ASSIGN DATA TO ARRAY
    times.append(results)
    ##SORTS DATA WITHIN ARRAY
    times.sort()
    ##ASKS TO KEEP LOOP GOING
    question = input("Do you want to keep adding items?: ")
    ##RESTARTS LOOP
    if (question == 'yes') or (question == 'Yes'):
        i = 0
    ##ENDS LOOP
    else:
        i = 4
        print(times[0], "is your best deal so far")


