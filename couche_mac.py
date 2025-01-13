from utils import *
import sys
import time
import threading

# @PCcentral
addr_pcc = "111011000101010111111001111110111011111011101110"
cle_crc = "1001"

type_machine = sys.argv[1]
#print(type_machine)

verbose = ""
if len(sys.argv) > 2:
	verbose = sys.argv[2]


# Fonction pour Thread PCC
def thread_pcc_recepteur():
    #addr_moi = addr_pcc
	supp=0
	while True:
		"""a_traiter = read_all("phy_to_mac_pcc.txt")
		if len(a_traiter)!=0:
			reset_fichier("phy_to_mac_pcc.txt")
			for reponse in a_traiter:
				print("PCC - trame capture recue avec crc\n" + reponse)
				reponse_sans_crc = check_crc(reponse, cle_crc)
				print("PCC - trame capture recue sans CRC\n")
				print(reponse_sans_crc)
				if reponse_sans_crc != None:
					ttr, adr, asr, dr = decoder(reponse_sans_crc)
					if adr == addr_pcc and ttr == "00000":
						#print(dr + "joliment") #joliment
						trame_ack = creer_trame("00001", asr, adr, dr)
						print("PCC - trame ack envoyee sans CRC\n")
						print(trame_ack)
						trame_ack = encoder(trame_ack, cle_crc)
						print("PCC - trame ack envoyee avec CRC\n")
						print(trame_ack)
						write_line("mac_to_phy_pcc.txt", trame_ack)
					elif adr == addr_pcc and ttr == "00001":
						write_line("buffer.txt",string_to_binary(asr)) #protection mutex
					
		"""
		reponse = read_and_delete("phy_to_mac_pcc.txt", supp)
		supp+=1
		if len(reponse)!=0:
			#print("PCC - trame capture recue avec crc\n" + reponse)
			reponse_sans_crc = check_crc(reponse, cle_crc)

			if verbose == "-v":
				blabla(reponse_sans_crc)
			#print("PCC - trame capture recue sans CRC\n")
			#print(reponse_sans_crc)
			if reponse_sans_crc != None:
				ttr, adr, asr, dr = decoder(reponse_sans_crc)
				if adr == addr_pcc and ttr == "00000":
					#print(dr + "joliment") #joliment
					trame_ack = creer_trame("00001", asr, adr, dr)
					#print("PCC - trame ack envoyee sans CRC\n")
					#print(trame_ack)
					trame_ack = encoder(trame_ack, cle_crc)
					#print("PCC - trame ack envoyee avec CRC\n")
					#print(trame_ack)
					write_line("mac_to_phy_pcc.txt", trame_ack)
				elif adr == addr_pcc and ttr == "00001":
					write_line("buffer.txt", asr) #protection mutex	"""
		
# CAPTEUR
if type_machine == "cap":
    
	# @GEI215presenceA
	#addr_moi = "111011000101010111111001001010001000111100010000"
	# @GEI215luminositeA
	addr_moi = "111011000101010111111001001010001000111100100000"
	supp=0
	while True:
		time.sleep(5)
		data = read_and_delete("capture.txt", supp)
		supp+=1
		if data != "":
			trame = creer_trame("00000", addr_pcc, addr_moi, data)
			#print("CAP - envoi trame sans crc\n")
			#print(trame)
			trame = encoder(trame, cle_crc)

			reset_fichier("phy_to_mac_cap.txt")
			ack = False
			nbr_envoi = 0

			while ack == False and nbr_envoi<3:
				#print("CAP - envoi trame avec crc\n")
				#print(trame)
				write_line("mac_to_phy_cap.txt",trame)
				time.sleep(2)
				nbr_envoi += 1
				a_traiter = read_all("phy_to_mac_cap.txt")
				if len(a_traiter) != 0:
					reset_fichier("phy_to_mac_cap.txt")
					for reponse in a_traiter:
						reponse = ascii_to_binary(reponse)
						#print("CAP - ack recu avec crc\n")
						#print(reponse)
						reponse_sans_crc = check_crc(reponse, cle_crc)
						
						if verbose == "-v":
							blabla(reponse_sans_crc)						

						#print("CAP - ack recu sans crc\n")
						#print(reponse)
						if reponse_sans_crc != None:
							ttr, adr, asr, dr = decoder(reponse_sans_crc)
							if adr == addr_moi and ttr == "00001":
							    ack = True


			if ack == True:
				print("Donnee envoyee au PC Central et acquittement recu")
			else:
				print("Abandon de l'envoi apres 3 tentatives, acquittement jamais recu")


        
# ACTIONNEUR
elif type_machine == "act":

    # @GEI213actionneurB
    addr_moi = "111011000101010111111001001010001000110100110001"
    supp=0
    while True:
        data = read_and_delete("phy_to_mac.txt", supp)
        supp+=1
        if data != "" :
            reponse_sans_crc = check_crc(data, cle_crc)

            if verbose == "-v":
                blabla(reponse_sans_crc)

            if reponse_sans_crc != None:
                ttr, adr, asr, dr = decoder(reponse_sans_crc)
                if adr == addr_moi and ttr == "00000":
                    write_line("ordre.txt",dr)
                    trame = creer_trame("00001", addr_pcc, addr_moi, dr)
                    trame = encoder(trame, cle_crc)
                    write_line("mac_to_phy.txt",trame)
        
      
    
# VERIFIER SI LE FICHIER N'EST PAS VIDE AVANT DE LIRE DEDANS
# SI OUI RENVOYER ""

#Affichage joliment

#mutex sur fichiers sensibles
    

elif type_machine == "pcc":

	# @PCcentral
	# addr_moi = addr_pcc

	# Partie réception
	thread_pcc_recep = threading.Thread(target=thread_pcc_recepteur, args=())
	thread_pcc_recep.start()
	supp=0
	# Partie émission
	addr_dest = read_and_delete("requete.txt", 0)
	if addr_dest != "":
		trame = creer_trame("00000", addr_dest, addr_pcc, data)
		trame = encoder(trame, cle_crc)
		ack = False
		nbr_envoi = 0
		while ack == False and nbr_envoi<5 :
			#print("PCC - trame encodee envoyee\n")
			#print(trame)
			write_line("mac_to_phy.txt", trame)
			time.sleep(2)
			reponse = read_and_delete("buffer.txt", supp)
			supp+=1
			#print("PCC - trame recue\n")
			#print(reponse)
			if reponse != "":
				reponse_sans_crc = check_crc(reponse, cle_crc)

				if verbose == "-v":
					blabla(reponse_sans_crc)

				if reponse_sans_crc != None:
					ttr, adr, asr, dr = decoder(reponse_sans_crc)
					if adr == addr_pcc and ttr == "00001":
						ack = True
				nbr_envoi += 1
				if ack == False:
					print("Ordre non transmis")

   
else:
    print("Machine non reconnue. Lancez le programme avec l'argument correspondant à votre machine : cap, act ou pcc\n")

