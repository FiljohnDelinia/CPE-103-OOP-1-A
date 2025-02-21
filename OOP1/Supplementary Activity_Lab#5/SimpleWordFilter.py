def word_filter(sentence, bad_words):
    for word in bad_words:
        sentence = sentence.replace(word, '*' * len(word))
    return sentence

sentence = "The movie had a bad plot and some really nasty scenes, but the acting was great."
bad_words = ["bad", "nasty"]
filtered_sentence = word_filter(sentence, bad_words)
print(filtered_sentence)    