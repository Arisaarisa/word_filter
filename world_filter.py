# class WordFilter:
#     def __int__(self, ng_word):
#         self.ng_word = ng_word
#
#     def detect(self):
#         return self.ng_word
#
#         print(self.detect())
#
#
# if __name__ == "__main__":
#     my_filter = WordFilter("assena-ru")
#     my_filter.detect()
class WordFilter:
    def __init__(self, ng_word):
        self.ng_word = ng_word

    def detect(self):
        if self.ng_word == "アーセナル":
            print(True)
            return True
        else:
            print(False)
            return False

if __name__ == "__main__":
    my_filter = WordFilter("アーセナル")
    my_filter.detect()

print("アーセナル")

print("リバプール")
