## HW05

def checker(block):
    """ 
    計算有多少不連通的'#'(dirty zone) 
    """
    n = len(block)
    cleaned = [[False] * n for _ in range(n)] # 紀錄哪些地方清理過
    # print(cleaned) [[False, False, False], [False, False, False], [False, False, False]]

    def clean(r, c): # (row,col)
        if r < 0 or r >= n or c < 0 or c >= n:
            return 
        if cleaned[r][c] or block[r][c] != '#': 
            return # 乾淨或已處理
        cleaned[r][c] = True
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            clean(r+dr, c+dc)

    count = 0
    for i in range(n):
        for j in range(n):
            if block[i][j] == '#' and not cleaned[i][j]:
                count += 1
                clean(i, j)
    return count
    # count = 0
    # if len(block) <= 1 :
    #     return 0
    # elif block[0][-1] == '.' and block[1][0] == '.':
    #     if '#' in block[0] and block[1]:
    #         count += 1
    # return count  + checker(block[1:])

def dirt_detector():
    tiles_num = int(input())
    # print(tiles_num)
    all = []
    for _ in range(tiles_num):
        block_size = int(input())
        dirty_info = []

        for line in range(block_size):
            line = str(input())
            dirty_info.append(line)
        # print(dirty_info)
        all.append(dirty_info)
    # print(all)

    for block in all: # 遍歷所有list
        # print(block)
        print(checker(block)) # 對所有list進行檢查並回傳數量



if __name__ == "__main__":
    dirt_detector()













