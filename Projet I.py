#Project objective: This program generates passwords randomly

#Importing needed objects
import secrets
import string
import re

#fonction qui permet de generer un mot de passe
def generator():
        #Method that returns an object of type str
        alphabet = string.ascii_letters + string.digits + string.punctuation
        #Object that generates a password within a range of 8-20:Returns an object of type str
        password = ''.join(secrets.choice(alphabet) for i in range(8,20))
        #Print the password
        return password

#fonction qui permet de verifier le mot de passe généré
def verification():
    if len(password) < 8:
        return 
    elif len(password) >20:
        return
    elif re.search(r'[0-9]',password) is None:
        return 
    elif re.search(r'[A-Z]',password) is None: 
        return 
    elif re.search(r'[*-+/;:~''.!@#$%^&*()_+<>,]',password) is None:
        return 
    elif re.search(r'[a-z]',password) is None:
        return 
    else:
        return password

#fonction qui permet de garder le mot de passe dans un fichier texte
def stockage():
    #le chemin du dossier
    stockageFile="D:/PANESS IIHT/COURS/GROUP WORK/Output Passwords.txt"
    #methode qui permet d'écrire dans le fichier texte
    stockageFile= open(stockageFile, "w")
    
    #concantenation qui va servir a représenter le texte entre et le mot de passe
    keptPassword= inputText + ':' + verification()
    #pouvoir ecrire le texte dans le fichier
    stockageFile.write(keptPassword)

#appeler les fonctions
inputText= input('Input An Account: ') 
password= generator()
print(verification())
stockage= stockage()







