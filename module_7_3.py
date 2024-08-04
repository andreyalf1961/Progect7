class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for item in self.file_names:
            with open(item, 'r', encoding='utf-8') as file:
                text_ = file.read().lower()
                puncts = [',', '.', '=', '!', '?', ';', ':', ' -']
                for p in puncts:
                    if p in text_:
                        text_ = text_.replace(p, '')
                text_ = text_.split()
                all_words[item] = text_
        return all_words

    def find(self, word):
        word_position = {}
        for key, value in self.get_all_words().items():
            for w in value:
                if word.lower() == w:
                    word_position[key] = value.index(w) + 1
                    break
        return word_position

    def count(self, word):
        quantity_of_words = {}
        for key, value in self.get_all_words().items():
            q = 0
            for i in value:
                if word.lower() == i:
                    q += 1
            quantity_of_words[key] = q
        return quantity_of_words


finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())
print('Первое найденное слово TEXT:', finder1.find('TEXT'))
print('Количество слова TEXT:', finder1.count('teXT'))

finder2 = WordsFinder('Walt_Whitman.txt', 'Kipling.txt', 'Mother_Goose.txt')
print(finder2.get_all_words())
print('Первое найденное слово the:', finder2.find('the'))
print('Количество слова the:', finder2.count('the'))
