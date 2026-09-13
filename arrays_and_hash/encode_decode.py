def encode(strs):
    result = ""
    for s in strs:
        size = len(s)
        result += f"{size}#{s}"
    return result


def decode(s):
    result = []
    length = len(s)
    i = 0
    while i < length:
        j = i
        while s[j] != "#":
            j += 1

        size = int(s[i: j])
        j += 1
        word = s[j: j + size]
        result.append(word)
        i = j + size
    return result


if __name__ == '__main__':
    strs = ["neet", "code", "love", "you"]
    encoded = encode(strs)
    print(encoded)
    print(decode(encoded))  # expected: ["neet", "code", "love", "you"]

    strs = ["we", "say", ":", "yes", ""]
    encoded = encode(strs)
    print(encoded)
    print(decode(encoded))  # expected: ["we", "say", ":", "yes", ""]
