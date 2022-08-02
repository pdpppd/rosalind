from difflib import SequenceMatcher

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
        # print(a)
    # print('final ', final)
    return final

# test AAATAAA
#      AAATCCC
def matchie(a, b):
    cnt = 0
    bruh = True
    match = False
    while True: 
        if a[:cnt] == b[-cnt:]:
            print('yay')
            print(a[:cnt])
            print(b[-cnt:])
            match = True
        elif a[-cnt:] == b[:cnt]:
            print('yay')
            print(a[-cnt:])
            print(b[:cnt])
            match = True
        else:
            break
        cnt += 1

    if match == True: 
        return True
    else: 
        return False
        # if cnt == len(a):
        #     return False
        #     break
        

def main(): 
    bro = process_fasta('data/p12test.txt')
    print(matchie(bro['Rosalind_0498'], bro['Rosalind_2391']))


if __name__ == '__main__':
    main()
