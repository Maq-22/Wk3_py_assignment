def calculate_discount(price, discount_percent):
    """Return the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Ask the user for inputs
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Print the result formatted to 2 decimal places
print(f"Final price: {final_price:.2f}")

