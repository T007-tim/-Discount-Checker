#This is a discounted price calculator in python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get input from user
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display the result
if final_price < price:
    print(f"Discount applied! Final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. Final price is: ${final_price:.2f}")


 