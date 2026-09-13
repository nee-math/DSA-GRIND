def encode(strs):
    pass


def decode(s):
    pass


if __name__ == '__main__':
    strs = ["neet", "code", "love", "you"]
    encoded = encode(strs)
    print(encoded)
    print(decode(encoded))  # expected: ["neet", "code", "love", "you"]

    strs = ["we", "say", ":", "yes", ""]
    encoded = encode(strs)
    print(encoded)
    print(decode(encoded))  # expected: ["we", "say", ":", "yes", ""]
