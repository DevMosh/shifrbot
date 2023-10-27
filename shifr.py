alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


# ЦЕЗАРЬ
def caesar_cipher(word, key):
    result = ''
    word = word
    offset = key

    for i in word:
        num = alphabet.find(i) + offset
        result += alphabet[num]

    print('шифровка:', result)
    return result



def decrypt_caesar_cipher(word, key):
    result = ''
    word = word
    offset = key

    for i in word:
        num = alphabet.find(i) - offset
        result += alphabet[num]

    print('расшифровка:', result)
    return result

#

# ВИЖЕНЕРА
def vigener_cipher(word, key):
    key = key.upper()
    result = ''
    word = word.upper()
    key = key * (len(word) // len(key)) + key[:len(word) % len(key)]

    for i in range(len(word)):
        num = alphabet.find(key[i])
        n = alphabet.find(word[i]) + num
        result += alphabet[n]

    print(result)
    return result

#

def decrypt_vigener_cipher(word, key):
    key = key.upper()
    result = ''
    word = word.upper()
    key = key * (len(word) // len(key)) + key[:len(word) % len(key)]

    for i in range(len(word)):
        num = alphabet.find(key[i])
        n = alphabet.find(word[i]) - num
        result += alphabet[n]

    print(result)
    return result


# АТБАШ
def atbash_cipher(word):
    result = ''
    word = word.upper()

    for i in word:
        num = 32 - alphabet.find(i)
        result += alphabet[num-1]

    print(result)
    return result

#

# Полибианский квадрат
def polybian_square_cipher(word, key):
    word = word.upper()
    weight = int(key)
    result = ''
    for i in word:
        num = alphabet.find(i) + weight
        result += alphabet[num]
    return result


def decrypt_polybian_square_cipher(word, key):
    word = word.upper()
    weight = int(key)
    result = ''
    for i in word:
        num = alphabet.find(i) - weight
        result += alphabet[num]
    print(result)
    return result
#

# ТРИСЕМИУС
# def trisemus_cipher():
#     key = t8.get().upper()
#     word = t9.get().upper()
#     new_key = "".join(dict.fromkeys(key))
#     weight = int(t10.get())
#     result = ''
#
#     for i in alphabet:
#         if i not in new_key:
#             new_key += i
#     new_key *= 2
#     for i in word:
#         num = new_key.find(i) + weight
#         result += new_key[num]
#
#     print(result)
#     resultLabel8["text"] = f"Результат: {result}"
#
#
# def decrypt_trisemus_cipher():
#     key = t8.get().upper()
#     word = t9.get().upper()
#     new_key = "".join(dict.fromkeys(key))
#     weight = int(t10.get())
#     result = ''
#
#     for i in alphabet:
#         if i not in new_key:
#             new_key += i
#     new_key *= 2
#     for i in word:
#         num = new_key.find(i) + 32 - weight
#         result += new_key[num]
#
#     print(result)
#     resultLabel9["text"] = f"Результат: {result}"
#
#

# # биграмный
# def bigrams_cipher():
#     result = ''
#     key = t11.get().upper()
#     word = t12.get().upper()
#     last_letter = ''
#     new_key = "".join(dict.fromkeys(key))
#     for i in alphabet:
#         if i not in new_key:
#             new_key += i
#     if len(word) % 2 != 0:
#         last_letter = word[-1]
#         word += '0'
#
#     new_key *= 2
#     for i in range(0, len(word), 2):
#         a = new_key.find(word[i])
#         b = new_key.find(word[i+1])
#         print(a, b, word[i], word[i+1])
#         if abs(a - b) % 4 == 0:
#             result += new_key[a + 4]
#             result += new_key[b + 4]
#         elif (a // 4) == (b // 4):
#             if a % 3 == 0:
#                 result += new_key[a - 3]
#                 result += new_key[b + 1]
#             elif b % 3 == 0:
#                 result += new_key[b - 3]
#                 result += new_key[a + 1]
#             else:
#                 result += new_key[a + 1]
#                 result += new_key[b + 1]
#         else:
#             num = abs((a % 4) - (b % 4))
#             if (a % 4) < (b % 4):
#                 result += new_key[a + num]
#                 result += new_key[b - num]
#             else:
#                 result += new_key[a - num]
#                 result += new_key[b + num]
#
#     if last_letter:
#         result = result[:-2]
#         result += last_letter
#     print(result)
#     resultLabel10["text"] = f"Результат: {result}"
#
#
# def decrypt_bigrams_cipher():
#     result = ''
#     key = t11.get().upper()
#     word = t12.get().upper()
#     new_key = "".join(dict.fromkeys(key))
#     last_letter = ''
#     for i in alphabet:
#         if i not in new_key:
#             new_key += i
#     if len(word) % 2 != 0:
#         last_letter = word[-1]
#         word += '0'
#
#     new_key *= 2
#
#     for i in range(0, len(word), 2):
#         a = new_key.find(word[i])
#         b = new_key.find(word[i + 1])
#         if abs(a - b) % 4 == 0:
#             result += new_key[a - 4]
#             result += new_key[b - 4]
#         elif (a // 4) == (b // 4):
#             if a % 4 == 0:
#                 result += new_key[a + 3]
#                 result += new_key[b - 1]
#             elif b % 4 == 0:
#                 result += new_key[b + 3]
#                 result += new_key[a - 1]
#             else:
#                 result += new_key[a - 1]
#                 result += new_key[b - 1]
#         else:
#             num = abs((a % 4) - (b % 4))
#             if (a % 4) > (b % 4):
#                 result += new_key[a - num]
#                 result += new_key[b + num]
#             else:
#                 result += new_key[a + num]
#                 result += new_key[b - num]
#
#     if last_letter:
#         result = result[:-2]
#         result += last_letter
#     print(result)
#     resultLabel11["text"] = f"Результат: {result}"
#

# # Гронсфельда
# def gronsfeld_cipher():
#     key = t13.get().upper()
#     word = t14.get().upper()
#     result = ''
#     key = key * (len(word) // len(key)) + key[:len(word) % len(key)]
#     key *= 2
#     for i in range(len(word)):
#         num = alphabet.find(word[i]) + int(key[i])
#         result += alphabet[num]
#
#     print(result)
#     resultLabel12["text"] = f"Результат: {result}"
#
#
# def decrypt_gronsfeld_cipher():
#     key = t13.get().upper()
#     word = t14.get().upper()
#     result = ''
#     key = key * (len(word) // len(key)) + key[:len(word) % len(key)]
#     key *= 2
#     for i in range(len(word)):
#         num = alphabet.find(word[i]) - int(key[i])
#         result += alphabet[num]
#
#     print(result)
#     resultLabel13["text"] = f"Результат: {result}"