# LISTS LEARNING 
simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
del(simple_list[0])
print(simple_list)

# DICTIONARIES LEARNING

d = {'name': 'Max'}
print(d.items())
for k, v in d.items():
    print(k, v)
del[d['name']]

# TUPLES LEARNING 

tup = (1,2,3)
print(tup.index(1))
# del(tup[0]) ## does not work, tuples are immutable!!

# SETS LEARNING 

s = {'Max', 'Anna', 'Max'}
# del(s['Max']) ## does not work, use discard()
st = set()
st = s.copy()
st.add('Bob')
print(st)
print(s)

