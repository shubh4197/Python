l = ['a', 'b', 'c', 'd', 'e', 'f']
print(len(l))
print(max(l))
print(min(l))
l.append('g')
print(l)
l2 = ['h', 'i', 'j']
l.extend(l2)
print(l)
l.insert(2, 'z')
print(l)
l.pop(2)
l.pop()
print(l)
l.sort()
print(l)
