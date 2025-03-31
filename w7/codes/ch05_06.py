##Ch5.6

monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
        1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print('The third month is ' + monthNumbers[3])
dist = monthNumbers['Apr'] - monthNumbers['Jan']
print('Apr and Jan are', dist, 'months apart')


# def keySearch(L, k):
    # for elem in L:
        # if elem[0] == k:
            # return elem[1]
    # return None

# L = [['a', 1], ['b', 2]]
# print(keySearch(L, 'a'))


# monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
        # 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
# keys = []
# for e in monthNumbers:
    # keys.append(str(e))
# print(keys)
# keys.sort()
# print(keys)


# birthStones = {'Jan':'Garnet', 'Feb':'Amethysgt', 'Mar':'Acquamarine',
               # 'Apr':'Diamond', 'May':'Emerald'}
# months = birthStones.keys()
# print(months)
# birthStones['June'] = 'Pearl'
# print(months)


## More examples
# def displatDict(dictOfElements) :
    # for key , value in dictOfElements.items():
        # print(key, " : ", value)

## Convert List items as keys in dictionary with enumerated value
# listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
# dictOfWords = {i : listOfStr[i] for i in range(0, len(listOfStr))}
# displatDict(dictOfWords)

## Convert two lists to a dictionary
# listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
# listOfInt = [56, 23, 43, 97, 43, 102]
# dictOfWords = dict(zip(listOfStr, listOfInt))
# displatDict(dictOfWords)

## Convert a list of tuples to dictionary
# listofTuples = [("Riti" , 11), ("Aadi" , 12), ("Sam" , 13),("John" , 22),("Lucy" , 90)]
# studentsDict = dict(listofTuples)
# displatDict(studentsDict)
