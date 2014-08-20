import sys
for shift in range(1, 26):
    print 'rot-%d: ' % shift
    cipher = ''
    for string in sys.argv[1]:
        for letter in string:
            if letter.isalpha():
                base = ord('A') if letter.isupper() else ord('a')
                cipher += str(chr((ord(letter) - base + shift) % 26 + base))
            else:
                cipher += letter
    print cipher, '\n'
