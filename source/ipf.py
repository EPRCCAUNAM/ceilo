r"""


Idealized point function method
*********************************

@author: Burgos Andrea,
Translated to Python by JLGF.

This function obtains the residual layer height from an idealized profile.
The method is thoroughly described in [Steyn (1999), Wang et. al. (2016)] but basically obtains boundary layer parameters by
fitting an idealized backscatter profile to the observed profile, where the Residual Layer Height (RLH) is determined by the profile that reduces
the error between the idealized and the observed profiles through a minimum.

The idealized profile  :math:`B(r)` is given by:

.. math:: B(r)=\frac{B_m+B_\mu}{2} - \frac{B_m-B_\mu}{2} erf \bigg(\frac{r-r_m}{s}\bigg) .

* :math:`B_m` Mean mixed layer backscatter.
* :math:`B_\mu` mean backscatter in the air inmediately above the mixed layer depth.
* :math:`r_m` Mixed layer depth.
* :math:`erf` `Error function  <https://en.wikipedia.org/wiki/Error_function>`_.


Args:
   allprf (numpy array):  Backscattering matrix.

Kwargs:
   state (bool): Current state to be in.

Returns:
   float: Residual Layer Height (m)

A way you might use me is

>>> residual_h=ipf(backscattering,z,t)

This returns the residual layer height to be used by the algorithm.

It is important to note that this function makes use of the scipy function erf, so scipy must be installed::

    from scipy.special import erf

.. function:: ipf(allprf, z, t)

   Format the exception with a traceback.

   **allprf**: backscattering matrix, numpy array nxm dims
   **param t**: time vector, typically decimal time hours.minutes
   **param z**: height vector, typically numpy array ranging from 10 to 5000 m.
   **Return** float: Residual Layer Height

"""
#!/usr/bin/env/python
# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import erf
import os,sys,glob
# Define idealized profile function method, inputs are backscattering matrix, height (z) and time (t) arrays.
def ipf(allprf,z,t):
	# Alocation of possible entraiment values s.
	s=np.arange(10,100,10)
	# obtenemos la longitud de s
	isz=len(s)
	#indices de z
	z_i=np.arange(0,500,dtype=int)
	# indices de s
	s_i=np.arange(0,isz)
	# niveles a probar como posiblles zm
	niv=500
	# nivel minimo a partir donde se empieza a busar la altura.
	niv_min=30

	mlh=np.zeros(len(t))
	for i,tt in enumerate(t):

		rmsd=np.zeros((len(np.arange(niv_min,niv-np.max(s))),isz))
		s_espesor=np.zeros((len(np.arange(niv_min,niv-np.max(s))),isz))
	# Time-loop
		zk=np.zeros((len(t),isz),dtype=int)
		prf=allprf[:,i]
		# height loop over possible values of entrainment
		Bu=np.zeros((len(np.arange(niv_min,niv-np.max(s))),len(s)))
		B=np.zeros((len(z_i),len(np.arange(niv_min,niv-np.max(s))),len(s)))
		for k,z0 in enumerate(s):
			# Loop over all levels
			Bm=np.zeros(len(np.arange(niv_min,niv-np.max(s))))
			for ij,j in enumerate(np.arange(niv_min,niv-np.max(s))):
				zm=int(z[j-1])
				s_espesor[ij,k]=float(z[int(j+s[k])]-z[j]-1)
				Bm[ij]=np.nanmean(prf[0:j])
				Bu[ij,k]=np.nanmean(prf[j:j+s[k]])
				B[z_i,ij,k]=(((Bm[ij]+Bu[ij,k])/2.)-((Bm[ij]-Bu[ij,k])/2.))*(erf(((z[z_i]-zm))/s_espesor[ij,k]))
				rmsd[ij,k]=np.sqrt((1/float(niv))*(np.nansum(B[:,ij,k]-prf))**2)
				if np.nanmin(rmsd[niv_min:-1,k])>np.nanmean(np.nonzero(rmsd)):
					B[z_i,ij,k]=(((Bm[ij]+Bu[ij,k])/2.)-((Bm[ij]-Bu[ij,k])/2.))*(-erf(((z[z_i]-zm))/s_espesor[ij,k]))
				rmsd[ij,k]=np.sqrt((np.nansum(B[s[k]:len(z_i)-s[k],ij,k]-prf[s[k]:len(z_i)-s[k]]-1)**2)/float(niv))
			zk[i,k]=int(np.where(rmsd==np.nanmin(rmsd[:,k]))[0])+niv_min-1
		mlh[i]=z[zk[i,0]]
		if np.nonzero(np.nanmin(rmsd[:,k]))>np.nanmean(np.nonzero(rmsd)):
			mlh[i]=np.nan
		if mlh[i]<201 or mlh[i]>4300:
			ml[i]=np.nan
