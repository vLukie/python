#冒泡排序

def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            return
    
  
