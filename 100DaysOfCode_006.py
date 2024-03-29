with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        # 將所有字元轉成小寫
        cleaned_line = line.lower()
        # 刪除所有標點符號
        pun = str.maketrans("!.,:;-?", "       ")
        cleaned_line = cleaned_line.translate(pun)
        # 依照單字切割
        words = cleaned_line.split()
        cleaned_words = "\n".join(words)
        # 每行放一個單字
        outfile.write(cleaned_words)