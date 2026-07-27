user_name=input("What's your name?")

item_price=int(input("Enter item price"))

quantity=int(input("Enter item quantity"))

total_amount=(item_price*quantity)
if total_amount> 1000:
    print("discount 20%")
    discount=20
    discount_total_amount=(item_price*quantity)-(item_price*quantity*.10)
    
elif total_amount>500:
    print("discount 10%")
    discount=10
    discount_total_amount=(item_price*quantity)-(item_price*quantity*.20)

print(f"Bill for {user_name}: Total = {total_amount}, Discount = {discount}%, Total after discount = { discount_total_amount}  ")