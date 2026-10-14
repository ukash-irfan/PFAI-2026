usd = float(input("Enter amount in USD: "))
rate = float(input("Enter exchange rate: "))

local_amount = usd * rate

print("Converted amount =", round(local_amount, 2))