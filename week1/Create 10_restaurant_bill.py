food_price = float(input("Enter food price: "))
tax = float(input("Enter tax percentage: "))
discount = float(input("Enter discount percentage: "))
service_charge = float(input("Enter service charge: "))

# 1. Add tax
amount_after_tax = food_price + (food_price * tax / 100)

# 2. Subtract discount
amount_after_discount = amount_after_tax - (amount_after_tax * discount / 100)

# 3. Add service charge
final_bill = amount_after_discount + service_charge

# 4. Display final bill
print(f"Final bill = {final_bill:.2f}")