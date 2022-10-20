import random



def jeu_combat():

        niveau_vie = 20
        des = random.randint(1,6)
        des_adversaire = random.randint(1,6)

        print ("la force de votre adversaire est")
        print (des_adversaire)
        print (f"vous avez {niveau_vie} vie")

        jeu = str(input("""
Que voulez-vous faire ? 
1- Combattre cet adversaire 
2- Contourner cet adversaire et aller ouvrir une autre porte 
3- Afficher les règles du jeu 
4- Quitter la partie
"""))

        if jeu == "3":
            print("""
Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
            """)
            jeu_combat()

        if jeu == "4":
            print ("Merci au revoir...")
            exit()

        if jeu == "1":
            print (des)
            if des > des_adversaire:
                print("tu as gagner")
                print("-------------------------------------------")
                niveau_vie += 1
                jeu_combat()

            if des < des_adversaire:
                niveau_vie -= des_adversaire
                print("vous avez perdue")
                print("-------------------------------------------")
                jeu_combat()









jeu_combat()
