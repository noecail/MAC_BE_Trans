import os
import binascii


def binary_to_ascii(binary_string):

    ascii_text=""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        ascii_text += chr(int(byte,2))
    return ascii_text

def ascii_to_binary(ascii_text):

    binary_string= ""
    for char in ascii_text:
        binary_string += f"{ord(char):08b}"
    #binary = string_to_binary(binary_string)
    return binary_string


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
def encoder(data, key):
 
    l_key = len(key)
 
    # Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
 
    # Append remainder in the original data
    return data + remainder

#0100101010010001

def check_crc(trame_string, cle):
    reste = mod2div(trame_string,cle)
    a_comparer = '0'*(len(cle)-1)
    if reste == a_comparer:
        print("Trame correcte !")
        trame_sans_crc = trame_string[:-3]
        return(trame_sans_crc)
    else:
        print("Erreur bit sur la trame recue : rest = " + reste)
        return(None)


def decoder(trame_sans_crc):
    type_trame_recu = trame_sans_crc[:5]
    add_dest_recu = trame_sans_crc[5:53]
    add_src_recu = trame_sans_crc[53:101]
    data_recu = trame_sans_crc[101:]
    return type_trame_recu, add_dest_recu, add_src_recu, data_recu


def creer_trame(type_trame, add_dest, add_src, data):
    trame = type_trame + add_dest + add_src + data
    #print("trame construite : ")
    #print(trame)
    #print(type(trame))
    #print('\n')
    return(trame)


def read_and_delete(fichier, supp):
	#lire la ligne
	f = open(fichier, "r")
	lignes = f.readlines()
	data=""
	if len(lignes)>0:
		data_bin = lignes[0]

		f.close()

		#supprimer la ligne
		g = open(fichier, "w")
		i = 0
		for ligne_boucle in lignes:
			if i != 0:
				g.write(ligne_boucle)
			else:
				i += 1
		g.close()

		#formater la ligne pour renvoi
		#data = data_bin.decode('utf-8')
		
		#if supp!=0:
		#data = data[:-1] #supprimer le retour à la ligne #si ça bug peut etre ici 10/01
		data = ascii_to_binary(data_bin)

	return(data)


def write_line(fichier, ligne):
    f = open(fichier, "a")
    ligne_bin = string_to_binary(ligne)
    ligne_ascii = binary_to_ascii(ligne_bin)
    if(os.stat(fichier).st_size != 0):
        f.write("\n")
    f.write(ligne_ascii)
    f.close()

    
def read_all(fichier):
    f = open(fichier)
    lines = f.readlines()
    f.close()
    return(lines)


def reset_fichier(fichier):
    os.remove(fichier)
    f = open(fichier,"w")
    print("reset")



def switch_bat(batiment):
	#print(batiment)
	if batiment == "001010":
	    return "GEI"
	if batiment == "000110":
	    return "CSH"
	else:
	    return "inconnu"

def switch_etage(etage):
	#print(etage)
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
	#print(salle)
	return str(int(salle,2))

def switch_type(type_trame):
	#print(type_trame)
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

def blabla(trame):
	type_trame_recu = trame[:5]
	#print("type_trame_recu | " + type_trame_recu)
	add_dest_recu = trame[5:53]
	#print("add_dest_recu   | " + add_dest_recu)
	add_src_recu = trame[53:101]
	#print("add_src_recu    | " + add_src_recu)
	data_recu = trame[101:]
	#print("\nLa trame recue contient les informations suivantes : ")
	type_trame_recu_litteral = "donnees" if type_trame_recu=="00000" else "acquittement"

	if add_src_recu[24:30] == "111110":
		add_src_recu_litteral = " au PC Central"

	else:
		add_src_recu_litteral = " au batiment "+ switch_bat(add_src_recu[24:30]) + " au " + switch_etage(add_src_recu[30:34]) + " dans la salle " + switch_salle(add_src_recu[34:40]) + ".\nC'est un appareil de type " + switch_type(add_src_recu[40:44]) + " et son identifiant est " + switch_id(add_src_recu[44:] + ".")

	data_recu_litteral = binary_to_ascii(data_recu)


	print("La trame recue est de type " + type_trame_recu_litteral + ", elle provient de la machine situee" + add_src_recu_litteral)
	print("Voici les donnees contenues : ")
	print(data_recu_litteral)
    
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
