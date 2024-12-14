import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, '')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        results = {}
        for file_name, words in all_words.items():
            try:
                results[file_name] = words.index(word) + 1
            except ValueError:
                results[file_name] = -1
        return results

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        results = {}
        for file_name, words in all_words.items():
            results[file_name] = words.count(word)
        return results

finder = WordsFinder('test_file.txt')

print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
