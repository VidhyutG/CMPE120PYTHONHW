#program to swap first and last item in a list
def swap_last_item(newList):
 ''' Accepts a list and interchanges the first and last element in the list'''
 #swapping
 newList[0], newList[-1] = newList[-1], newList[0]
 return newList
