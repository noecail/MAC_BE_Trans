#Trame données de présenceA vers PC Central

# trame de type data
type_trame = b'00000'

# @PCcentral
add_dest = b'111011000101010111111001111110111011111011101110'

# @GEI215presenceA
add_src = b'111011000101010111111001001010001000111100010000'

# donnee du capteur
f = open("capture_test.txt", "r")
data = f.read()
# convertir data en bytes
data_bit = b''
for bit in data:
    data_bit += b'0' if bit=='0' else b'1'

# code à ajouter avant décodage et retrouver après décodage
crc = b'000'

# concatenation des parties de la trame
trame = type_trame + add_dest + add_src + data_bit + crc

print("trame : ")
print(trame)
print(type(trame))

#
#
#ALGO CRC
#
#

trame_crc = trame


print("trame_crc : ")
print(trame_crc)
print(type(trame_crc))


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
