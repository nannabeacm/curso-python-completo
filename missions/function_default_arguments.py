def order_hot_dog(quantity=1):
    suffix = "hot-dog" if quantity == 1 else "hot-dogs"
    print(f"Ordering {quantity} {suffix}.")

order_hot_dog()   # Uses default (1)
order_hot_dog(5)  # Uses 5