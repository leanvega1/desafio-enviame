import sys


def search_words_equal_reverse_words(text):
    reverse_text = text[::-1]
    i, j, k = 0, 0, 0
    result = set()
    finded_word = ''

    while i < len(text):
        while j < len(reverse_text) and k < len(text):
            if text[k] == reverse_text[j]:
                finded_word += text[k]
                k += 1
                j += 1
            else:
                if len(finded_word) > 1:
                    result.add(finded_word)
                else:
                    k = i
                finded_word = ''
                j += 1

        if len(finded_word) > 1:
            result.add(finded_word)
        finded_word = ''
        i += 1
        k = i
        j = 0
    return result

def main():
    text = sys.argv[1]
    finded_words = search_words_equal_reverse_words(text)
    print('\n')
    print(f'Palabras encontradas: {sorted(list(finded_words))}')

if __name__ == "__main__":
    main()

