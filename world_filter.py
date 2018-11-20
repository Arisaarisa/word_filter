# my_filter = WordFilter("アーセナル")
#
# # NGワードが含まれている場合
# my_filter.detect("昨日のアーセナルの試合アツかった！") # Trueを返す ※出力されるわけではありません！
#
# # NGワードが含まれていない場合
# my_filter.detect("昨日のリバプールの試合アツかった！") # Falseを返す ※出力されるわけではありません！

rtn = "アセナール" in "昨日のアセナールの試合はアツかった!"
print(rtn)


# my_filter = WordFilter("アセナール")
#
# if my_filter == WordFilter:
