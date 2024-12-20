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
