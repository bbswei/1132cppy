# Prime Number : A prime number (or a prime) is a natural number greater than 1
# that is not a product of two smaller natural numbers.
# 19 = 1 × 19 (Prime number)
# 25 = 5 × 5 (Not a Prime number)
# In this assignment, you have to find the largest prime number smaller or equal the given number.
# Input: 30 Output: Largest Prime Number: 29
# Input: 1 Output: 1 is not a prime number

# Input Format:
# The given number will be a positive number smaller than 1000, thus, it does not need to consider the negative input number or 0.
# Output Format:
# Please come up with the results in the following format: Largest Prime Number: {max_prime}


# 1. How to use loop algorithms to find the prime number is the basic task of the assignment.
# 2. Since the number might be a little bit large, thus, how to make the algorithm operate efficiently is important.
# 3. You can search for the prime number table on web to check whether you algorithm work.

# 檢查一個數是否為prime
def prime_detector(num):
    for i in range(2, num):
        remain = num % i 
        if remain == 0:
            return False
    return int(num)

# 檢查小於等於該數最大的prime
def max_prime(num):
    prime_list = []
    for j in range(1, num+1):
        prime_nums = prime_detector(j) 
        prime_list.append(prime_nums)
    return(max(prime_list))

num = int(input())

import time
start = time.time()

if num == 1:
    print('1 is not a prime number.')
else:
    print(f'Largest Prime Number: {max_prime(num)}')

end = time.time()
print(f'{end-start}seconds')




        









