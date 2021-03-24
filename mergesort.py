#!/bin/env python


def merge_sort(mylist):

    if len(mylist) > 1:
        middle = int(len(mylist)/2)
        L = mylist[:middle]
        R = mylist[middle:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                mylist[k] = L[i]
                i+=1
            else:
                mylist[k] = R[j]
                j+=1
            k+=1
        
        while i < len(L):
            mylist[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            mylist[k] = R[j]
            j+=1
            k+=1
    return mylist

a = merge_sort([1,6,3,4,3,9,23,2])
print(a)