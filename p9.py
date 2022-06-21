string = input('string: ')
find = input('motif: ')

start = 0
positions = []
while start < len(string):
    index = string.find(find, start, len(string)) 
    if index == -1:
        break
    truepos = index + 1
    positions.append(truepos) 
    start = truepos

print(*positions)
