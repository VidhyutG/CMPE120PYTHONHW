#program to swap first and last item in a list
def swap_last_item(newList):
 ''' Accepts a list and interchanges the first and last element in the list'''
 #length of list is assigned to size for easy index access
 size = len(newList) 
 temp = newList[0]
 newList[0] = newList[size-1]
 newlist[size-1] = temp
  
 return newList
