buildings=['plaza 1','plaza 2','plaza 3','plaza 4','plaza 5','plaza 6','plaza 7','plaza 8','plaza 9','plaza 10']

# implementing the push
buildings.append('plaza 11')

print(buildings)

# implementing the pop
buildings.pop()
print(buildings)

# implementing the peek
x=buildings[-1]
print(x)

# implenting the is_empty
buildings=[]
if len(buildings)==0:
    print('The Stack is empty')