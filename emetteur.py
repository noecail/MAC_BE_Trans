#Trame données de présenceA vers PC Central

type_trame = b'00000'

add_dest = b'111011000101010111111001111110111011111011101110'

add_src = b'111011000101010111111001001010001000111100010000'

f = open("capture_test.txt", "r")
data = f.read()
#convertir data en binary string

crc = b'000'


trame = type_trame + add_dest + add_src + data + crc

#ALGO CRC



trame_crc = trame



print(trame_crc)


a = '10101010'
b = '0b11111111'
#c = bin(int(a))

data = (''.join(format(ord(x), 'b') for x in a))
print(data)
print(type(data))

byte_string = b'10101010'
string = byte_string.decode('utf-8')
print(byte_string)
print(string)
print(type(byte_string))
print(type(string))

# a) créer l'octet en bytes avec b'xxxxxxxx'
# b) concaténer avec un +
# c) si besoin, trame.decode('utf-8')
