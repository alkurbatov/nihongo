import sys
import core


if __name__ == '__main__':
    words = core.read_words('nihongo/lesson{}.txt'.format(sys.argv[1]))
    core.learn(words)
