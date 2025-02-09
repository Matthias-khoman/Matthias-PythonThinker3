# Task 1
BOS = {'Notebook':2.50,'Pencil':0.50,'Pen':1.20,'Ruler':1.50,'Eraser':0.50,'Writing Pad':2.50,'Marker':2.00,'Glue':3.00,'Calculator':35.00}

def display_BOS():
    print('---------Welcome to MBK----------')
    for item, price in BOS:
        print("{:^30}:${:^8.2f}".format(item, price))
    print('spend $20 to get 10% off')

customer_order={}

def take_order(BOS, order, quantity,  customer_order):
    if order in BOS:
        print(f'{order} has been added')
        customer_order[order] = {'quantity': quantity, 'cost': BOS[order]}
    else:
        print("We don't sell that")



def order_summary(customer_order):
    print('-----------Order Summary------------')
    for order, quantity_cost in customer_order.items():
        quantity = quantity_cost[quantity]
        cost = quantity_cost[cost]
        print(f'{order} x {quantity} at {cost} each')
        total_price


        