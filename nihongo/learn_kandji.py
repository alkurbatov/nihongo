import core
import sys


if __name__ == '__main__':
    tag = sys.argv[1] if len(sys.argv) > 1 else None
    words = core.read_words('nihongo/kandji300.txt', tag)

    core.learn(words)
