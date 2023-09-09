#You have been given sales data in the form of a list of tuples. Each tuple represents a sale, 
#containing the following information: (product_name, quantity, price_per_unit). 

    
    
sales_data = [
    ("ProductA", 10, 5.0),
    ("ProductB", 5, 7.5),
    ("ProductA", 8, 5.0),
    ("ProductC", 15, 2.0),
    ("ProductB", 3, 7.5),
]

#1. Calculate the total revenue from all sales.
total_revenue = 0
for sale in sales_data:
    total_revenue += sale[1] * sale[2]
print("Total revenue: {}" .format(total_revenue))

#aalternative code1
print()
print("Total revenue: " + str(sales_data[0][1] * sales_data[0][2] + sales_data[1][1] * sales_data[1][2]
        + sales_data[2][1] * sales_data[2][2] + sales_data[3][1] * sales_data[3][2] + 
        sales_data[4][1] * sales_data[4][2]))
    
#Alternative code2
total_revenue1 = sum(quantity * price for _, quantity, price in sales_data)
print(f"Total revenue : {total_revenue1}")

#2. Find the product that generated the highest revenue.
Product_A = []
Product_B = []
Product_C = []
producta, productb, productc = 0, 0, 0
for sale in sales_data:
    match sale[2]:
        case 5.0:
            Product_A.append(sale)
            producta += sale[1]*sale[2]

        case 7.5:
            Product_B.append(sale)
            productb += sale[1]*sale[2]

        case 2.0:
            Product_C.append(sale)
            productc += sale[1]*sale[2]
        case _:
            pass

list = [producta, productb, productc]
if producta == max(list):
    print("ProductA generated maximum revenue")
elif productb == max(list):
    print("ProductB generated the maximum revenue")
else:
    print("ProductC generated the maximum revenue")
    
#Alternative code

product_revenues = {}
for product, quantity, price in sales_data:
    revenue = quantity * price
    product_revenues[product] = product_revenues.get(product, 0) + revenue
print(product_revenues)

max_product = max(product_revenues, key= product_revenues.get) # type: ignore
print(f"{max_product} generated the maximum revenue")


#3. Create a dictionary that shows the total quantity sold for each product

diction = {"ProductA": producta,
           "ProductB": productb,
           "ProductC": productc}

