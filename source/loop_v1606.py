"""
Main file  loop_v1606.py
*********************************
This file reads the parameters in and calls functions to process and average raw data

    Args:
      ceiloparameters.txt (input file):  Backscattering matrix.
	Parameters in ceiloparameters.txt 

	Main directory5
	Output Directory
	Run Version
	Averaging time window (in minutes)
	Estacion
	
	
	

    Returns:
       files: backscattering matrix, mixed-layer height, contour plots 

    A way you might use me is

    >>> loop_v1606.py 

   :param allprf: backscattering matrix, numpy array nxm dims
   :param tvec: time vector, typically decimal time hours.minutes
   :param zvec: height vector, typically numpy array ranging from 10 to 5000 m. 
   :rtype: float: Residual Layer Height 

"""

# import library for 2-D graphs
import matplotlib
# Generar imagenes sin que aparezcan ventanas: high quality images using the Anti-Grain Geometry engine
# pylab combina pyplot con numpy en un solo namespace, preferible en situaciones de calculos y graficos.  
# importar estructura matematica y ploteo 
import numpy as np
import matplotlib.pyplot as plt
#importar modulo para acceder al sistema operativo
import sys
import fileinput
import glob,os
#carpeta donde se encuentra el script
org=os.system('pwd')
path=os.getcwd() 
filename='ceiloparameters.txt'
f=open(filename,'r')
lines=f.read().splitlines()
#Carpeta de files a reprocesar
lista=['H']

#Directorio madre
directorio=lines[1]
fdirectory=lines[3]
# Definir Estacion
estacion=lines[9]
# Se lee la version de corrida que es
runv=lines[5]
dt=lines[7]
#Crear carpetas raiz,etc. 
org=os.system('pwd')
os.chdir(fdirectory)
os.system('mkdir '+runv)
print(fdirectory)
#Carpeta de destino de los plots 
#os.chdir(fdirectory+runv+'/')
#os.system('mkdir Plots')
#os.system('mkdir MLH')
#os.system('mkdir Matrix')
#os.chdir('Matrix')
#os.system('mkdir numprof')
os.chdir(path+'/')
# Ciclo que busca archivos del mismo dia. 
for j in lista:
	carpeta=directorio
	filelist=glob.glob(carpeta+"*.DAT")
	filelist=np.sort(filelist)
	oldfile='            '	
	for i,filename in enumerate(filelist):
		print ( 'start')
		files= filename.split('/')[-1]

		if oldfile[0:6]!=files[0:6]:
			#Se da el comando de correr el script useceiloarg.py usando los argumentos dados, si files es mas de uno se dan 4 o mas argumentos
			#Files es el numero de archivos a utilizar
			comandline=  ('python ceilov201605.py %s %s %s %s %s %s' % (estacion, carpeta,fdirectory,runv,dt,files) )
			j=1
	
			try:
				nextfile=filelist[i+j].split('/')[-1]
			except:
				continue 
			#ciclo while para que se inserten como argumentos todos los archivos mientras sean del mismo dia. 
			while nextfile[0:6]==files[0:6]:
				comandline=comandline+' '+nextfile
				j=j+1
				try: 
					nextfile=filelist[i+j].split('/')[-1]
				except:
					break
		
			#Se imprime el comando al sistema, observando todos los argumentos que se insertan. 
			print(comandline)
			os.system(comandline)
			oldfile=files

#Make loop. call mlh_todf,add,clouds.py Right here. 
#I think... 	
