class WordFilter:
    def __init__(self, ng_word):
        self.ng_word = ng_word

    def detect(self, word):
        if self.ng_word in word:
            return True
        else:
            return False


my_filter = WordFilter('アーセナル')

print(my_filter.detect('昨日のアーセナル戦はアツかった!'))
print(my_filter.detect('昨日のリバプール戦はアツかった!'))
