import random


def read_words(filepath, keyword=None):
    words = []

    with open(filepath) as f:
        for i in f.readlines():
            if i.startswith('#'):
                continue

            record = i.strip().split('|')
            if not keyword:
                words.append(record)
                continue

            if len(record) > 2:
                tags = record[2].split(',')
            else:
                tags = ()

            if keyword not in tags:
                continue

            words.append(record)

    return words


def learn(data):
    try:
        while data:
            pair = random.choice(data)
            data.remove(pair)

            if len(pair) < 2:
                print('Unexpected format: {}'.format(pair))
                return

            print(pair[0])
            input()

            print('{}\n'.format(pair[1]))

    except KeyboardInterrupt:
        pass
