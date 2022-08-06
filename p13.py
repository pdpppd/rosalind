from importfasta import *

def lsc(strings):
    test_str = strings[0]
    ref = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]
    lcs = ''
    for k in ref: 
        # print('substring ', k)
        true = []
        for index, item in enumerate(strings): 
            # print(index, item)
            if k in item: 
                true.append(True)
            else: 
                true.append(False)
        if all(x == True for x in true):
            if len(k) > len(lcs):
                lcs = k 
        # print('longest common string ', lcs)
    return lcs

def main(): 
    data = process_fasta('data/p13data.txt')
    genomelist = [data[key] for key in data]
    op = lsc(genomelist)
    print(op)

if __name__ == '__main__':
    main()

