st = { 1, 2, 4, 6, 8, 9, 12, 16, 15}

new = set([2,4,6,8,10,12,14,16,18])

odd = set([1,9,15])

st.discard(odd)

st.clear()

st.update(new)

print(st)