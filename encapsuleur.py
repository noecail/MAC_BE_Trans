from utils import *


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
f = open("capture.bin", "rb")
data_bin = f.read()
data = data_bin.decode('utf-8')
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



print("Transmission")
print("--")
print("----")
print("------")



f = open("mac_to_phy.bin", "wb")
f.write(trame_crc_binary)
f.close()
