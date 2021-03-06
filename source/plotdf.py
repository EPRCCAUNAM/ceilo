"""
Plotting Data-Frame
=====================

.. toctree::
   :maxdepth: 2

This is the main plotting package
"""

#!/usr/bin/python/env
# -*- coding: utf8 -*-
#Version 201605
#import matplotlib
#matplotlib.use('Agg')
import os
import numpy as np
import glob
import sys
import math
import pandas as pd
import time
import matplotlib.pyplot as plt
import datetime
from ceilotools import *
from dftools import *
carpeta='/home/D1_CEILO/JQRO/Results_day/Angel/jqro.csv'
#outf=outputdir+'all_avgperiods.csv'
outputdir='/home/D1_CEILO/UNAM/PRCL/Results/paperplots/'
outfile=carpeta
dirlist=[]
labe=['MLH (m)']
base=1.0/6.0
df=pd.read_csv(outfile)
#dfold.index=dfold[dfold.columns[0]]
#standard=dfold['Min60']
df.index=df[df.columns[0]]
#df['10 minavg']=standard
#df.to_csv(outfile)
#df['Gradient_Ipm']=df['Gradient_Ipm']-60
#darange=pd.date_range(start=datetime.datetime(2008,12,2,0,0),end=datetime.datetime(2016,6,4,23,55),freq='5min')
#print darange
#ndex=pd.to_datetime(darange)
print df.columns
#x=yy
df.index=pd.to_datetime(df.index)
print df.head()
lista=['MLH (m)']
#print len(df['G-F2']), len(df['G-F'])
#print data
#ilist=[60,100,140,200]
#hourly(data,False,False,'10 min',False)
#df2.to_csv(outputdir+'all_avgperiods.csv',index_label='Fecha y hora')
#df=df2
colorlist=['k','b']
#dt=df['2009':]
#dx=df['2011':'2017']
#early=dt.groupby([dt.index.hour,dt.index.minute]).mean()
#after=dx.groupby([dx.index.hour,dx.index.minute]).mean()
#plt.plot(range(750,3000),range(750,3000))
#plt.figure(figsize=(12,9))
#plt.xlabel('2008-2010 (m)')
#plt.ylabel('2011-2016 (m)')
#plt.grid()
#plt.show()
#df=dx
#corrplot(df,outputdir)
#x=yy
#df=dt.append(dx)
#df=df[(df.year != 2010) | (df.year==2010 and df.month <5)]
f,axarr=plt.subplots(3,sharex=True,figsize=(16,16))
for j,i in enumerate(lista):
#	print i#
	c=colorlist[j]
	data=df[i]
	data=data.dropna()
	print 'Important print'
	print len(data), len(df)
	#data=data[data>100]
	#print data
	avg=labe[j]
#	monthtable(data)
	#denom=4000-ilist[j]
	#minutes(data,data,False,True,False,avg,False,c)
	#minutes(data,data,False,True,False,avg,False,c)
	#plt.show()
	#plt.savefig(outputdir+'jqroevolution.png')
	#plt.close()
#	plt.grid()
#	plt.grid()
#	x=data.groupby([data.index.hour,data.index.minute,data.index.month]).mean().unstack()
	#store=pd.HDFStore('output.h5')
#	y=np.array(x)
#	print x
#	print y
#	f=open('tabla.txt','w')
#	for i,j in enumerate(x.index):
#		f.write(str(j[0])+' '+str(j[1])+' '+str(y[i][0:11])+'\n')
#	x=yy
	#yearly(df,filtered,output,name)
	#Filtered=True or False if filter needed for bad years
	#ouput=Directory to put plot in
	#name=filename of plot .png
#	yearly(data,True,'../../PRCL/Results/Plots/article/','yearly')
	# df= Data Frame Pandas
	# show= True or False to show graph at end of script
	# rmean = True or False to use or not running mean algorithm
	# save = True or False to auto save figure.
	# name = Label for plot if needed

#x	# wstd = True or False to plot std instead of df.
#	minutes(data,False,True,False,avg,False,c)
#	blhanomaly(data,outputdir+'Plots/meanmonthly.png')
#	plt.savefig(outputdir+'Plots/article/devol.png')
#	x=yy
#	plt.grid()
#	bimonthly(data,'../../PRCL/Results/Plots/bm_
	#bimonthly(data,outputdir+'jqrobm_annomal.png')
#	bimonthly(data,outputdir+'Plots/article/dmlhdt.png')
#	blhanomaly(data,outputdir+'Plots/article/mean_tseries.png')
#	plt.plot(one)
	#cleanday(data)
	mlhmax(data,c,f,axarr,avg,outputdir+'jqro_longt.png')
	#bd=data.groupby([df.index.year, df.index.month]).mean()
	#bd=bd.groupby([bd.index.month,bd.index.year]).mean()
	#bd.plot()
#for j in axarr:
#	j.grid()
#	j.legend(loc='best')
#plt.grid()
#plt.show()
#plt.xlabel(u'Year',fontsize=20)
#plt.grid()
	#plt.xticks(size=16)
#plt.tight_layout()
#plt.savefig(outputdir+'timeseries_3.eps')
#plt.show()
#x=yy
#plt.grid()
#plt.legend(loc='upper left')
#plt.savefig(outputdir+'filtercomparsion_2.eps')
#plt.show()
x=yy
plt.xlim([0,24])
#plt.legend(loc='upper left',title=u'Filter',fontsize=11)
plt.grid()
plt.savefig(outputdir+'Plots/cesar1.png')
plt.close()
