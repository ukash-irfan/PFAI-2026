def average(a, b):
    return (a + b) / 2


def double(number):
    return number * 2


try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid input! Please enter a numeric value.")

ali_mark = 88 
if ali_mark >= 85: 
    print("Ali: A") 
elif ali_mark >= 70: 
    print("Ali: B") 
else: 
    print("Ali: below B")  

sara_mark = 73 
if sara_mark >= 85: 
    print("Sara: A") 
elif sara_mark >= 70: 
    print("Sara: B") 
else: 
    print("Sara: below B")  