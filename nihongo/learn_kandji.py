import core


if __name__ == '__main__':
    words = core.read_words('nihongo/kandji300.txt')
    core.learn(words)
