## Week 6 - Ex2
'''
Merge groups from connections.
Initialization: Every city is in its own group.
For each connection:
Merge two groups that the cities in into one group.
Update for other cities in the same group.

>>> 6
>>> City4 City2
>>> City3 City2
>>> City6 City5
>>> q
'''

def main():
    num = int(input())
    city = [('City' + str(i)) for i in range(1, num+1)]
    city_group = dict(zip(range(1, num+1), city)) # initial_group
    # print(city)
    # print(city_group)
    while True:
        connection = input()
        if connection == 'q':
            break
        
        info = list(connection.split(" "))
        print(info)

            


    # while True:
    #     line = input().strip()
    #     if line == 'q':
    #         break
    #     try:
    #         num = int(line)
    #         cities = [i for i in range(num)]
    #     except:

    #         print(cities)


        # for idx, info in line:
        #     num_of_cities = int(line)
        # for line in range(num_of_cities):
        #     connection = line.strip()
        #     print(connection)


main()


