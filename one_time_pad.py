# one time pad
import random
import math
message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
def String2Binary(message):
    message = message.upper()
    converted: str = ""
    for letter in message:
        if letter =='A':
            converted+="00000"
        elif letter == 'B':
            converted+="00001"
        elif letter =='C':
            converted+='00010'
        elif letter=='D':
            converted+= '00011'
        elif letter=='E':
            converted+='00100'
        elif letter =='F':
            converted+='00101'
        elif letter =='G':
            converted+= '00110'
        elif letter == 'H':
            converted+='00111'
        elif letter =='I':
            converted+='01000'
        elif letter =='J':
            converted+='01001'
        elif letter=='K':
             converted+='01010'
        elif letter=='L':
            converted+='01011'
        elif letter=='M':
            converted+='01100'
        elif letter=='N':
            converted+='01101'
        elif letter =='O':
            converted+='01110'
        elif letter =='P':
            converted+='01111'
        elif letter =='Q':
            converted+='10000'
        elif letter =='R':
            converted+='10001'
        elif letter =='S':
            converted+='10010'
        elif letter =='T':
            converted+= '10011'
        elif letter =='U':
            converted+='10100'
        elif letter =='V':
            converted+='10101'
        elif letter =='W':
            converted+='10110'
        elif letter =='X':
            converted+='10111'
        elif letter =='Y':
            converted+='11000'
        elif letter == 'Z':
            converted+='11001'
        elif letter=='.':
            converted+='11010'
        elif letter=='!':
            converted+='11011'
        elif letter=='?':
            converted+='11100'
        elif letter=='(':
            converted+='11101'
        elif letter == ')':
            converted+='11110'
        elif letter=='-':
            converted+='11111'
        else:
            continue
    return converted

def Binary2String(number):
    converted = ""
    temp = []
    last_block=""
    string = ""
    num=1

    for i in range(len(number)):
        temp += number[i]
        if num % 5 == 0:
            string = list2string(temp)
            if string == '00000':
                converted +="A"
            elif string == '00001':
                converted += "B"
            elif string =='00010':
                converted += 'C'
            elif string=='00011':
                converted+= 'D'
            elif string =='00100':
                converted+='E'
            elif string =='00101':
                converted+='F'
            elif string =='00110':
                converted+= 'G'
            elif string == '00111':
                converted+='H'
            elif string =='01000':
                converted+='I'
            elif string =='01001':
                converted+='J'
            elif string =='01010':
                converted+='K'
            elif string=='01011':
                converted+='L'
            elif string =='01100':
                converted+='M'
            elif string=='01101':
                converted+='N'
            elif string =='01110':
                converted+='O'
            elif string =='01111':
                converted+='P'
            elif string =='10000':
                converted+='Q'
            elif string =='10001':
                converted+='R'
            elif string =='10010':
                converted+='S'
            elif string =='10011':
                converted+= 'T'
            elif string =='10100':
                converted+='U'
            elif string =='10101':
                converted+='V'
            elif string =='10110':
                converted+='W'
            elif string =='10111':
                converted+='X'
            elif string =='11000':
                converted+='Y'
            elif string == '11001':
                converted+='Z'
            elif string=='11010':
                converted+='.'
            elif string=='11011':
                converted+='!'
            elif string=='11100':
                converted+='?'
            elif string=='11101':
                converted+='('
            elif string == '11110':
                converted+=')'
            elif string=='11111':
                converted+='-'
            temp = []
            string=""
        num+=1
    return converted

def list2string(l):
    string = ""
    for num in l:
        string += str(num)
    return string

def generate_key(length):
    binary_string = ''.join(random.choice(['0', '1']) for _ in range(length))
    return binary_string


def one_time_pad_encryption(message): #takes string with the message and returns the cryptotext in a string
    converted_num_list = []
    converted = String2Binary(message)
    length = len(converted)
    print(len(converted))
    for letter in converted:
        converted_num_list.append(int(letter))
    key_num_list = []
    key = generate_key(length)
    for letter in key:
        key_num_list.append(int(letter))
    encrypted = []
    for i in range(length):
        encrypted.append(converted_num_list[i] ^ key_num_list[i])
    return Binary2String(list2string(encrypted)), key

def one_time_pad_decryption(encrypted_message, key): #takes the encrypted message in a string and returns the plaintext in a string
    converted_num_list = []
    converted = String2Binary(encrypted_message)
    length = len(converted)
    for letter in converted:
        converted_num_list.append(int(letter))
    key_num_list = []
    for letter in key:
        key_num_list.append(int(letter))
    decrypted = []
    for i in range(length):
        decrypted.append(converted_num_list[i] ^ key_num_list[i])
    return Binary2String(list2string(decrypted))

encrypted, key = one_time_pad_encryption(message)
print(message)
print("")
print("key:"+key)
print("")
print(encrypted)
print("")
print(one_time_pad_decryption(encrypted,key))
