text = "The quick brown fox jumps over the lazy dog"
text = text.lower()
alph = "abcdefghijklmnopqrstuvwxyz"
for i in alph:
    if i in text:
        print("True")
    else:
        print("False")
