def func(x):
    return x + 1
    
def test_answer():
    assert func(3) == 4

    for x in range(len(num)):
        for i in range(k):
            num[x] = math.ceil(num[x] / 2)
    
    return sum(num)



    # Pick starting point 
    for Len in range(1,n + 1): 
          
        # Pick ending point 
        for i in range(n - Len + 1): 
              
            j = i + Len - 1
            sub = ''
            for k in range(i,j + 1):
                sub = sub+coins[k]
                
            if set(sub) == distLetter and len(sub) < lenOfSub:
                lenOfSub = len(sub)