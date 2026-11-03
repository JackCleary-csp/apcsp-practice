def drink_price(size, extra):
    if size == "S":
        price = 3
    elif size == "M":
        price = 4
    elif size == "L":
        price = 5
    if extra == "Y":
        price += 1
    elif extra == "N":
        price = price
    return price
    

def serve_customer(customer_number, drink_count):
    current_price = 0
    for i in range(0, int(drink_count), 1):
        size = input().upper()
        extra = input().upper()
        current_price += drink_price(size, extra)
    print( "CUSTOMER " + str(customer_number) + ": $" + str(current_price))
    return current_price
    
def main():
    total_price = 0
    customers = int(input())
    for i in range(0, customers, 1):
        total_price = 

main()

    
    
    
    