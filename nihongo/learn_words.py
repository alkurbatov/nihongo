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
   ('служащий банка', 'ぎんこういん [гинкооИн]'),
   ('врач', 'いしゃ [ишА]'),
   ('ученый', 'けんきゅうしゃ [кэнкЮЮша]'),
   ('университет', 'だいがく [дайгАку]'),
   ('больница', 'びょういん [бёёИн]'),
   ('кто', 'だれ [дарЭ]'),
   ('(кто)', 'どなた [донатА]'),
   ('~ лет', 'さい [саИ]'),
   ('да', 'はい [хАй]'),
   ('нет', 'いいえ [ииЭ]'),
   ('не так', 'ちがいます [чигаимАс]'),
   ('спасибо', 'ありがとう [аригатОО]'),
   ('(спасибо)', 'ありがとう ございます [аригатОО годзаимАс]'),
   ('доброе утро', 'おはよう [охаЁ]'),
   ('(доброе утро)', 'おはよう ございます [охаЁ годзаимАс]'),
   ('добрый день', 'こんにちは [коннИчива]'),
   ('добрый вечер', 'こんばんは [комбанвА]'),
   ('до свидания', 'さよなら [саЁнара]'),
   ('прошу вас, будьте добры', 'おねがいします [онэгАишимас]'),
   ('пожалуйста', 'ください [кудасАй]'),
   ('извините', 'すみません [сумимасЭн]'),
   ('хорошо', 'いいです [иидЭс]'),
   ('имя', 'なまえ [намаЭ]'),
   ('прошу', 'どうぞ [дООзо]'),
   ('это', 'こちら [кочирА]'),
   # Phrases
   ('сколько лет?', 'なんさい か？ [нансАи кА]'),
   ('(сколько лет?)', 'おいくつ か？ [ойкУцу кА]'),
   ('как вас зовут?', 'おなまえは [онамАэва]'),
   ('вам понятно?', 'わかります か [вакаримАс ка]'),
   ('приятно познакомиться', 'どうぞ よろしく (おねがいします) [дООзо ёрошикУ онэгаишимАс]'),
   ('ещё раз, пожалуйста', 'もういちど おねがいします [мооичидО онэгаишимАс]'),
   ('приехал из', 'きました [кимашитА]'),
   ('Извините, но ~ ?', 'しつれい [шицурЭи]'),
   ('~ не являюсь (конец отрицания в предложении)', 'じゃ ありません [джа аримасен]'),
]


if __name__ == '__main__':
    core.learn(words)
