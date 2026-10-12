text = "The quick brown fox jumps over the lazy dog"
text = text.lower()
alph = "abcdefghijklmnopqrstuvwxyz"
cnt = 0
for i in alph:
    if i in text:
        cnt += 1
if cnt == 26:
    print(True)
else:
    print(False)
