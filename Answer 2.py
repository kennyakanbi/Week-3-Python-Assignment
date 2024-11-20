# Using calculate_discount function, prompt the user to enter the original price of an item 
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.
        
    Returns:
        float: The final price after applying the discount if the discount is 20% or higher.
               Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Main program
def main():
    # Prompt user for the original price
    original_price = float(input("Enter the original price of the item: "))
    
    # Prompt user for the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)
    
    # Display the result
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${final_price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")

# Run the program
if __name__ == "__main__":
    main()
