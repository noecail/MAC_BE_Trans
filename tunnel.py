from utils import *

# Simule tunnel entre capteur et pcc
supp1=0
supp2=0
while True:
	truc_cap = read_and_delete("mac_to_phy_cap.txt",supp1)
	truc_pcc = read_and_delete("mac_to_phy_pcc.txt", supp2)
	supp1+=1
	supp2+=1
	if truc_cap != "":
		#Tester bit-flip lors de la transmission de la donnée : décommenter et envoyer "UU"
		#truc_cap="00000111011000101010111111001111110111011111011101110111011000101010111111001001010001000111100010000010101010101010101001010100"
		print("CAP vers PCC -- " + truc_cap)
		write_line("phy_to_mac_pcc.txt",truc_cap)
	if truc_pcc != "":
		#Tester bit-flip lors de la transmission deu ack : décommenter et envoyer "UU"
		#truc_pcc = "00001111011000101010111111001001010101000111100010000111011000101010111111001111110111011111011101110010101010101010100001010101"
		print("PCC vers CAP -- " + truc_pcc)
		write_line("phy_to_mac_cap.txt",truc_pcc)
