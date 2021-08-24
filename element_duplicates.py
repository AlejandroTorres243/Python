def remove_dup(l):
    unique = set(l)
    new_list = list(unique)
    new_list.sort()
    return new_list

lst = [12,12,44,54,54,1,1,8,3,5,5,91,100]
print(lst)
print(remove_dup(lst))