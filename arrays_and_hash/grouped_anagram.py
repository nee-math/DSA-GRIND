def group_anagram(s):
    store = {}

    for item in s:
        sort_item = "".join(sorted(item))
        if sort_item in store:
            store[sort_item].append(item)
        else:
            store[sort_item] = [item]

    result = []

    for _, v in store.items():
        result.append(v)

    return result


# Time: O(N * m log m)
# Space: O(N * M)


# act, cat, tac, atc -> act
if __name__ == '__main__':
    print(group_anagram(s=["act", "pots", "tops", "cat", "stop", "hat"]))
