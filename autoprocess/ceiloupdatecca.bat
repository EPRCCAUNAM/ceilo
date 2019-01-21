cd C:\Documents and Settings\admin_xp\Desktop\ceilo-act
DATE /T > date.txt
Dir "C:\Program Files\CL-VIEW\Datos_3\??????00.DAT" /B /O:-D > MyFilename.txt
Set /P _MyVar=<MyFilename.txt
echo %_MyVar%
copy "C:\Program Files\CL-VIEW\Datos_3\"\%_MyVar% ceilocca.dat
Dir "C:\Program Files\CL-VIEW\Datos_3\????????.DAT" /B /O:-D > MyFilename.txt
Set /P _MyVar2=<MyFilename.txt
echo %_MyVar2%
if NOT %_MyVar%==%_MyVar2% more +2 "C:\Program Files\CL-VIEW\Datos_3\"\%_MyVar2% >> ceilocca.dat
rem added second file
C:\Python27\python.exe useceilo.py
pscp.exe -pw  espectro ceiloCCA.png grutter@132.248.8.68:/var/www/espectroscopia/ceilo
move date.txt date_old.txt
rem E:
rem cd AltMet
rem pscp.exe -pw espectro AltMet.png grutter@132.248.8.68:/var/www/altzomoni/met
rem pscp.exe -pw espectro Caseta.png grutter@132.248.8.68:/var/www/altzomoni/met
rem pscp.exe -pw espectro CCAMet.png grutter@132.248.8.68:/var/www/espectroscopia/UNAM/met
