import codecs
from ctypes import BigEndianStructure
import re
import encodings

def add_to_dictionary(dictionary, to_add):
    if(len(dictionary + to_add)>4095):
        dictionary += to_add
        dictionary = dictionary[4095:]
    else:
        dictionary += to_add
    return dictionary

def compress(filename):
    f = codecs.open(filename,"r","utf-8").read()
    file = open("compressed.txt", "wb")

    buffer=""
    dictionary = ""
    i=0
    while(i<len(f)):
        character = f[i]
        if buffer+character in dictionary and len(buffer) < 15:
            buffer+=character
            i+=1
        elif len(buffer) == 0:
            file.write(character.encode('utf-8'))
            dictionary = add_to_dictionary(dictionary,character)
            i+=1
        else:
            if len(buffer.encode('utf-8')) >= 3:
                file.write('\7'.encode('utf-8'))
                temp = dictionary.find(buffer)
                temp = temp << 4
                temp = temp | len(buffer)
                file.write(temp.to_bytes(2,byteorder ='big'))
            else:
                file.write(buffer.encode('utf-8'))
            dictionary = add_to_dictionary(dictionary,buffer)
            buffer = ""
    #Wypisz resztki pominięte przez pętlę
    if len(buffer) != 0:
        if buffer in dictionary:
            if len(buffer.encode('utf-8')) >= 3:
                file.write('\7'.encode('utf-8'))
                temp = dictionary.find(buffer)
                temp = temp << 4
                temp = temp | len(buffer)
                file.write(temp.to_bytes(2,byteorder ='big'))
            else:
                file.write(buffer.encode('utf-8'))
            dictionary = add_to_dictionary(dictionary,buffer)
            buffer = ""
        else:
            file.write(character.encode('utf-8'))
            dictionary = add_to_dictionary(dictionary,character)

    file.close()
    f.close()


def decompress(filename):
    f = open(filename,"rb")
    file = open("decompressed.txt", "wb")
    dictionary = ""
    buffer = b''
    character = f.read(1)
    while(character):
        if(character != '\7'.encode('utf-8')):
            file.write(character)
            buffer += character
            character = f.read(1)
        else:
            temp_dict = buffer.decode('utf-8')
            dictionary = add_to_dictionary(dictionary,temp_dict)
            buffer = b''
            #Po zaktualizowania słownika można wyszukać w nim odpowiednią zawartość
            character = f.read(2)
            character = int.from_bytes(character, byteorder='big')
            temp1 = character >> 4
            temp2 = character & 15
            found = dictionary[temp1:temp1+temp2]
            file.write(found.encode('utf-8'))
            dictionary = add_to_dictionary(dictionary,found)
            character = f.read(1)

    file.close()
    f.close() 


#compress("literacki_pl.txt")
decompress("compressed.txt")
