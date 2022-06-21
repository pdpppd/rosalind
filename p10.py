
import numpy as np 

def process_fasta(path):
    raw = open(path)
    raw = raw.read()
    rawsplit = raw.split('\n')
    fasta = list(map(lambda x: x[1:] if x[0] == '>' else x, rawsplit))
    final = {}
    for i in range(0, len(fasta), 2):
        x = fasta[i+1]
        x = list(x)
        final[fasta[i]] = x
    return final

def creatematrix(data_dict):
    array = []
    for key in data_dict:
        array.append(data_dict[key])
    return array

def createprofile(dnamatrix):
    matrix = np.array(dnamatrix)
    matrix = matrix.transpose()
    profile = []
    for column in matrix: 
        column = list(column)
        A = column.count('A')
        C = column.count('C')
        G = column.count('G')
        T = column.count('T')
        profile.append([A, C, G, T])
    profile = np.array(profile)
    profile_transposed = profile.transpose()
    return profile_transposed, profile 

def createconsensus(profile):
    consensus = ''
    correlation = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    for item in profile:
        i = list(item)
        maxind = i.index(max(i))
        base = correlation[maxind]
        consensus += base
    return consensus

data = process_fasta('sample.txt')
print(data)
print('------')

matrix = creatematrix(data)
print(matrix)
print('------')

profile_t, profile = createprofile(matrix)
print(profile)
print('------')

consensus = createconsensus(profile)
print(consensus)
print('A:', profile_t[0])
print('C:', profile_t[1])
print('G:', profile_t[2])
print('T:', profile_t[3])
