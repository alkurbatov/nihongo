import core
import sys


def parse_args(args):
    if not len(args):
        return set()

    if ',' in args[0]:
        return set(args[0].split(','))

    if '-' in args[0]:
        interval = args[0].split('-', maxsplit=1)

        tags = set()
        start = int(interval[0])
        while start <= int(interval[1]):
            tags.add(str(start))
            start += 10

        return tags

    return set()


if __name__ == '__main__':
    core.clear_screen()

    search_tags = parse_args(sys.argv[1:])
    words = core.read_words('nihongo/kanji.txt', search_tags)

    core.learn(words)
