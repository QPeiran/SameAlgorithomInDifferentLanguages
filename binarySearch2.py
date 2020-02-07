import math

Arr = [x for x in range(3,10)]

#print(len(Arr))

def binaryS(var_, arr_):
    k = math.ceil(len(arr_)/2)
    #print(k)
    if len(arr_)/2 < 1:
        return arr_
    else:
        if var_ < arr_[k]:
            start = arr_[0]
            print("up Start : %s" %start)# 
            end = arr_[k]
            print("up End : %s" %end)# 
            _arr = [x for x in range(start, end)]
            print(_arr)
            return binaryS(var_, _arr)
        else:
            start = arr_[k]
            print("down Start: %s"%(start))# 6
            end = arr_[len(arr_) - 1]
            print("down End: %s"%(end))# 10
            _arr = [x for x in range(start, end + 1)]
            print(_arr)
            return binaryS(var_, _arr)
        
print(binaryS(7, Arr))


#the θ(log n)
