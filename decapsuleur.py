from utils import *


f = open("phy_to_mac.bin", "rb")
trame_recue_binary = f.read()
trame_recue_binary = trame_recue_binary[:-1]


print("------")
print("----")
print("--")
print("Réception")

print("")

# Trame reçue
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
