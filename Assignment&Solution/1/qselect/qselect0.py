# CS519_HW1
# Name: Hongyan Yi
# ONID: yih

import random

def qselect(k,list):
    if not 0 < k <= len(list):
        return ValueError("Not enough elements in the list")
		
    while True:
        pivot = random.choice(list)
	#print pivot
        pcount = 0
        left = []
        right = []
        for elem  in list:
            if elem < pivot:
                left.append(elem)
            elif elem > pivot:
                right.append(elem)
            else:
                pcount +=1		# good way to handle duplicates
        #print left
	#print right
	if k <= len(left):		
            list = left
        elif k <= len(left) + pcount:
            return pivot
        else:
            list = right
            k = k-(len(left)+pcount)

    