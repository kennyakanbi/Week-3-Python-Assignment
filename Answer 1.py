# Creating function that calculates the final price after applying a discount. 
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

# Calculate the discounted price 
    discounted_price = price - (price * discount_percent / 100) 
    return discounted_price  
else: 
# Return the original price 
    return price
# Example usage 
original_price = 100.0
discount = 25.0 

final_price = calculate_discount(original_price, discount) 

print(f"The final price is: ${final_price:.2f}")
