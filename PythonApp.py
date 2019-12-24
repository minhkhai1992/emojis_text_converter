def emoji_converter(message):
    word = message.split(' ')
    emojis ={
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for smile in word:
        output+=emojis.get(smile,smile) + " "
    return output


message = input(">")
print(emoji_converter(message))