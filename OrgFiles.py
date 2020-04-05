def completo():
	import os
	import time
	import shutil

	files=[[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
	files_copy=[[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
	ruta=input("Escriba la ruta que desea organizar (dejelo vacio y aprete enter dos veces si quiere la que esta por defecto): ")
	if ruta=="":
		path=os.getcwd()
	else:
		while (True):
			path=ruta
			if os.path.exists(path):
				break

	directorios=["Documentos","Presentaciones","Imagenes","Setups","Videos","Musica","Libros","Archivos Comprimidos"]

	print("Organizando --> ",path)
	type_files=os.listdir(path)
	punto="."

	for folder_name in directorios:
		if path[-1]=="\\":
			if not os.path.exists(path+folder_name):
				os.makedirs(path+folder_name)
		else:
			if not os.path.exists(path+"\\"+folder_name):
				os.makedirs(path+"\\"+folder_name)
	for c in range(len(directorios)):
		for extension in files[c]:
			for file in type_files:
				if path[-1]=="\\":
					if extension in file and not os.path.exists(path+directorios[c]+"\\"+file) and not file=="OrgFiles.exe":
						shutil.move(path+file,path+directorios[c]+"\\"+file)
				else:
					if extension in file and not os.path.exists(path+"\\"+directorios[c]+"\\"+file) and not file=="OrgFiles.exe":
						shutil.move(path+"\\"+file,path+"\\"+directorios[c]+"\\"+file)


	for folder_name in directorios:
		if ruta=="":
			path=os.getcwd()
		else:
			while (True):
				path=ruta
				if os.path.exists(path):
					break

		path=path+"\\"+folder_name
		archivos_enlistados=os.listdir(path)
		for file in archivos_enlistados:
			date=time.ctime(os.path.getctime(path+"\\"+file))
			year=date[-4:]
			if not os.path.exists(path+"\\"+year):
				os.makedirs(path+"\\"+year)
			else:
				pass
			if not os.path.exists(path+"\\"+year+"\\"+file) and not file=="Organizar fecha.exe" and not file==year and punto in file:
				shutil.move(path+"\\"+file,path+"\\"+year+"\\"+file)
	completado()


def clasificar(manual):
	import os
	import shutil
	files=[[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
	files_copy=[[".pdf",".doc",".docx",".txt"],[".pptx",".ppt",".potx",".pptm",".potm"],[".png",".PNG",".jpg",".JPG",".gif",".GIF",".jpeg",".JPEG"],[".exe",".iso",".msi",".apk"],[".mp4",".avi",".mkv"],[".mp3",".wav"],[".epub",".mobi"],[".rar",".zip"]]
	if manual:
		path=input("Introduzca la ruta que desea organizar: ")
		num_carpetas=int(input("¿Cuantas carpetas quiere crear?"))
		i=0
		directorios=[]
		fichero=["documentos","presentaciones","imagenes","setups","videos","musica","libros","archivos comprimidos"]
		while i<num_carpetas:
			carpeta=int(input("¿Que contiene la %dº carpeta?\n     1.Documentos\n     2.Presentaciones\n     3.Imagenes\n     4.Setups\n     5.Videos\n     6.Musica\n     7.Libros\n     8.Archivos Comprimidos\n-->"%(i+1)))
			fichero[i]=fichero[carpeta-1]
			files[i]=files_copy[carpeta-1]
			i+=1
		i=0
		while i<num_carpetas:
			valor=input("Introduzca el nombre de la carpeta de %s: "%fichero[i])
			directorios.append("\\"+valor)
			i=i+1
	else:
		path=os.getcwd()
		directorios=["Documentos","Presentaciones","Imagenes","Setups","Videos","Musica","Libros","Archivos Comprimidos"]


	print("Organizando --> ",path)
	type_files=os.listdir(path)


	for folder_name in directorios:
		if path[-1]=="\\":
			if not os.path.exists(path+folder_name):
				os.makedirs(path+folder_name)
		else:
			if not os.path.exists(path+"\\"+folder_name):
				os.makedirs(path+"\\"+folder_name)
	for c in range(len(directorios)):
		for extension in files[c]:
			for file in type_files:
				if path[-1]=="\\":
					if extension in file and not os.path.exists(path+directorios[c]+"\\"+file) and not file=="OrgFiles.exe":
						shutil.move(path+file,path+directorios[c]+"\\"+file)
				else:
					if extension in file and not os.path.exists(path+"\\"+directorios[c]+"\\"+file) and not file=="OrgFiles.exe":
						shutil.move(path+"\\"+file,path+"\\"+directorios[c]+"\\"+file)
	completado()


def menu():
	print("\n\n\
	░█████╗░██╗░░░░░░█████╗░░██████╗██╗███████╗██╗░█████╗░░█████╗░██████╗░░█████╗░██████╗░\n\
	██╔══██╗██║░░░░░██╔══██╗██╔════╝██║██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗\n\
	██║░░╚═╝██║░░░░░███████║╚█████╗░██║█████╗░░██║██║░░╚═╝███████║██║░░██║██║░░██║██████╔╝\n\
	██║░░██╗██║░░░░░██╔══██║░╚═══██╗██║██╔══╝░░██║██║░░██╗██╔══██║██║░░██║██║░░██║██╔══██╗\n\
	╚█████╔╝███████╗██║░░██║██████╔╝██║██║░░░░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║\n\
	░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝ ʙʏ Nᴇɪᴋᴏɴ6.\n\n")
	menu="\n\n*************************************\n* Elija una de las opciones:        *\n*     1.Organizar (auto).           *\n*     2.Organizar (manual).         *\n*     3.Organizar por fechas.       *\n*     4.Palabra clave.              *\n*     5.Completo (fecha y formato). *\n*     6.Informacion.                *\n*     7.Salir.                      *\n*************************************\n-->"
	while (True):
		opcion=int(input(menu))
		if opcion == 1:
			clasificar(0)
		elif opcion == 2:
			clasificar(1)
		elif opcion == 3:
			organizar_fechas()
		elif opcion==4:
			palabra_clave()
		elif opcion == 5:
			completo()
		elif opcion == 7:
			break
		elif opcion == 6:
			print("            ██╗░░░██╗  ░░███╗░░░░░██████╗░\n            ██║░░░██║  ░████║░░░░░╚════██╗\n            ╚██╗░██╔╝  ██╔██║░░░░░░░███╔═╝\n            ░╚████╔╝░  ╚═╝██║░░░░░██╔══╝░░\n            ░░╚██╔╝░░  ███████╗██╗███████╗\n Esta es la ░░░╚═╝░░░  ╚══════╝╚═╝╚══════╝\n\n -MODO Auto\n  Se crearan un total de 8 carpetas donde se ordenaran en cada una de ellas archivos como documentos,\n  presentaciones, imagenes, programas de instalacion, videos, musica y archivos comprimidos.\n\n -MODO Manual\n  Tendras la opcion de elejir el numero de carpetas que se crearan y su nombre, asi como\n  el tipo de archivos que quieres organizar. Solo se pueden organizar los archivos con \n  estos formatos: .pdf, .doc, .docx, .txt, .pptx, .potx, .pptm, .potm, .png, .jpg, .gif,\
	 .jpeg, \n  .exe, .iso, .msi, .apk, .mp4, .avi, .mkv, .mp3, .wav, .epub, .mobi, .rar, .zip.\n\n **En futuras versiones podra añadir mas formatos de forma manual\n\n -ORGANIZAR Fechas\n  Como su nombre indica organizara los archivos\n  basandose en la fecha de creacion.\n\n -MODO Palabra Clave\n  Se introduce la ruta a organizar y la palabra\n  que se buscara entre los archivos. Tambien\n  tienes la opcion de editar el nombre de la carpeta destino.\n  Las mayusculas se tendran en cuenta a la hora de buscar la palabra clave.\n\n")
		else:
			print("Esa opcion no existe. Pruebe con otra.")

def organizar_fechas():
	import os
	import time
	import shutil
	punto="."
	texto="¿Esta seguro de que quiere ejecutar este comando?(s/n)"
	opcion=input(texto)
	if opcion=='s':
		path=os.getcwd()
		archivos_enlistados=os.listdir()
		print(archivos_enlistados)
		for file in archivos_enlistados:
			date=time.ctime(os.path.getctime(path+"\\"+file))
			year=date[-4:]
			if not os.path.exists(path+"\\"+year):
				os.makedirs(path+"\\"+year)
			else:
				pass
			if not os.path.exists(path+"\\"+year+"\\"+file) and not file=="Organizar fecha.exe" and not file==year and punto in file:
				shutil.move(path+"\\"+file,path+"\\"+year+"\\"+file)
	elif opcion=='n':
		menu()
	completado()
def palabra_clave():
	import os
	import shutil
	# MOVER A CARPETA DETERMINADA

	ruta=input("Escriba la ruta que desea organizar (dejelo vacio y aprete enter si quiere la que esta por defecto): ")
	if ruta=="":
		path=os.getcwd()
	else:
		while (True):
			path=ruta
			if os.path.exists(path):
				break
	kyw=[]
	while (True):

		add=input("Introduzca la palabra clave (enter para detener): ")
		kyw.append(add)
		if add=="":
			break
		else:
			pass

	folder_name=input("Introduzca el nombre de la carpeta que desea crear o la ruta de la carpeta destino: ")
	if "\\" in folder_name:
		folder_path=folder_name
	else:
		folder_path=path+"\\"+folder_name
	file_names=os.listdir(path)
	contador=0

	for each_kyw in kyw[:-1]:
		for file in file_names:
			if not os.path.exists(folder_path) and each_kyw in file and "." in file:
				os.makedirs(folder_path)
			if each_kyw in file and not os.path.exists(folder_path+"\\"+file) and not file=="OrgFiles.exe" and "." in file:
				shutil.move(path+"\\"+file,folder_path+"\\"+file)
				contador+=1

	if contador==0:
		print("No se ha encontrado ningun archivo con la palabra clave. ")
		menu()
	else:
		completado()
def completado():
	input("\n\n\
	█▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ ▄▀█ █▀▄ █▀█\n\
	█▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ █▀█ █▄▀ █▄█")
	return

menu()
