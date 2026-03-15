def get_final_price(base_price, discount_code):
    if discount_code == 'FRIEND':
        return base_price - (base_price*0.2)
    elif discount_code == 'VIP':
        return base_price - (base_price*0.5)
    else:
        return base_price


price1 = get_final_price(100, 'FRIEND') # Returns 80
price2 = get_final_price(100, 'VIP')    # Returns 50
price3 = get_final_price(100, '')       # Returns 100

# 3. Display
print(f"Friend paid: ${price1}")
print(f"VIP paid: ${price2}")
print(f"Regular paid: ${price3}")