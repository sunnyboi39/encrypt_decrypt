# string methods
message = input("enter your message: ")


def scramble2encrypt(phrase):
    phrase_val = len(phrase)
    phrase_new = phrase.replace(' ', '_')
    # make list for message characters
    phrase_list = []
    for i in range(0, phrase_val):
        phrase_list.append(phrase_new[i])

    print(phrase_list)
    unico_list = []
    str_new_list = []
    for char in range(0, phrase_val, 2):
        unico = ord(phrase_list[char])
        unico_list.insert(char, unico-3)
        # print("unicode list even: ", unico_list)
    for chart in range(1, phrase_val, 2):
        unicod = ord(phrase_list[chart])
        unico_list.insert(chart, unicod + 5)
        # print("unicode list odd: ", unico_list)

    for st in range(0, phrase_val):
        str_new = chr(unico_list[st])
        str_new_list.append(str_new)
        # print("encrypted message list: ", str_new_list)
    mess_encrypt = ''.join(str_new_list)
    print("encrypted message: ", mess_encrypt)
    return mess_encrypt


def scramble2decrypt():
    phrase = scramble2encrypt(message)
    phrase_val = len(phrase)
    phrase_list = []
    unico_list = []
    str_new_list = []
    for p in range(0, phrase_val):
        phrase_list.append(phrase[p])
    for char in range(0, phrase_val, 2):
        unico = ord(phrase_list[char])
        unico_list.insert(char, unico + 3)
        # print("unicode list even: ", unico_list)
    for chart in range(1, phrase_val, 2):
        unicod = ord(phrase_list[chart])
        unico_list.insert(chart, unicod - 5)
        # print("unicode list odd: ", unico_list)

    for st in range(0, phrase_val):
        str_new = chr(unico_list[st])
        str_new_list.append(str_new)
        # print("decrypted message list: ", str_new_list)
    mess_decrypt = ''.join(str_new_list)
    print("decrypted message: ", mess_decrypt)


scramble2decrypt()
