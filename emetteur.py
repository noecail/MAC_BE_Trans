# Homemade
def string_to_binary(input_string):
    output_binary = b''
    for bit in input_string:
        output_binary += b'0' if bit=='0' else b'1'
    return output_binary
        
# Pour le CRC
def xor(a, b):
 
    # initialize result
    result = []
 
    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return (''.join(result))

# Pour le CRC
# Performs Modulo-2 division
def mod2div(dividend, divisor):
 
    # Number of bits to be XORed at a time.
    pick = len(divisor)
 
    # Slicing the dividend to appropriate
    # length for particular step
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
 
        if tmp[0] == '1':
 
            # replace the dividend by the result
            # of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + dividend[pick]
 
        else: # If leftmost bit is '0'
 
            # If the leftmost bit of the dividend (or the
            # part used in each step) is 0, the step cannot
            # use the regular divisor; we need to use an
            # all-0s divisor.
            tmp = xor('0'*pick, tmp) + dividend[pick]
 
        # increment pick to move further
        pick += 1
 
    # For the last n bits, we have to carry it out
    # normally as increased value of pick will cause
    # Index Out of Bounds.
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword


# Pour le CRC
# Function used at the sender side to encode
# data by appending remainder of modular division
# at the end of data.
def encodeData(data, key):
 
    l_key = len(key)
 
    # Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
 
    # Append remainder in the original data
    return data + remainder



###
###  Trame de type données, de presenceA vers PCcentral
###

# trame de type data
type_trame = "00000"

# @GEI215presenceA
add_dest = "111011000101010111111001001010001000111100010000"

# @PCcentral
add_src = "111011000101010111111001111110111011111011101110"

# donnee du capteur
f = open("capture_test.txt", "r")
data = f.read()
data = data[:-1] #supprimer le retour à la ligne


# concatenation des parties de la trame
trame = type_trame + add_dest + add_src + data

print("trame : ")
print(trame)
print(type(trame))
print('\n')

#ALGO CRC
cle = "10001"
trame_crc = encodeData(trame,cle)


print("trame_crc : ")
print(trame_crc)
print(type(trame_crc))
print('\n')


trame_crc_binary = string_to_binary(trame_crc)


print("trame_crc_binary : ")
print(trame_crc_binary)
print(type(trame_crc_binary))
print('\n')

# a) créer l'octet en bytes avec b'xxxxxxxx'
# b) concaténer avec un +
# c) si besoin, trame.decode('utf-8')


### utile possiblement : création d'un type byte et conversion en string
### exemple : (0101)2 ---> "0101"
#byte_string = b'10101010'
#string = byte_string.decode('utf-8')
#print(byte_string)
#print(string)
#print(type(byte_string))
#print(type(string))


### utile possiblement : convertir ASCII en bin ?
#a = "a"
#data = (''.join(format(ord(x), 'b') for x in a))
#print("expected : ")
#print("01100001")
#print(data)
#print(type(data))


print("Transmission")
print("--")
print("----")
print("------")


print("")


print("------")
print("----")
print("--")
print("Réception")

print("")

# Trame reçue
trame_recue_binary = trame_crc_binary
print("trame_recue_binary : ")
print(trame_recue_binary)
print(type(trame_recue_binary))
print('\n')

# Conversion en string de la trame reçue
trame_recue_string = trame_recue_binary.decode('utf-8')
#trame_recue_string = "00000111011011101010111111001001010001000111100010000011011000101010111111001111110111011111011101110010010011100110010001"
print("trame_recue_string : ")
print(trame_recue_string)
print(type(trame_recue_string))
print('\n')

print("Decodage en cours...")
cle = "10001"

#Verification de la trame
reste = mod2div(trame_recue_string,cle)
print("reste : " + reste)
a_comparer = '0'*(len(cle)-1)
if reste == a_comparer:
    print("Transmission correcte !")
else:
    print("Erreur lors de la transmission")
    
# Retrait du code CRC de la trame recue
trame_sans_crc = trame_recue_string[:-4]
print("\nLa trame recue contient les informations suivantes : ")


# Recuperation des informations contenues dans la trame
type_trame_recu = trame_sans_crc[:5]
print("type_trame_recu | " + type_trame_recu)

add_dest_recu = trame_sans_crc[5:53]
print("add_dest_recu   | " + add_dest_recu)

add_src_recu = trame_sans_crc[53:101]
print("add_src_recu    | " + add_src_recu)

data_recu = trame_sans_crc[101:]
print("data_recu       | " + data_recu)

print("")

# Traitement des informations
type_trame_recu_litteral = "donnees" if type_trame_recu=="00000" else "acquittement"


def switch_bat(batiment):
    print(batiment)
    if batiment == "001010":
        return "GEI"
    if batiment == "000110":
        return "CSH"
    else:
        return "inconnu"

def switch_etage(etage):
    print(etage)
    if etage == "1001":
        return "sous-sol -1"
    if etage == "0000":
        return "rez de chaussee"
    if etage == "0001":
        return "1er etage"
    if etage == "0010":
        return "2eme etage"
    else:
        return "inconnu"

def switch_salle(salle):
    print(salle)
    return str(int(salle,2))

def switch_type(type_trame):
    print(type_trame)
    if type_trame == "0000":
        return "cafe"
    if type_trame == "0001":
        return "presence"
    if type_trame == "0010":
        return "luminosite"
    if type_trame == "0011":
        return "actionneur"
    else:
        return "inconnu"

def switch_id(ident):
    return(ident)

add_dest_recu_litteral = " au batiment "+ switch_bat(add_dest_recu[24:30]) + " au " + switch_etage(add_dest_recu[30:34]) + " dans la salle " + switch_salle(add_dest_recu[34:40]) + ". C'est un appareil de type " + switch_type(add_dest_recu[40:44]) + " et son identifiant est " + switch_id(add_dest_recu[44:] + ".")


add_src_recu_litteral = add_src_recu

data_recu_litteral = data_recu


print("La trame recue est de type " + type_trame_recu_litteral + ", elle provient de la machine situee" + add_dest_recu_litteral + " Elle est a destination de la machine " + add_src_recu_litteral)
print("Voici les donnees contenues : " + data_recu_litteral + "\n")

print("Programme terminé !")
