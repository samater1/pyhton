def dictonary_translator(kalmad):
    words = kalmad.split(' ')
    somali_translate = {
        "go": "soco",
        "come": "kaalay",
        "sleep":  "seexo"
    }
    english_translate = {
        "soco": "go",
        "kaalay": "come",
        "seexo":  "sleep"
    }
    result = ' '
    for word in words:
        if langauge == 'som':
            result += somali_translate.get(word, word) + " "
            return result
        else:
            result += english_translate.get(word, word) + " "
            return result


kalmad = input("gali kalmada: ")
langauge = input("eng > som: ").lower()
print(dictonary_translator(kalmad))

