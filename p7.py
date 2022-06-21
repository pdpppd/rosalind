def mendel(k, m, n):
    total = k + m + n 
    two_rec = (n/total) * ((n-1)/(total-1))
    two_hetero = (m/total) * ((m-1)/(total-1))
    recandhetero = (m/total) * ((n)/(total-1)) + (n/total) * ((m)/(total-1))
    tot = two_hetero*1/4 + two_rec + recandhetero*1/2
    comp = 1 - tot
    return comp

print(round(mendel(18, 25, 24), 5))
