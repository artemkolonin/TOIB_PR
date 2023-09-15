import string, itertools

def smart_input(inp):
    all_digits = True
    positive = True
    for sym in inp:
        if sym < '0' or sym > '9':
            all_digits = False
    if all_digits:
        inp = int(inp)
        if inp < 0:
            positive = False
    return(all_digits, positive)

print('Введите режим работы (0 - буквы, 1 - буквы+цифры, 2 - буквы+цифры+символы):')
mode = input()
while mode < '0' or mode > '2':
    print('Недопустимое значение')
    print('Введите режим работы (0 - буквы, 1 - буквы+цифры, 2 - буквы+цифры+символы):')
    mode = input()
mode = int(mode)
print('Введите максимальную длину пароля:')
maxlen = input()
all_digits, positive = smart_input(maxlen)
while not positive or not all_digits:
    print('Недопустимое значение')
    print('Введите максимальную длину пароля:')
    maxlen = input()
    all_digits, positive = smart_input(maxlen)
maxlen=int(maxlen)
print('Введите максимальное число паролей для каждой длины:')
max_passwords = input()
all_digits, positive = smart_input(max_passwords)
while not positive or not all_digits:
    print('Недопустимое значение')
    print('Введите максимальное число паролей для каждой длины (0 - ограничения нет):')
    max_passwords = input()
    all_digits, positive = smart_input(max_passwords)
max_passwords=int(max_passwords)
if mode == 0:
    azbuka = string.ascii_letters
elif mode == 1:
    azbuka = string.ascii_letters+string.digits
elif mode == 2:
    azbuka = string.ascii_letters+string.digits+string.punctuation
res_arr = []
for length in range(1, maxlen+1):
    check_count = 0
    pack = itertools.combinations_with_replacement(azbuka, length)
    for example in pack:
        word = ''
        for letter in example:
            word += letter
        res_arr.append(word)
        check_count += 1
        print(word)
        if max_passwords > 0 and check_count >= max_passwords:
            break
        words_comb = itertools.permutations(word, length)
        for words in words_comb:
            new_word = ''
            for letter in words:
                new_word += letter
            if new_word not in res_arr:
                res_arr.append(new_word)
                print(new_word)
                check_count += 1
            if max_passwords > 0 and check_count >= max_passwords:
                break
        if max_passwords > 0 and check_count >= max_passwords:
            break
    if max_passwords > 0 and check_count >= max_passwords:
        continue
file = open('result.txt', 'w')
for word in res_arr:
    file.write(word+' ')
file.close()