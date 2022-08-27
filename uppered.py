def highlight_word(sentence, word):
    sen= word in sentence
    return sen
    

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud "))
(highlight_word("Automating with Python is fun", "fun"))
(highlight_word("pythoneer with persistence", "persistence"))
