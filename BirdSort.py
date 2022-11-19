import os
from tkinter import Tk, filedialog
import datetime
import pathlib
from pathlib import Path
import shutil

print("By Wojtekb30, 2022")
print("Hello! This program will sort files based on their type and date (for technical reasons it will ignore .py, .ini and .exe files tho)")
print("Witaj! Ten program posortuje pliki wg. ich typu i daty (program ignoruje pliki .py, .ini i .exe)")
input("Press ENTER/RETURN to start | Naciśnij ENTER/RETURN by rozpocząć ")
root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.

root.attributes('-topmost', True)
# folder path
dir_path = filedialog.askdirectory()
print("Wybrano: | Chosen:")
print(dir_path)
print("Type '1' to sort by creation date. Type anything else to sort by modification date:")
print("Wpisz '1', aby sortować według daty utworzenia. Wpisz cokolwiek innego, aby sortować według daty modyfikacji:")
rodzajsort = input()
print("Are you sure to start? | Jesteś pewnien, że chcesz rozpocząć?")
input("Press ENTER/RETURN to start | Naciśnij ENTER/RETURN by rozpocząć ")

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
        

n=0
while n<len(res):
    if str(rodzajsort)=="1":
        czasplikuraw = os.path.getctime(dir_path+"/"+res[n])
    else:
        czasplikuraw = os.path.getmtime(dir_path+"/"+res[n])
    rozszerzenie = pathlib.Path(dir_path+"/"+res[n]).suffix
    czasplikuu = datetime.datetime.fromtimestamp(czasplikuraw)
    czaspliku=str(czasplikuu)
    czaspliku = czaspliku[0:10]
    print("File: "+str(dir_path+"/"+res[n])+" |Time: "+str(czaspliku)+" |Type: "+str(rozszerzenie))
    if str(rozszerzenie).lower()!=".exe" and str(rozszerzenie).lower()!=".py" and str(rozszerzenie).lower()!=".ini":
        sciezka = Path(dir_path+"/"+rozszerzenie[1:]+"_files/"+czaspliku)
        print(sciezka)
        os.makedirs(sciezka, exist_ok = True)
        shutil.move(dir_path+"/"+res[n], sciezka)

        
        
        print("Sorted")
    else:
        print("File skipped")
    
    n=n+1
print(" ")
print("Done")
input("Press ENTER/RETURN to end | Naciśnij ENTER/RETURN by zakończyć ")