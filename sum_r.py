def sum_r(*n):
   sm = 0
   d = []
   for num in n:
       sm += num
       Num = str(num).split('.')
       d.append(len(Num[1]))
   min_d = min (d)
   return round(sm, min_d)

print(sum_r(12.56,12.848,11.1567,90.007))