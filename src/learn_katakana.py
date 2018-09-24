import random


row_a = [
    ('а', 'ア'),
    ('и', 'イ'),
    ('у', 'ウ'),
    ('э', 'エ'),
    ('о', 'オ')
]
row_ka = [
    ('ка', 'カ'),
    ('ки', 'キ'),
    ('ку', 'ク'),
    ('кэ', 'ケ'),
    ('ко', 'コ')
]
row_sa = [
    ('са', 'サ'),
    ('ши', 'シ'),
    ('су', 'ス'),
    ('сэ', 'セ'),
    ('со', 'ソ')
]
row_ta = [
    ('та', 'タ'),
    ('чи', 'チ'),
    ('цу', 'ツ'),
    ('тэ', 'テ'),
    ('то', 'ト')
]
row_na = [
    ('на', 'ナ'),
    ('ни', 'ニ'),
    ('ну', 'ヌ'),
    ('нэ', 'ネ'),
    ('но', 'ノ')
]


kana = row_a + row_ka + row_sa + row_ta + row_na


def learn():
    try:
        while kana:
            syllable = random.choice(kana)
            kana.remove(syllable)

            print(syllable[0])
            input()

            print(syllable[1])
            input()

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    learn()
