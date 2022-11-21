
def ceasar(input_file, output_file, what, n=3):
    if(what=='e'): #szyfrowanie

        fread=open(input_file,'r')
        fwrite=open(output_file,'w')
        while 1:
            # read by character
            char = fread.read(1)
            if not char:
                break

            if ord(char) in range (ord('a'), ord('z')+1):
                char=(ord(char)+n)
                if char>ord('z'):
                    char=char-ord('z')+ord('a')-1
                fwrite.write(chr(char))
            else:
                fwrite.write(char)

        fread.close()
        fwrite.close()

    if(what=='d'): #odszyfrowywanie
        fread = open(input_file, 'r')
        fwrite = open(output_file, 'w')

        while 1:
            # read by character
            char = fread.read(1)
            if not char:
                break

            if ord(char) in range (ord('a'), ord('z')+1):
                char=(ord(char)-n)
                if char<ord('a'):
                    char=char+ord('z')-ord('a')+1
                fwrite.write(chr(char))
            else:
                fwrite.write(char)

        fread.close()
        fwrite.close()

ceasar('/home/students/mat/j/jb417512/python/cos.txt', '/home/students/mat/j/jb417512/python/proba1.txt', 'd')
