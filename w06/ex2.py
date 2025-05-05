## Week 6 - Ex2
from itertools import permutations

def checker(ans, digits):
    A = 0
    B = 0

    # 找幾個 A
    for i in range(4):  
        if ans[i] == digits[i]:
            A += 1

    # 找幾個 B
    for g in digits:
        if g in ans:
            B += 1

    B = B - A

    return A, B

def game_cheater():
    candidate = list(permutations(range(10), 4))

    while True:
        guess = input()
        if guess == "q":
            break

        digits = list(map(int, guess.split("->")[0].strip().split()))
        x = int(guess.split("A")[0].split("->")[1].strip()) # A
        y = int(guess.split("A")[1].split("B")[0].strip()) # B

        new_candidate = [] 
        for ans in candidate:
            result = checker(ans, digits)
            if result == (x, y):
                new_candidate.append(ans)

        candidate = new_candidate
        # print(f"After input '{guess}', remaining candidates: {len(candidate)}")
        # print(digits)
    if candidate:
        print('Possible codes:')
        for pos_ans in sorted(candidate):
            print(" ".join(map(str, pos_ans)))
    else:
        print('No valid codes')

if __name__ == "__main__":
    game_cheater()


# candidate = [ans for ans in candidate if checker(and, digits) == (x, y)]


