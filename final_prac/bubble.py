# Bubble sort
# You are given an unsorted list nums. 
# Your task is to sort this list with bubble sort. 
# However, it is too easy that asking you implement the algorithm. 
# In this question, you are ask to answer "the number of swap" during the bubble sort.
# Note that in our bubble sort, we want to get a increasing sorted list, and we also promise that the given list has no duplicate numbers.

def count_swap(number_list):
    n = len(number_list)
    count = 0
    for i in range(n): # 輪數
        print(i)
        for j in range(0, n - i - 1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
                # print(number_list)
                count += 1
    print(" ".join(str(num) for num in number_list))
    print(f"Swap: {count}")

    
# number_list = [1, 2, 3, 4, 5, 6, 7, 45, 12, 22]
number_list = list(map(int, input().split(" ")))
count_swap(number_list)


    