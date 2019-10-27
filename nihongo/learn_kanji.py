import core
import sys


if __name__ == '__main__':
    core.clear_screen()

    search_tags = set(sys.argv[1].split(',')) if len(sys.argv) > 1 else set()
    words = core.read_words('nihongo/kanji.txt', search_tags)

    core.learn(words)
