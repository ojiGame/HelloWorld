print("何か入力してEnterキーを押してください")
input_line = input()
print("HelloWorld 2019/10/26")
print("あなたが入力したのは、" + str(input_line) + "で")
if str.isalpha(input_line):
    print("すべて文字ですね。")
elif str.isdecimal(input_line):
    print("すべて数字ですね。")
else:
    print("英数字混合、または特殊文字を含んでいますね。")