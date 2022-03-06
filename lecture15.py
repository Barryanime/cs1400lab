english_to_spanish = {'I': 'Yo', 'My': 'Mi', 'am': 'soy', 'name': 'nombre', 'is': 'es', 'programmer': 'programador', 'a': 'un'}

english_sentence = input("Type of sentence: ")
english_words = english_sentence.split()

translated = " "
for word in english_words:
    print(english_to_spanish.get(word, 'unknown'))
