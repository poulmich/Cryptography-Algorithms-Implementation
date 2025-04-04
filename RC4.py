def list2string(l):
    string = ""
    for num in l:
        string += str(num)
    return string

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

def ShiftBitString(string, bit_number, num):
    bit_block = ""
    bit_shifts = num - bit_number
    for i in range(bit_shifts):
        bit_block += '0'
    for letter in string:
        bit_block += letter
    return bit_block

def complete_with_zeros(string, bit_number,num):
    bit_block = ""
    bit_shifts = num - bit_number
    for letter in string:
        bit_block += letter
    for i in range(bit_shifts):
        bit_block += '0'
    return bit_block

def Bytes2Bits(l):
    length = len(l)
    temp_string = ""
    ret_str = ""
    temp = 0
    for i in range(length):
        temp = bin(l[i])
        temp_string = temp[2:]
        if len(temp_string) < 8:
            ret_str += ShiftBitString(temp_string, len(temp_string), 8)
            temp_string = ""
        else:
            ret_str += temp_string
            temp_string = ""
    return ret_str

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


def String2Bytelist(string):
    N = len(string)
    temp_str = ""
    l = []
    help_str = ""
    converted = String2Binary(string)
    length = len(converted)
    bit_number = length - (length // 8) * 8
    num = 1
    for i in range(length):
        temp_str += converted[i]
        if num % 8 == 0:
            l.append(int(temp_str, 2))
            temp_str = ""
        elif num >= (length // 8) * 8:
            help_str += converted[i]
            if num == length:
                help_str = complete_with_zeros(help_str, bit_number, 8)
                l.append(int(help_str, 2))
        num += 1
    return l


def swap_list(l, i, j):
    temporary = l[i]
    l[i] = l[j]
    l[j] = temporary
    return l


def key_schelduling(S, message):
    K = []
    i = 0
    j = 0
    length = len(message)
    for num in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S = swap_list(S, i, j)
        K.append(S[(S[i] + S[j]) % 256])
    return K


def permutation(seed):
    seed_num_list = []
    for i in range(len(seed)):
        seed_num_list.append(seed[i])
    S = []
    length = len(seed)
    for i in range(256):
        S.append(i)
    j = 0
    for i in range(256):
        j = (j + S[i] + seed_num_list[i % length]) % 256
        S = swap_list(S, i, j)
    return S


def RC4_encrytpion(message, seed):  # takes string with the message and returns the cryptotext in a string
    converted_msg = String2Bytelist(message)
    length = len(converted_msg)
    converted_seed = String2Bytelist(seed)
    S = permutation(converted_seed)
    key = key_schelduling(S, converted_msg)
    encrypted = []
    for i in range(length):
        encrypted.append(converted_msg[i] ^ key[i])
    encrypted = Bytes2Bits(encrypted)
    return Binary2String(encrypted), key


def RC4_decryption(encrypted_message, key):  # takes the encrypted message in a string and returns the plaintext in a string
    converted = String2Bytelist(encrypted_message)
    length = len(converted)
    decrypted = []
    for i in range(length):
        decrypted.append(converted[i] ^ key[i])
    return Binary2String((Bytes2Bits(decrypted)))

msg="MISTAKES ARE AS SERIOUS AS THE RESULTS THEY COST"
encrypted, key = RC4_encrytpion(msg, "HOUSE")
decrypted = RC4_decryption(encrypted, key)

print(encrypted)
print(decrypted)
