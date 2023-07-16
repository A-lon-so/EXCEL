import pywhatkit 

#Contact
#numero_de_telefono = input("Numero de telefono: ")
#pywhatkit.sendwhatmsg("+573017475783", "Test", 11, 26)

#pywhatkit.sendwhatmsg("+573017475783", "Test", 11, 26, True, 2)


#groups 
#https://chat.whatsapp.com/EGULvrEQgOT6AegiBIflkC

goupid = input("id del grupo: ")
pywhatkit.sendwhatmsg_to_group(goupid, "Test 2", 12, 56)
