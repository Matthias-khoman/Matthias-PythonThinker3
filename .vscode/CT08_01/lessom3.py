# Task 1
BOS = {'Notebook':2.50,'Pencil':0.50,'Pen':1.20,'Ruler':1.50,'Eraser':0.50,'Writing Pad':2.50,'Marker':2.00,'Glue':3.00,'Calculator':35.00}

def display_BOS():
    print('---------Welcome to MBK----------')
    for item, price in BOS:
        print("{:^30}:${:^8.2f}".format(item, price))
        
        