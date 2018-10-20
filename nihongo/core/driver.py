import random


def read_words(filepath):
    words = []

    with open(filepath) as f:
        for i in f.readlines():
            if i.startswith('#'):
                continue

            words.append(i.strip().split('|'))

    return words


def learn(data):
    try:
        while data:
            pair = random.choice(data)
            data.remove(pair)

            print(pair[0])
            input()

            print('{}\n'.format(pair[1]))

    except KeyboardInterrupt:
        pass
