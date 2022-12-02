from random import randrange

nonb_ordinate = randrange(0, 500)

nonb_utilisateur = int( input("entrez le nombre:"))
chans = 5 
if nonb_utilisateur == nonb_ordinate:
    print("vous avez gagne")

while nonb_utilisateur !=  nonb_ordinate and chans != 0:
    
    if nonb_utilisateur > nonb_ordinate:
        
        print("le nombre est superieur reesayer: ")  
        nonb_utilisateur = int(input("Reentrez le nombre stp: "))
    elif nonb_utilisateur < nonb_ordinate:
        print("le nombre est inferieur reesayer: ")
        nonb_utilisateur = int(input("Reentrez le nombre stp: "))
    else:
        print("vous avez gagne")
        print(nonb_ordinate)
    chans -= 1
if chans == 0:
    print("desole vous avez perdu")
    print("le nombre secret est ")
    print(nonb_ordinate)
    
    
        
        
          