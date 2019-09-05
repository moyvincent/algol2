
fullArray = [1, 1, 1, 1, 4]


def odd(x): #function to check if fullArray is odd or even
  return x % 2 != 0

def canBalance(fullArray):
    splitArray = []
    resultArray = []
    sumArray = sum(fullArray)
    splitArraysum = sum(splitArray)


    if not odd(sum(fullArray)):
        x = 0
        while splitArraysum != sumArray:
            splitArray.append(fullArray[x]) #add the first list item in fullArray to splitArray1
            
            fullArray.remove(fullArray[x])  #remove the first list item in fullArray

            sumArray = sum(sorted(fullArray))   #calculate the new value of sumArray
            splitArraysum = sum(splitArray) #calculate new value of splitArraysum 

        else:
            resultArray = [splitArray, fullArray]
    else:
        print("Cannot split")
        resultArray = -1
    return resultArray               



print('splitted array:',canBalance(fullArray))

