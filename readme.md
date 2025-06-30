# IPI1 DEV @Python 2024/2025
# ------------------
# 1/ Objectif
- IAPI021: Gérer un projet de dev informatique de A-Z (cahier des charges, conception, dev, test) par équipe de 2/3/4 en 6 1/2 journée

# 2/ Todo
Gérer un parc informatique d'ordis soit client, soit serveur référencés par un nom et un prix.
Pour monter un réseau (clients/serveurs), je passe par un switch sur lequel il y a 3 ports Serveur (ports Entrée) et 16 ports Clients (port Sortie).
Le système permet de créer clients et serveurs, mais aussi de les associer, ainsi il doit attribuer automatiquement les bons ports E et S (par tirage au sort).
La config est stockée en BD. Le coût final est demandé.

# 3/ Consignes
 - Prog Objet, il faut impérativement une (ou des) classes 'Métier' (c'est quoi le nom de cette classe, les attributs, les méthodes?) 
 - la qualité du code est à soigner (nomenclature, pertinence des choix, flexibilité, ...)
 - le programme principal est séparé de la classe 'métier'
 - traiter les erreurs (puis-je brancher 4 serveurs? Non! -> Exception)
 - l'architecture en couche (MVC 4 tiers) permet le travail de groupe (couche métier M, couche controller C, rendu V, persistance)

# 4/ Détails
- Ordi Client: nom= C1, prix=1000 (par défaut)
- Ordi Serveur: nom=S1, prix=5000 (par défaut)
- Base de données: Mysql

# 5/ Bonus
- 1/ Faire un tracé graphique du réseau avec en absisse les serveurs, en ordonnée le côut de chaque serveur (incluant les clients associés):

- Pour cela, install d'un biblio (mathplotlib, cf: https://matplotlib.org/stable/tutorials/pyplot.html ):
Pour le tracé:
1/ install pip
python -m pip install -U pip (ou py -m pip install -U pip)
2/ install mathplotlib 
py -m pip install --user -U matplotlib 

exemple de code:
import matplotlib.pyplot as plt
import numpy as np

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()
...

1.1/ Faire un tracé du réseau avec le switch 

- 2/ autre tâche: rajouter un printer (unique) côté serveur
un printeur=(adr IP, coût)

- 3/ Stockage GIT
- 4/ Configurer le système d'association Serveur/Client (Ex: S2=C1, C4, C5)

# 6/ Résultats attendus
Exemple:
Network: IPI1-DEV
        S2 Server Cost: 10000 Port: 1 Server global Cost: 14400
                C5 1000 Port: 5
                C7 1300 Port: 1
                C12 1100 Port: 16
                        P2 142.234.299.11 1000
 
        S1 Server Cost: 5000 Port: 2 Server global Cost: 7200
                C1 1000 Port: 7
                C2 1200 Port: 12

        S3 Server Cost: 7000 Port: 3 Server global Cost: 9100
                C4 1000 Port: 6
                C14 1100 Port: 14

Ports OUT: [1, 0, 0, 0, 1, 3, 2, 0, 0, 0, 0, 2, 0, 3, 0, 1] 
Network Global Cost: 30700
