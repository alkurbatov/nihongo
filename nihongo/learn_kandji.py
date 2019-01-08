import core
import sys


if __name__ == '__main__':
    search_tags = sys.argv[1].split(',') if len(sys.argv) > 1 else None
    words = core.read_words('nihongo/kandji300.txt', set(search_tags))

    core.learn(words)
