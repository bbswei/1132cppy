##Ch5.3 Lists


# L = ['I did it all', 4, 'love']

# for i in range(len(L)):
    # print(L[i])


# Techs = ['MIT', 'Caltech']
# Ivys = ['Harvard', 'Yale', 'Brown']

# Univs = [Techs, Ivys]
# Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

# print('Univs =', Univs)
# print('Univs1 =', Univs1)
# print(Univs == Univs1)

# print(Univs == Univs1) #test value equality
# print(id(Univs) == id(Univs1)) #test object equality
# print('Id of Univs =', id(Univs))
# print('Id of Univs1 =', id(Univs1))

# print('Ids of Univs[0] and Univs[1]', id(Univs[0]), id(Univs[1]))
# print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1]))

# Topic: aliasing
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Techs.append('RPI')

for e in Univs:
    print('Univs contains', e)
    print(' which contains')
    for u in e:
        print('   ', u)

# ## Topic: list plus, extend, append
# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print('L3 =', L3)
# L1.extend(L2)
# print('L1 =', L1)
# L1.append(L2)
# print('L1 =',L1)

# ## Topic: Cloning
# def removeDups(L1, L2):
    # for e1 in L1:
        # if e1 in L2:
            # L1.remove(e1)

# # def removeDups(L1, L2):
    # # newL1 = list(L1)
    # # for e1 in newL1:
        # # if e1 in L2:
            # # L1.remove(e1)

# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# removeDups(L1, L2)
# print('L1 =', L1)
