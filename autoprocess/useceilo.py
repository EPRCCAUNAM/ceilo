#!/usr/bin/python/env
# import library for 2-D graphs
import matplotlib
# Generar imagenes sin que aparezcan ventanas: high quality images using the Anti-Grain Geometry engine
matplotlib.use('Agg')
# pylab combina pyplot con numpy en un solo namespace, preferible en situaciones de calculos y graficos.  
#llamar a la clase ceilo (otro programa)
from ceiloclass import ceilo 
from ceilotools import *
# importar estructura matematica y ploteo (ya se hizo en pylab pero adelante se vuelve a llamar)
import numpy as np
import matplotlib.pyplot as plt
#importar modulo para acceder al sistema operativo
import os
#import smoothing de script de wolf (suaviza los puntos promediando los tres vecinos mas cercanos)
from smoothingkernel import smoothmatrix
from smoothingkernel import smoothmatrixn
import fileinput

print ( 'start')
filename='ceilocca.dat'
runv='201705'
# remove line
read=readfile('info.txt')
lines=[]
for line in fileinput.input(filename):
    if line.find('Closed') > -1 :
        print (line)
        print (line[0:12])
    if line[0:12] == '-File Closed':
            print ('hola')
    else:
            lines.append(line)
f=open(filename,'w')
f.writelines(lines)
f.close()
#'/media/1 tb/CEILO/A2111900.DAT'
readceilo=ceilo(filename)
readceilo.init()
print ('readceilo.tarr')
#print (readceilo.tarr)
#print (readceilo.ipos0)
#print (readceilo.dpos)
dt=1.0/60.0*10.
alldata=readceilo.readceilofile(filename,dt)
#print (readceilo.dpos)
allprf=alldata[2]
tarr=alldata[0]
z=alldata[1]
zmax=5000.0 #np.max(z)
amax=0.333
a0=0.01
a1=(amax-a0)/zmax
SK=smoothmatrixn(z,a0,a1,100)
print ( SK )
allprf=np.dot(SK,allprf)
at0=0.1
ST=smoothmatrixn(tarr,at0,0,10)
allprf=np.dot(allprf,ST)

### para plot
idx=[i for i,zi in enumerate(z) if zi < zmax]
z=z[idx]
allprf=allprf[idx,:]
amin=np.min(allprf)
allprf=allprf #-amin
#allprf=np.log(allprf)
#tarr,zz,
#Colorbar maximum color level y ticks range
maximum=np.max(allprf)
if maximum < 500: 
	counter=0
	while counter < maximum:
		counter+=100
	counter-=100
	maxcollevel=counter
	m0=50
else: 
	maxcollevel=550
	m0=40
#Un color cada colorss niveles (Valores sugeridos para que el colorbar tenga continuidad). 
colorss= (maxcollevel-100)/m0
tickrange = maxcollevel
#Tick every tickt number of levels
tickt =100
#Limpieza de los files
#Levels of plot
levels=range(0,maxcollevel,1)
for i in range(len(allprf[0,:])):
	for j in range(len(allprf[:,0])):
		if allprf[j,i] > max(levels):
			allprf[j,i] = max(levels)
		elif allprf[j,i] < min(levels):

			allprf[j,i] = min(levels)
#para normalise the color scale
plt.figure(figsize=(9,6))
c1=plt.contourf(tarr,z,allprf,levels)

# color bar
cticks=range(0,tickrange,tickt) #colorbar ticks
cb=plt.colorbar(c1,ticks=cticks)
cb.set_label('Backscattering [a.Units]')

##
##c1=matplotlib.pylab.contourf(tarr,z,allprf,50)
##plt.colorbar(c1)
##plt.clim(0,5000)

plt.xlabel('Time [UT-6]')
plt.ylabel('Height [m a.g.l.]')
plt.title('Ceilometer CCA-UNAM')
ttext=np.max(tarr)/3
# para obtener la fecha y la hora actual
os.system('date /T > stime.txt')
os.system('time /T >> stime.txt')
ftime=open('stime.txt','r')

sdate=ftime.readline()
stime=ftime.readline()
ftime.close()

h=int(stime[0:2])
m=int(stime[3:5])
am=stime[6:10]
rename=sdate[6:10]+sdate[3:5]+sdate[0:2]
#Print en la grafica fecha y hora. 
plt.text(ttext,3500,sdate, color='white')
plt.text(ttext,3000,stime, color='white')
plt.xlim(0,24)
plt.ylim(0,zmax)
estacion=read[1][0:4]
print estacion
mlh=np.zeros(len(tarr),dtype=float)
for i,t in enumerate(tarr):
	if t < 7.0 or t > 19.:
		up=95
	elif t < 10. or t > 16.:
		up=145
	else:
		up=185
	try: 
		mlh[i]=algmlh(allprf,'C2',mlh,i,z,tarr,t,up)
	except:
		mlh[i]=algmlh(allprf,'Gradient',mlh,i,z,tarr,t,up)

plt.plot(tarr,mlh,'wo')

plt.savefig('ceilocca.png')

if h == 11 and m > 55 and am=='p.m.':
	os.system('mkdir '+rename)
	writematrix(rename+"\\" +rename+"_"+estacion+"_matrix.txt",allprf,z,tarr,estacion,rename,runv)
	writemlh(rename+"\\" +rename+"_"+estacion+"_mlh.txt",tarr,mlh,estacion)
	writehdf(read[2:],allprf,tarr,z,mlh,rename,rename+"\\" +rename+"_"+estacion+"_.hdf")
	plt.savefig(rename+"\\" +rename+'_UNAM.png')
	os.system("pscp -pw c31l0 -r "+rename+" ceilo@132.248.8.37:/home/D1_CEILO/UNAM/New_Backup")
	os.system('rmdir '+rename+ '/s /q')
plt.show()