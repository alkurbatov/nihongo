import core


words = [
    ('я', 'わたし [ватащИ]'),
    ('ты (вы)', 'あなた [анатА]'),
    ('вон тот', 'あの [анО]'),
    ('он, она, вон тот человек', 'あのひと [анО хитО]'),
    ('(он, она, вон тот человек)', 'あのかた [анО катА]'),
    ('~ господин, госпожа', 'さん [сан]'),
    ('~ ребенок', 'ちゃん [чан]'),
    ('~ человек', 'じん [дзин]'),
    ('учитель (о ком-то)', 'せんせい [сенсЭ]'),
    ('учитель (о себе)', 'きょうし [кёёшИ]'),
    ('студент', 'がくせい [гакусЭ]'),
    ('служащий фирмы', 'かいしゃいん [кайшаИн]'),
    ('~ служащий фирмы', 'しゃいん [шаИн]'),
    ('банк', 'ぎんこう [гинкО]'),
    ('служащий банка', 'ぎんこういん [гинкооИн]'),
    ('врач', 'いしゃ [ишА]'),
    ('ученый', 'けんきゅうしゃ [кэнкЮЮша]'),
    ('университет', 'だいがく [дайгАку]'),
    ('больница', 'びょういん [бёёИн]'),
    ('кто', 'だれ [дарЭ]'),
    ('(кто)', 'どなた [донатА]'),
    ('~ лет', 'さい [сай]'),
    ('да', 'はい [хАй]'),
    ('нет', 'いいえ [ииЭ]'),
    ('спасибо', 'ありがとう [аригатОО]'),
    ('(спасибо)', 'ありがとう ございます [аригатОО годзаимАс]'),
    ('доброе утро', 'おはよう [охаЁ]'),
    ('(доброе утро)', 'おはよう ございます [охаЁ годзаимАс]'),
    ('добрый день', 'こんにちは [коннИчива]'),
    ('добрый вечер', 'こんばんは [комбанвА]'),
    ('до свидания', 'さよなら [саЁнара]'),
    ('разрешите представиться', 'はじめまして [хадзимэмашИтэ]'),
    ('прошу вас, будьте добры', 'おねがいします [онэгАишимас]'),
    ('пожалуйста', 'ください [кудасАй]'),
    ('извините', 'すみません [сумимасЭн]'),
    ('хорошо', 'いいです [иидЭс]'),
    ('имя', 'なまえ [намаЭ]'),
    ('пожалуйста (предложение кому-либо чего-либо)', 'どうぞ [дООзо]'),
    ('это', 'こちら [кочирА]'),
    ('домашнее задание', 'しゅくだい [шюкудаИ]'),
    ('работа', 'しごと [шиготО]'),
    ('император', 'てんのう [теннОО]'),
    ('певец', 'かしゅ [кашЮ]'),
    ('король', 'おうさま [оосамА]'),
    ('актер', 'はいゆう [хайЮЮ]'),
    ('художник', 'がか [гакА]'),
    ('писатель', 'さっか [саккА]'),
    ('Китай', 'チューゴク [чююгокУ]'),
    ('Англия', 'イギリス [игирисУ]'),
    # Phrases
    ('сколько лет?', 'なんさい ですか？ [нансАй дэскА]'),
    ('(сколько лет?)', 'おいくつ ですか？ [оЙкуцу дэскА]'),
    ('как вас зовут?', 'おなまえは [онамАэва]'),
    ('где работаете?', 'あしごとは [ашиготОва]'),
    ('из какой вы страны?', 'なにじん ですか [наниджИн дэска]'),
    ('вам понятно?', 'わかります か [вакаримАс ка]'),
    ('не понятно / не знаю', 'わかりますえん [вакаримАсен]'),
    ('приятно познакомиться', 'どうぞ よろしく (おねがいします) [дООзо ёрошикУ (онэгаишимАс)]'),
    ('ещё раз, пожалуйста', 'もういちど おねがいします [мооичидО онэгаишимАс]'),
    ('приехал из', 'きました [кимашитА]'),
    ('Извините, но ~ ?', 'しつれいですが [шицурЭидэсга]'),
    ('~ не являюсь (конец отрицания в предложении)', 'じゃ ありません [джа аримасен]'),
    ('вам спасибо, взаимно (в ответ на чью-то благодарность)', 'こちらこそ [кочиракосО]'),
    ('пожалуйста (в ответ на чью-то благодарность)', 'どういたしまして [дооиташимашитЭ]'),
    ('мы встречаемся впервые (произносится при первом знакомстве)', 'はじめまして [хадзимемашитЕ]')
]


if __name__ == '__main__':
    core.learn(words)
