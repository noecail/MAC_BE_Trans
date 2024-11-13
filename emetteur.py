type_trame = '170'

add_dest = ''

add_src = ''

f = open("capture_test.txt", "r")
data = f.read()

crc = '000'


trame = type_trame + add_dest + add_src + data + crc

#ALGO CRC



trame_crc = trame




a = 'Ob10101010'
b = '0b11111111'
c = a+b
print(a+b)
