import platform
import random
import subprocess


def clear_screen():
    if platform.system().lower() == 'windows':
        return subprocess.call('cls')

    return subprocess.call('clear')

def read_words(filepath, search_tags=None):
    words = []

    with open(filepath) as f:
        for i in f.readlines():
            if i.startswith('#'):
                continue

            record = i.strip().split('|')
            if not search_tags:
                words.append(record)
                continue

            if len(record) > 2:
                tags = set(record[2].split(','))
            else:
                tags = set()

            if not search_tags & tags:
                continue

            words.append(record)

    return words


def learn(data):
    try:
        total = len(data)
        shown = 0

        while data:
            shown += 1
            pair = random.choice(data)
            data.remove(pair)

            if len(pair) < 2:
                print('Unexpected format: {}'.format(pair))
                return

            print('({}\{}) {}?'.format(shown, total, pair[0]))
            input()

            print('{}\n\n'.format(pair[1]))

    except KeyboardInterrupt:
        pass
