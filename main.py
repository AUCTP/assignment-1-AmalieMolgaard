#This assingment is made by Amalie Mølgaard Nielsen and Rikke Mia Petersen

#In this assignment, you will create a simulation of the university cafeteria where customers arrive, 
#purchase items, and leave. The program should track the inventory of the items, simulate customer 
#transactions, and generate a report of the day's sales.

import random 

print("The canteen is now open for today")

#Task 1: items: List of product names, prices: List of product prices, inventories: List of product inventories.
items = ["Sandwich", "Salad", "Cake", "Bun", "Coffee", "Iced Coffee", "Water", "Soda"]
prices = [50, 45, 30, 20, 25, 30, 20, 25]
inventories = [100, 50, 30, 50, 200, 150, 50, 50]

#Task 2: Simulate customers
def simulate_customers(customerNumber): #defines a function that takes one parameter - how many customers visit the cafeteria 
    sales = [] #empty list sales, that will store all the items that were bought by customers
    
    for i in range(customerNumber): #a definite loop that repeats for each customer. i starts at 0 and increases by 1 for each customer
        print(f"\nCustomer no.{i + 1}:") #prints the customer number (starting at 1 instead of 0)
        buy = random.choice([True, False]) #randomly picks whether the customer decides to buy or not. random.choice() chooses True or false with 50/50 chancee

        if buy == True: #if this condtion is true, python moves to the nextblock of code
            item = random.choice(items) #randomely selects a product from the items list
            index = items.index(item) #finds the position(index) of the selected item in the items list

            if inventories[index] > 0: #checks if there is stock available for the item
                inventories[index] -= 1 #if stock is available the customer can buy it and the inventory reduces by 1
                sales.append(item) #adds the bought item to the sales list
                print(f"The customer bought a {item}")
            else:
                print(f"The customer wanted a {item}, but was not able to buy it, as it was out of stock.") #if there was no stock, priints a message saying that the customer couldn't buy the item

        else: #this runs when buy == false, meaning the custoemr chose not to buy anything
            print("The customer did not buy anyting today")
    
    return sales #after all customers have been processed, the function returns the list of all successful sales

#run simulation
sales_today = simulate_customers(10)

#Task 3: process sales and total revenue
def process_sales(sales):
    total_revenue = 0 #starts with zero income
    for sale in sales: #go through every item that was sold
        index = items.index(sale) #find the position of the item in the list
        total_revenue += prices[index] #add its price to the total 
    return total_revenue

# Task 4: Generate sales report
def generate_report(sales): #defines a function for the sales report
    print("\n DAILY SALES REPORT ")
    total_revenue = process_sales(sales)  # calculates the total revenue
 
  #prints how many of each item was sold and reaming stock
    for i in range(len(items)): #go through all items
        sold_count = sales.count(items[i]) #count how many times the item was sold
        print(f"{items[i]}: sold {sold_count}, remaining stock: {inventories[i]}")
    
  #print the total revenue for the day
    print(f"\nTotal revenue: {total_revenue}")

# Run the simulation
sales_today = simulate_customers(10) #ssimulates 10 customers visiting the cafeteriaa 
generate_report(sales_today) #generates the daily sales report

# Task 5: Calculate the cost of leftover items
def leftover_inventory():
    total_cost = 0  # start from zero cost

    for i in range(len(items)):  # loop through all items by index
        leftover = inventories[i]              # how many are left
        cost_per_item = prices[i] / 2          # production cost is half the price
        total_cost += leftover * cost_per_item # add cost for this item

    return total_cost

# calculate leftover costs
total_cost = leftover_inventory()
print(f"Total cost of leftover items: {total_cost}")










