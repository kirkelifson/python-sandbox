import string, sys
alpha = list(string.ascii_lowercase)
for shift in range(1, 26):
    print 'rot-%d: ' % shift
    cipher = ''
    for string in sys.argv[1]:
        for letter in string:
            if letter.isupper():
                cipher += alpha[(ord(letter) - ord('A') + shift) % 26].upper()
            elif letter.islower():
                cipher += alpha[(ord(letter) - ord('a') + shift) % 26]
            else:
                cipher += letter
    print cipher, '\n'
