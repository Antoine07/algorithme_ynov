

def search_char_v1(x, content):

    for i in range(len(content)):

        if content[i] == x :
            return i

    return None

print(search_char_v1("r", "bonjour"))

def search_char_v2(x, content):
    i = 0
    while i <len(content) and content[i] != x:
        i += 1

    if i < len(content):
        return i

    return None

print(search_char_v2("o", "bonjour"))