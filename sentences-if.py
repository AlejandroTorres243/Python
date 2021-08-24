lst = ['Python', 'C', 'C++', 'Java']
print(lst)

if'Python' not in lst:
  lst.append('Python')
elif 'Java' not in lst:
  lst.append('Java')
else:
  lst.append('JS')

print(lst)