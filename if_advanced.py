total = 760

discount = 0

promo_item_bought = True

if(total <= 500):

    discount = total * 0.05

elif((total >= 500) and (promo_item_bought)):

    discount = total * 0.10

total = total - discount

print(total)