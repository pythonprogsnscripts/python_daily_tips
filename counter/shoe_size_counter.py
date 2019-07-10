from collections import Counter
n = int(input())
shoe_size = Counter(list(map(int,input().split())))

def calculate_total_price(shoe_size):
    customers = int(input())
    total_price = 0
    for _ in range(customers):
        size, price = map(int,input().split())
        if shoe_size[size] > 0:
            total_price += price
            shoe_size[size] -= 1
    return total_price

print(calculate_total_price(shoe_size))