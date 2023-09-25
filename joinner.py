import time
import random
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader

def start_infos():
    infos = [
        "Logiciel pour combiner/joindre des fichiers PDF",
        "Attention !!!!!!!!! Asurez-vous d'avoir executer ce programme dans le meme repertoire que des fichiers a combiner/joindre ",
        "Vous Devez Simplement Entrez le Nom et Le Nombres des Fichiers a combiner/joindre",
    ]

    for fs in infos:
        print(fs)
        print()
        time.sleep(1.8)

def get_numbers_files():
    numbers = int(input("Entrez le nombres de fichiers a combiner/joindre: "))
    return numbers

def get_files_name():
    numbers = get_numbers_files()
    found = glob.glob("*")
    files = []
    if numbers:
        for nbs in range(numbers):
            nbs_name = input(f"Entrez le nom pour le fichier {nbs+1}: ")
            for fd in found:
                if fd == nbs_name:
                    if nbs_name.endswith(".pdf"):
                        files.append(nbs_name)
                    else:
                        print("Les Fichiers doivent etre de type (PDF) .........././././././././././././")
                else:
                    print("Desole Fichier Introuvable .........................../././././././././././.")
    return files

def get_file_name_out():
    return input("Entrez le nom du fichier en sorite SANS l'extension [.pdf] : ")


def joinner_function():
    try:
        content_out = PdfFileWriter()
        files = get_files_name()
        file_name_out = get_file_name_out()
        if files:
            for fls in files:
                fla = open(f"{fls}", "rb")
                flas = PdfFileReader(fla)
                if flas.getNumPages() >1:
                    for i in range(flas.getNumPages()):
                        content_out.addPage(flas.getPage(i))
                elif flas.getNumPages() == 1:
                    content_out.addPage(flas.getPage(0))
                else:
                    print('ERREUR ABSOLUE !!!!!!!!!!!!! ...../././././././.')
            if file_name_out:
                file_out = open(f"{file_name_out}.pdf", "wb")
            else:
                file_out = open("fichiers_sortie.pdf", "wb")

            content_out.write(file_out)
            file_out.close()
        else:
            print("Fin du Processus .........././././././././././././././")
    except:
        print("Fin du Processus .........././././././././././././././")


start_infos()

joinner_function()

input()
