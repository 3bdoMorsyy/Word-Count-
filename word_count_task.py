import nltk


def Map(text):
    map = []
    punc = """()[]}{,./\`!@#$%^&*_+-=|"'"""
    words = nltk.word_tokenize(text)
    for word in words:
        if word not in punc:
            map.append((word, 1))
    # print(f"This is Map Function Output {map}")
    return map


def Shuffle(text):
    keys = []
    Key_value = []
    map_out = Map(text)
    for i, j in map_out:
        keys.append(i)
    for key in set(keys):
        temp = key
        for _ in range(keys.count(key)):
            temp += " ,1"
        Key_value.append(f"({temp})")
    # print(f"This is Reduce Function Output {Key_value}")
    return Key_value



def MapReduce(text):
    final = []
    text = Shuffle(text)
    for word in text:
        occurnces = word.count(",1")
        word = word.replace(" ,1", "").replace("(", "").replace(")", "")
        final.append((word, occurnces))
    # print(f"This is MapReduce Final Output {final}")
    return final
