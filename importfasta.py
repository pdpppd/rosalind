def process_fasta(path):
    raw = open(path)
    raw = raw.read()
    new = raw.split('\n')
    indices = []
    final = {}
    for index, item in enumerate(new): 
        if item[0] == '>':
            indices.append(index)
    for i, index in enumerate(indices): 
        if index == indices[-1]:
            a = ''.join(new[index + 1:])
        else:   
            a = ''.join(new[index + 1: indices[i + 1]])
        name = new[index]
        name = name[1:]
        final[name] = a
    return final