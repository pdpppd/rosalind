
def lsc(strings):
    test_str = strings[0]
    ref = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]
    cs = []
    for k in ref: 
        for index, item in enumerate(strings): 
            if k in item: 
                strings[index] = True
    return strings

print(lsc(['GATTACA', 'TAGACCA', 'ATACA']))