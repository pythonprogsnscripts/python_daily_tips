'''
TODO
'''
n = int(input())
shoe_size = list(map(int,input().split()))

def total_price(shoe_size):
    '''
    This function takes the input of shoe sizes and the price of the each
    and calculates the total price. If the shoe size is not available in the
    list, the entry is discarded
    '''
    customers = int(input())
    total_price = 0
    for i in range(customers):
        size,price = map(int,input().split())
        if size in shoe_size:
            total_price += price
            shoe_size.remove(size)
    return total_price

print(total_price(shoe_size))
