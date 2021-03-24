

def heapify(list,n,i):
    print('calling heapify with {0} and {1}'.format(n,i))
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and list[i] < list[l]:
        largest = l 

    if r < n and list[largest] < list[r]:
        largest = r

    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        print('swapped {0} with {1}'.format(i,largest) )
        print(list, n, largest)
        heapify(list,n, largest)
                            
    
    

def heap_sort(list):
    print(list)
    n = len(list)
    for i in range((n//2)-1,-1,-1):
        #print(list, n, i)
        heapify(list,n,i)

    for i in range(n-1,0,-1):
        list[i], list[0] = list[0], list[i]
        print(list, i, '0')
        heapify(list,i,0)


