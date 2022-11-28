#this is a dictionary containing the menu items that we have,
#being mapped to specific keys that appear on the menu
#the keys are what we use to choose the items from the menu
MENU = {
    "A":"soda",
    "B":"french_fries", 
    "C":"burger", 
    "D":"milkshake", 
    "E":"cookies",
    "F":"juice_box"
}

# this is the function that is used to make an order.
#it keeps a list of the items that a customer chooses from the menu and that list is then 
#returned when the customer is done making an order
def pick_order():
    current_order = []
    while True:
        print("What can I get for you?")
        order = input()
        if order in MENU:
            current_order.append(MENU[order])
        else:
            print("I'm sorry, we don't serve that.")
            continue
        
        if is_order_complete():
            return current_order


#here we check to see whether the customer is done ordering from the menu by prompting
#them to enter either yes or no and then returning a boolean value basing on the input received 
def is_order_complete():
    print("Anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")


#this function prints out the items in the order list
def output_order(order_list):
    print("Okay, so you want")
    for order in order_list:
        print(order)


def main():
    ShowMenu()
    order = pick_order()
    output_order(order)
    BillingSystem(order)
    print("Please drive through to the second window.")
    
####BILLING SYSTEM
# this is the function that calculates the total cost of all the items that are the customers'
#order list
def BillingSystem(order):
    # this dictionary maps prices to the names of the items on the menu
    billing = {    
    "soda" : 1600,
    "french_fries" : 7000,
    "burger" : 15000,
    "milkshake" : 10000,
    "juice_box" : 2000,
    "cookies" : 1000,
    }

    total = 0.0

    #here we loop through the order list and check for the names of the items that the customer has ordered for
    #then we get the associated price of that item from the billing dictionary and add it to the total
    for item in order:
        if item in billing:
            total += billing[item]

    print("Final total:**********", total)
            

#this function prints out themenu to the customer
def ShowMenu():
    soda = 1600
    french_fries = 7000
    burger = 15000
    milkshake = 10000
    juice_box = 2000
    cookies = 1000
    total = 0.0
    print("""
    +-------------------------------------------+
    | The Restaurant For All Dreams** |
    +---------------------------------+---------+
    | A\tThe "Big Boy" Soda      | $""" + str(soda) + """  |
    +---------------------------------+---------+
    | B\tFrench Fries              | $""" + str(french_fries) + """   |
    +---------------------------------+---------+
    | C\tCelebrity Burger           | $""" + str(burger) + """  |
    +---------------------------------+---------+
    | D\tMilkShake  | $""" + str(milkshake) + str(0) + """  |
    +---------------------------------+---------+
    | E\tJuice Box                 | $""" + str(juice_box) + """  |
    +---------------------------------+---------+
    | F\tCookies                 | $""" + str(cookies) + """  |
    +---------------------------------+---------+
    """)
    
#if _name_ == "_main_":
main()