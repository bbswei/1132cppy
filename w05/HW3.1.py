def build_dict(words):
    one_word = words.split(",")
    # print(one_word) # ['apple', 'welcome', 'banana', 'cat', 'archive', 'once', 'australia', 'co', 'abc']
    dict = {}
    for word in one_word:
        if word[0].upper() not in dict.keys():
            dict[word[0].upper()] = [word]
        else:
            dict[word[0].upper()].append(word)
    # print(dict) {'A': ['apple', 'archive', 'australia', 'abc'], 'W': ['welcome'], 'B': ['banana'], 'C': ['cat', 'co'], 'O': ['once']}
    dict = {key: sorted(value) for key, value in sorted(dict.items())}
    return dict

    # sorted_items = sorted(dict.items())  # 按 key 進行排序
    # print(sorted_items)
    # new_dict = {}s
    # for key, value in sorted_items:
    #     new_dict[key] = sorted(value)  # 對每個 key 的 value（list）進行排序
    # dict = new_dict

def word_search(queries):
    # print(queries) # ['zoo', 'australia', 'cat', 'abc', 'co', 'banana']
    dict = build_dict(words)
    for voc in queries:
        # print(voc)
        if voc.strip():
            key = voc[0].upper()
            if key in dict and voc in dict[key]:
                print(key, dict[key].index(voc)+1)
            else:
                print('NOT FOUND')

words = input()
build_dict(words)

queries = []
while True:
    voc = input()
    if voc == '#':
        break
    queries.append(voc)
word_search(queries)