# Euler Problem #1 - Multiples of 3 or 5
# v1.0.0 - 25MAR2022
#
# Description:
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# 0,3,5,6,9,10,12,15,18,20,21,24,25,27,30,33,35,36,39,40
# 3,2,1,3,1 ,2 ,3 ,
# 3 ,2 ,1 ,3 ,1 ,2 ,3 ,
# 3 ,2 ,1 ,3 ,1



def SumOfMultiples():
    offsetList = [3, 2, 1, 3, 1, 2, 3]
    sumOfAllMultiples = 0
    valueToAdd = 0
    offsetIndex = 0
    
    while(valueToAdd < 999):
        valueToAdd += offsetList[offsetIndex]
        #print('ValuetoAdd: ' + str(valueToAdd))
        sumOfAllMultiples += valueToAdd
        #print('SumOfAllMultiples: ' + str(sumOfAllMultiples))
        offsetIndex += 1
        if(offsetIndex > 6):
            offsetIndex = 0
    
    return sumOfAllMultiples
 
print(SumOfMultiples())
 
