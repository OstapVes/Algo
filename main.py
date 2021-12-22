pattern = "aaaaaa"
pi = [0] * len(pattern)
index_one = 0
index_two = 1
while index_two < len(pattern):
    if pattern[index_one] == pattern[index_two]:
        pi[index_two] = index_one + 1
        index_two += 1
        index_one += 1
    else:
        if index_one == 0:
            pi[index_two] = 0
            index_two += 1
        else:
            index_one = pi[index_one - 1]

print(pi)


def kmp(text, pattern):
    text = "bbbbbbbbb"
    pattern_length = len(pattern)
    text_length = len(text)
    text_pos = 0
    pattern_pos = 0
    while text_pos < text_length:
        if text[text_pos] == pattern[pattern_pos]:
            text_pos += 1
            pattern_pos += 1
            if pattern_pos == pattern_length:
                print("Знайдено")
                return True

        else:
            if pattern_pos > 0:
                pattern_pos = pi[pattern_pos - 1]
            else:
                text_pos += 1

    if text_pos == text_length and pattern_pos != pattern_length:
        print("Не знайдено")
        return False


if __name__ == '__main__':
    kmp()


if __name__ == '__main__':
    text = "bbbaaaaaa"
    pattern = "aaaaaaaaaaa"
    kmp(text, pattern)
