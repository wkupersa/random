#!/bin/env python

from makelist import make_list
from mergesort import merge_sort
from heapsort import heap_sort


if __name__ == "__main__":
    mylist = make_list(10)
    merge_list = mylist.copy()
    heap_list = mylist.copy()
    print(mylist)
    '''
    merge_sort(merge_list)
    print(merge_list)
    print(mylist)
    '''
    heap_list= [5,4,3,2,1]
    heap_sort(heap_list)
    print(heap_list)