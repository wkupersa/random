#!/bin/env python

'''
You are driving a vehicle that has capacity empty seats initially available 
for passengers. The vehicle only drives east (ie. it cannot turn around and 
drive west.) Given a list of trips, trip[i] = [num_passengers, start_location, 
end_location] contains information about the i-th trip: the number of passengers 
that must be picked up, and the locations to pick them up and drop them off.  
The locations are given as the number of kilometers due east from your vehicle's 
initial location.

Return true if and only if it is possible to pick up and drop off all passengers 
for all the given trips. 
'''

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        # need to sort the list of trips by thier starting point (second number)
        # return them east to west
        # sort the trips appropriately  
        people = 0
        pickedUp = [] # keep track of people already in car and when they leave
        trips.sort(key = lambda x: x[1])
        for trip in trips:
            current_location = trip[1]
            # Have people left. Let them out first
            temp_list = pickedUp.copy()
            for passengers in temp_list:
                if passengers[1] <= current_location:
                    people -= passengers[0]
                    pickedUp.remove(passengers)
                else:
                    break
            # put he new people in
            people += trip[0]
            if people > capacity:
                return False
            else:
                pickedUp.append([trip[0],trip[2]])
                pickedUp.sort(key = lambda x: x[1])
        return True





        # need to keep track of the # of passengers vs the capacity at any given location
        #      


test = Solution()
print(test.carPooling([[3,2,8],[4,4,6],[10,8,9]],11))
