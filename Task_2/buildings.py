buildings=['A','B','C','D','E','F','G','H','I','J']

# implementing the push operation
buildings.append('K')
print(buildings)

# implementing the pop operation
buildings.pop()
print(buildings)

# implementing the peek operations
x=buildings[-1]
print(x)

# implementing the is_empty operation
if len(buildings) == 0:
    print('Stack is empty')
else:
    print('stack is not empty')