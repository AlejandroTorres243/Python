total = 870

if(total >= 500):

    discount = total * 0.05

    print('Discount: 5% OFF -'+str(discount))

else:
 
   discount = total * 0.10

   print('Discount: 10% OFF -'+str(discount))

total = total - discount

print('Total:'+ str(total))