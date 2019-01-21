import numpy as np
import math 
import os 
from wavelets import *
import h5py
import datetime
###########################################################################################################
###########################################################################################################
def writemlh(outputfile,horas,mlhs,estacion):
	fout=open(outputfile,'w')
	fout.write("Ceilometer Vaisala CL31. 10 min averages in "+estacion+"\n")
	fout.write("MLH from Gradient method. Espectroscopia y Percepcion Remota, CCA-UNAM\n")
	fout.write("Version del codigo: 201705  "  )
	fout.write("http://www.atmosfera.unam.mx/espectroscopia/ceilo/\n")
	fout.write("Hora.decimal  MLH(m)\n")
	for i,unamlh in enumerate(mlhs):
		timeh=horas[i]
		fout.write("%.3f         %i \n" % (timeh,unamlh))
	fout.close()	
###########################################################################################################
def writematrix(outputfile, matrix,zeta,t,estacion,filename,runv):
	fout=open(outputfile,'w')
	fout.write("Datos de retrodispersion en "+ estacion + filename+"\n" )
	fout.write("Ceilometro Vaisela CL31 \n")
	fout.write("Version del codigo: 201705\n"  )
	fout.write("http://www.atmosfera.unam.mx/espectroscopia/ceilo/\n")
	fout.write("Contacto: Espectroscopia y Percepcion Remota, CCA-UNAM\n")
	fout.write("Corrida de nombre "+str(runv)+'\n' )
	zstring="niveles:"
	for zval in zeta:
		zstring=zstring+" %i" % (zval)
	tstring ="horas: "
	for tval in t:
		tstring=tstring+" %.3f" % (tval)
	fout.write(zstring + "\n")
	fout.write(tstring +"\n")
	for i,vec in enumerate(matrix):
		for j,val in enumerate(vec):
	
			fout.write(str(val)+" ")
		fout.write("\n")
	fout.close()	


#Funcion para calcular promedios horarios para un dia, o para un archivo.
def runningMeanFast(x, N):
	ravg=np.convolve(x, np.ones((N,))/N,mode='valid')[(N-1):]
	size=len(ravg)
	dif=len(x)-len(ravg)
	apendix=np.zeros(dif)
		
	for i,j in enumerate(apendix):	
		if i == 0: 	
			apendix[i]=x[i]
		elif i == 1:
			apendix[i]=np.sum(x[i-1:i+1])/2.0
		else:
			apendix[i]=np.sum(x[i-2:i+1])/3.0
		#apendix[i]=np.sum(x[i-2:i+1])/3.0
	ravg=np.insert(ravg,0,apendix)
	#print len(ravg),len(x)
	print ravg
	return ravg
#USOS EN CEILOV 
def writenumofprof(outputfile,numofprof,t, estacion,filename):
	fout=open(outputfile,'w')
	fout.write("Datos de perfiles promediados "+ estacion + filename[1:-6]+"\n" )
	fout.write("Ceilometro Vaisala CL31 \n")
	fout.write("Version del codigo: 2016 05 \n"  )
	fout.write("http://www.atmosfera.unam.mx/espectroscopia/ceilo/\n")
	fout.write("Contacto: Espectroscopia y Percepcion Remota, CCA-UNAM\n")
	tstring ="horas: "
	for tval in t:
		tstring=tstring+" %.3f" % (tval)
	fout.write(tstring +"\n")
	for i,prof in enumerate(numofprof):
		timeh=t[i]
		fout.write("%.3f         %i \n" % (timeh,prof))
	fout.close()			
###########################################################################################################
def writeavgmatrix(outputfile,tvec,estacion,matrix,runv,averages):
	fout=open(outputfile,'w')
	fout.write('Matriz de datos diarios a promediar' +'\n')
	fout.write('Ceilometro Vaisala CL31 '+estacion+'\n')
	fout.write('Corrida correspondiente a '+str(runv)+'\n')
	tstring='Tiempo (horas):'
	avg=''
	for h,t in enumerate(tvec):
		tstring=tstring+" %.3f" % (t)
		avg=avg+str(averages[h])+' '
	fout.write(tstring + "\n")
	flistsize=matrix.shape
	tvec=flistsize[0]
	fvec=flistsize[1]
	for i in range(fvec):
		for j in range(tvec):
			point=matrix[j,i]
			fout.write(str(point)+' ')	
		fout.write('\n')
	fout.write(avg+'\n')		
	fout.close()
###########################################################################################################
#Usados en Avgmlh REDONDEANDO. 
def algmlh(allprf,method,mlh,i,z,tarr,t,uplim):
	jk=i
	lowlim=20
	uplim=uplim
	if len(z) > 255:
		lowlm=lowlim
		a1=2
		a2=10
		fi=a2
		nn=1
		try:
			vec=allprf[lowlim+1:uplim+1,jk]-allprf[lowlim:uplim,jk]
		except IndexError:
			return 
	elif len(z) <=250:
		lowlm=int(lowlim/2.)
		print 'check z'
		print lowlm 
		print z[lowlm]
		vec=allprf[lowlm+1:uplim+1,jk]-allprf[lowlm:uplim,jk]
		a1=1
		a2=20
		fi=5
		nn=2
	if  method == 'Composite 1' or method =='C2':
		imin=np.argmin(vec)
		mlh[jk]=z[imin+(lowlm)]
		bot,mlh[jk],top=haarcovtransfm(allprf,z,jk,'Auto',fi,t,uplim*10*nn,lowlim*10)
	elif method == 'C2':
		if mlh[jk]<=(lowlim*10+50) or (jk>1 and mlh[jk] - mlh[jk-1] > 200):
			a=120/a1
			bot,newmlh,top=haarcovtransfm(allprf,z,jk,'Auto',fi,t,uplim*10*nn,lowlim*10)
			if newmlh -mlh[jk-1] > 200:
				upper=uplim*10*nn
				while upper - newmlh < 500. and upper > 2500.:
					upper=upper-100 
					bot,newmlh,top=haarcovtransfm(allprf,z,jk,'Auto',fi,t,upper,lowlim*10)
			if mlh[jk]>(lowlim*10+50) or newmlh<=(lowlim*10+50):
				mlh[jk]=(newmlh+mlh[jk])/2.
			else: 
				mlh[jk]=newmlh
	return mlh[jk]

def readfile(file):
	f=open(file,'r')
	fi=f.readlines()
	f.close()
	return fi
def writehdf(lines,allprf,t,z,mlh,date,name):
	datelist=[]
	for i,tt in enumerate(t):
		hour=int(np.floor(tt))
		minute=int(round((tt-hour)*60,-1))
		datobj=str(datetime.datetime(int(date[0:4]),int(date[4:6]),int(date[6:8]),hour,minute))
		datelist.append(datobj)
	with h5py.File(name,'a') as hf:
		long=len(lines)
		j=0
		i=j+1
		while j<long:
		 	hf.attrs[lines[j]]=lines[i]
			j+=2
			i+=2
		print date
		grp=hf.create_group(date)
		dset=grp.create_dataset("Backscattering matrix",data=np.transpose(allprf))
		d2=grp.create_dataset("MLH",data=mlh)
		grp.create_dataset("Height [m]",data=z+10)
		grp.create_dataset("Datetimes",data=datelist)
		d2.attrs['VAR_DESCRIPTION']='Mixing layer height [m].'
		d2.attrs['Filter']='No cloud filter applied'
		d2.attrs['MLH method']='Minimum gradient method, combined with wavelet covariant transform method'

		dset.attrs['VAR_DESCRIPTION']='Backscatter signal (arb. units) averaged every 10 min'


