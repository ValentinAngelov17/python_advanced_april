def shop_from_grocery_list(budget, grocery, *args):
    grocery_list = grocery
    purchase_products = []
    missing_products = []
    shopping = args
    for product, value in shopping:
        if budget < value:
            break
        if product in grocery_list:
            if product not in purchase_products:
                if budget >= value:
                    budget -= value
                    purchase_products.append(product)
                    grocery_list.remove(product)
        if product not in purchase_products:
            missing_products.append(product)

    if len(grocery_list) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
