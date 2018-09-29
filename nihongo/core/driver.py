import random


def learn(data):
    try:
        while data:
            pair = random.choice(data)
            data.remove(pair)

            print(pair[0])
            input()

            print(pair[1])
            input()

    except KeyboardInterrupt:
        pass
