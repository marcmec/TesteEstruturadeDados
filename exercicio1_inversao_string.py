""" def inverter_string(string: str):
    return string[::-1]

print(inverter_string("hello world")) """


def inverter_string_pilha(string: str):
    pilha = []
    index_len_string = len(string) - 1
    string_final = ""
    for i in range(index_len_string + 1):
        pilha.append("")
    
    while(index_len_string >= 0):
        for char in string:
            pilha[index_len_string] = char
            index_len_string -= 1

    return string_final.join(pilha)

print(inverter_string_pilha("hello"))


