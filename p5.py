data = open('test.txt')
data = data.read()
data = data.replace('\n', '')
data = data.split('>')
new_data = []
for item in data:
    x = [item[:13], item[13:]]
    new_data.append(x)

new_data.pop(0)
print(new_data)

GCdata = []

for item in new_data:
    name = item[0]
    genome = item[1]
    GC = genome.count('G') + genome.count('C')
    GCpercent = (GC / len(genome)) * 100
    newitem = [name, GCpercent]
    GCdata.append(newitem)

maxitem = 0 
for item in GCdata: 
    if item[1] > maxitem: 
        maxitem = item[1]
        maxdata = item[0]

print(GCdata)
print(maxdata)
print(maxitem)