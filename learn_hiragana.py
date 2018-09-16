import random


row_a  = [('а', 'あ'), ('и', 'い'), ('у', 'う'), ('э', 'え'), ('о', 'お')]
row_ka = [('ка', 'か'), ('ки', 'き'), ('ку', 'く'), ('кэ', 'け'), ('ко', 'こ')]
row_ta = [('та', 'た'), ('чи', 'ち'), ('цу', 'つ'), ('тэ', 'て'), ('то', 'と')]
row_sa = [('са', 'さ'), ('ши', 'し'), ('су', 'す'), ('сэ', 'せ'), ('со', 'そ')]
row_na = [('на', 'な'), ('ни', 'に'), ('ну', 'ぬ'), ('нэ', 'ね'), ('но', 'の')]
row_ha = [('ха', 'は'), ('хи', 'ひ'), ('фу', 'ふ'), ('хэ', 'へ'), ('хо', 'ほ')]
row_ma = [('ма', 'ま'), ('ми', 'み'), ('му', 'む'), ('мэ', 'め'), ('мо', 'も')]
row_ya = [('я', 'や'), ('ю', 'ゆ'), ('ё', 'よ')]
row_ra = [('ра', 'ら'), ('ри', 'り'), ('ру', 'る'), ('рэ', 'れ'), ('ро', 'ろ')]
row_va = [('ва', 'わ'), ('во', 'を')]
row_n  = [('н', 'ん')]

kana = row_a + row_ka + row_ta + row_sa + row_na + row_ha + row_ma + \
       row_ya + row_ra + row_va + row_n


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

