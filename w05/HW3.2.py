def format_transformer(dishes):
    dish_list = dishes.split(";")
    meal, num, price, discount = dish_list
    quantity = int(num)
    uni_price = float(price)

    if "DISC" in discount:
        discount = float(discount.replace("DISC", ""))
        real_discount = (100 - discount)/100
        subtotal = uni_price * quantity * real_discount
        # print(real_discount)
    else:
        discount = 0
        subtotal = uni_price * quantity
        # print(discount)

    return meal, quantity, uni_price, subtotal

num_of_ppl = int(input())

for i in range(num_of_ppl):
    name = input()
    print(f"Customer: {name}")

    items = int(input())
    print(f"Number of Items: {items}")

    print("Order Details:")
    count = 1
    total_cost = 0

    for j in range(items): # 看他點了什麼、金額各自多少
        dishes = input()
        meal, quantity, price, subtotal = format_transformer(dishes)
        print(f"{count}. {meal} - Quantity: {quantity}, Unit Price: {price:.2f} TWD, Subtotal: {subtotal:.2f} TWD")
        count +=1
        total_cost += subtotal
    
    print(f"Total Cost: {total_cost:.2f} TWD")
   
    if i < num_of_ppl - 1:
        print()

