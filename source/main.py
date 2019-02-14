"""
Idealized point function method 
*********************************
This function obtains the residual layer height from an idealized profile. .

    Args:
       allprf (numpy array):  Backscattering matrix.

    Kwargs:
       state (bool): Current state to be in.

    Returns:
       float: Residual Layer Height (m)

    Raises:
       AttributeError, KeyError

    A way you might use me is

    >>> mlhipf=ipf(backscattering)

    This returns the residual layer height to be used by the algorithm.

Here is something I want to talk about::

    def my_fn(foo, bar=True):
        A really useful function.

        Returns None

.. function:: ipf(allprf, tvec, zvec)

   Format the exception with a traceback.

   :param allprf: backscattering matrix, numpy array nxm dims
   :param tvec: time vector, typically decimal time hours.minutes
   :param zvec: height vector, typically numpy array ranging from 10 to 5000 m. 
   :rtype: float: Residual Layer Height 

"""

import numpy as np
import pandas as pd
def ipf(allprf):
	print(allprf)
	return allprf
