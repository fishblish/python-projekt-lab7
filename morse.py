#cipher - morse z liter
#decipher - litery z morse'a
#citext - szyfr morsowy odpowiadajacy jednej literze
#i - licznik spacji miedzy morsowymi symbolami
#text - tekst do (od)szyfrowania

morse_dictionary = {'a': '.-', 'b': '-...',
                   'c': '-.-.', 'd': '-..', 'e': '.',
                   'f': '..-.', 'g': '--.', 'h': '....',
                   'i': '..', 'j': '.---', 'k': '-.-',
                   'l': '.-..', 'm': '--', 'n': '-.',
                   'o': '---', 'p': '.--.', 'q': '--.-',
                   'r': '.-.', 's': '...', 't': '-',
                   'u': '..-', 'v': '...-', 'w': '.--',
                   'x': '-..-', 'y': '-.--', 'z': '--..'}

def decrypt(text):
    text += ' ' #dodatkowa spacja na koniec calosci
    decipher = ''
    citext = ''
    for letter in text:
        if (letter != ' '):
            i = 0 #licznik zwiazany ze spacja
            citext += letter #dopóki nie trafimy na spacje to mamy jeden znak
        else: #czyli spacja
            i += 1 #i=1 (czyli to co tu za pierwszym razem) to pojedyncza spacja
            if i==2: #czyli nowe slowo
                decipher += ' '
            else:
                decipher += list(morse_dictionary.keys())[list(morse_dictionary.values()).index(citext)] #dodajemy znak na podstawie slownika
                citext = ''
    return decipher

def encrypt(text):
    cipher = ''
    for letter in text:
        if letter != ' ':
            cipher += morse_dictionary[letter] + ' '
        else:
            #spacja - przerwa między znakami, dwie - między słowami
            cipher += ' '
    return cipher

def morse(input_file, output_file, what): #funkcja wywolujaca encrypt lub decrypt linia po linii w zaleznosci od parametru
    # what - wskazuje co zrobic
    # e - encrypt, d - decrypt
    odczyt = open(input_file, 'r')
    zapis = open(output_file, 'w')
    if what=='e':
        for line in odczyt:
            line = line.rstrip()
            zapis.write(encrypt(line.lower()) + '\n')
    if what=='d':
        for line in odczyt:
            line = line.rstrip()
            zapis.write(decrypt(line.lower()) + '\n')
    odczyt.close()
    zapis.close()
