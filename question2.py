print("=== RESTAURANT MENU ===")
print("1. Pizza - $15.99")
print("2. Burger - $12.50")
print("3. Salad - $9.99")
print("4. Pasta - $13.75\n")

choice= input("Enter your choice (1-4): ")
drink = input("Would you like a drink? (+$2.50) (yes/no): ")

print("=== YOUR ORDER ===")
fcost=0
if(choice=="1"):
    fcost=12.99
    print("Food: Pizza - $15.99")
elif(choice=="2"):
    fcost=12.50
    print("Food: Burger - $12.50")
elif(choice=="3"):
    fcost=9.99
    print("Food: Salad - $9.99")
elif(choice=="4"):
    fcost=13.75
    print("Food: Pasta - $13.75")

if(drink=="yes"):
    print("Drink: Yes - $2.50")
    print(f"Subtotal: ${fcost+2.5}")
    print(f"Tax (8%): ${(fcost+2.5)*.08}")
    print(f"Total: ${(fcost+2.5)*1.08}")
elif(drink=="no"):
    print("Drink: No - $0.0")
    print(f"Subtotal: ${fcost}")
    print(f"Tax (8%): ${(fcost)*.08}")
    print(f"Total: ${(fcost)*1.08}")
