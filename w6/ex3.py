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
    city_name = [('City' + str(i)) for i in range(1, num+1)] 
    city_group = dict(zip(city_name, range(1, num+1), )) # initial_group
    # print(city_group)
    # >>> {'City1': 1, 'City2': 2, 'City3': 3, 'City4': 4, 'City5': 5, 'City6': 6, 'City7': 7, 'City8': 8, 'City9': 9, 'City10': 10}

    while True:
        connection = input()
        if connection == 'q':
            break

        a, b = connection.split(" ")
        group1 = city_group[a]
        group2 = city_group[b]

        new_group = num + 1
        num += 1
        for city, group in city_group.items():
            if group == group1 or group == group2:
                city_group[city] = new_group
    # print(city_group)
    return len(set(city_group.values()))


if __name__ == '__main__':
    print(main())


