import random


row_a = [
    ('а', 'ア'),
    ('и', 'イ'),
    ('у', 'ウ'),
    ('э', 'エ'),
    ('о', 'オ'),
]
row_ka = [
    ('ка', 'カ'),
    ('ки', 'キ'),
    ('ку', 'ク'),
    ('кэ', 'ケ'),
    ('ко', 'コ'),
]
row_sa = [
    ('са', 'サ'),
    ('ши', 'シ'),
    ('су', 'ス'),
    ('сэ', 'セ'),
    ('со', 'ソ'),
]
row_ta = [
    ('та', 'タ'),
    ('чи', 'チ'),
    ('цу', 'ツ'),
    ('тэ', 'テ'),
    ('то', 'ト'),
]
row_na = [
    ('на', 'ナ'),
    ('ни', 'ニ'),
    ('ну', 'ヌ'),
    ('нэ', 'ネ'),
    ('но', 'ノ'),
]
row_ha = [
    ('ха', 'ハ'),
    ('хи', 'ヒ'),
    ('фу', 'フ'),
    ('хэ', 'ヘ'),
    ('хо', 'ホ'),
]
row_ma = [
    ('ма', 'マ'),
    ('ми', 'ミ'),
    ('му', 'ム'),
    ('мэ', 'メ'),
    ('мо', 'モ'),
]
row_ya = [
    ('я', 'ヤ'),
    ('ю', 'ユ'),
    ('ё', 'ヨ'),
]
row_ra = [
    ('ра', 'ラ'),
    ('ри', 'リ'),
    ('ру', 'ル'),
    ('рэ', 'レ'),
    ('ро', 'ロ'),
]
row_wa = [
    ('ва', 'ワ'),
    ('во', 'ヲ'),
]
row_n = [
    ('н', 'ン'),
]


kana = row_a + row_ka + row_sa + row_ta + row_na + row_ha + row_ma + \
       row_ya + row_ra + row_wa + row_n


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
