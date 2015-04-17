shopping_list = ["banana", "laranja", "maca"]
 
stock = {
    "banana": 6,
    "maca": 0,
    "laranja": 32,
    "pera": 15
}
   
prices = {
    "banana": 4,
    "maca": 2,
    "laranja": 1.5,
    "pera": 3
}
 
def compute_bill(food):
    total = 0
    for p in shopping_list:
        if stock[p] > 0:
            total += prices[p]
            stock[p] -= 1
    return total