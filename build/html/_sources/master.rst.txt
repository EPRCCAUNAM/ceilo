.. Boundary Layer Ceilometer Retrieval documentation master file, created by
   sphinx-quickstart on Sun Feb 18 15:08:23 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: RUOA_logo2.fw.png
   :scale: 75 %
   :alt: alternate text
   :align: left

Ceilo code documentation of EPR group, CCA UNAM 
===============================================================

These pages document the code use to process ceilometer raw data and interpret the backscattering signal to estimate mixed or boundary layer structure. 
This is part of work done by the Spectroscopy and Remote Sensing (EPR) Group at UNAM, Mexico using the Red Universitaria de Observatorios Atmosfericos (RUOA) instruments. 

Since 2008, a suite of commercial lidar systems, the Vaisala CL31 ceilometer, have been measuring backscattering profiles across different urban and remote parts of Mexico. 
This instrument is particularly useful for boundary layer studies due to the :math:`\sim 10` [m] vertical resolution and a temporal resolution
ranging from 2 to 16 s. Through the analysis of these profiles, :cite:`jlgf2018` showed the typical diurnal and seasonal variability of the mixed-layer height.

.. image:: ceilo.jpg
   :scale: 75 %
   :alt: alternate text
   :align: center

Figure 1. Ceilometer Vaisala CL31. This instrument is an optical active remote sensing instrument equipped with an eye-safe laser that interacts with atmospheric aerosols in such a way that
the backscattered signal has been found to be a good proxy for aerosol distribution :cite:`brooks2003,jlgf2018`.


The documentation in this webpage serves to describe code functionality, present some examples of how the code may be adapted to process raw ceilometer data or, if this is the case, to estimate and visualize mixed layer height variability. 
Find index below. 

.. toctree::
   :name: mastertoc
   :numbered:
   :maxdepth: 5
   :caption: Contents:




   processing
   secondary
   tools
   dftools
   gallery
   


.. _linking-pages:

=============
Linking Pages
=============

| `Grupo de Espectroscopia y Percepcion Remota (EPR), Centro de Ciencias de la Atmosfera, UNAM <https://www.atmosfera.unam.mx/ciencias-ambientales/espectroscopia-y-percepcion-remota/>`_.
| `Laboratorio de Espectroscopia y Percepcion Remota <https://www.atmosfera.unam.mx/ciencias-ambientales/espectroscopia-y-percepcion-remota/laboratorio-de-espectroscopia/>`_.
| `Red Universitaria de Observatorios Atmosfericos <http://www.ruoa.unam.mx/>`_.


   .. sectionauthor:: Garcia-Franco J.L. <jgcaspark@ciencias.unam.mx>

Authors and Contributions
--------------------------

| Lead Scientists: *Grutter, M., Bezanilla A., Stremme W., Ruiz-Angulo A.*
| Main code author: *Garcia-Franco J.L.*
| Original code: *Stremme W.*
| Contributions from: *Burgos A.*


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
