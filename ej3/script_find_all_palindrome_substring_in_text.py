import sys

def find_palindromes_in_substring(text, j, k):
    palindromes = []
    while j >= 0 and k < len(text):
        if text[j] != text[k]:
            break
        palindromes.append(text[j : k + 1])
        j -= 1
        k += 1
    return palindromes

def find_all_palindrome_substrings(text):
    palindromes = []
    for i in range(0, len(text)):
        palindromes += find_palindromes_in_substring(text, i - 1, i + 1)
        palindromes += find_palindromes_in_substring(text, i, i + 1)
    return palindromes

def main():
    text = sys.argv[1]
    palindromes = find_all_palindrome_substrings(text)

    print('\n')
    print(f'Palabras encontradas: {palindromes}')

if __name__ == "__main__":
    main()

