name = input("Enter your name: ")
age = float(input("Enter your age: "))
numtik = float(input("How many tickets do you want? "))
if(age<13):
    ttype= "Child"
    cost=8
elif(age<=64):
    ttype= "Adult"
    cost=12
else:
    ttype="Senior"
    cost=9

print(f"\n=== MOVIE TICKET RECEIPT ===\nCustomer: {name}\nTicket Type: {ttype} (${cost}.00 each)\nQuantity: {numtik}\nTotal Cost: ${cost*numtik}\nThank you for your purchase!")