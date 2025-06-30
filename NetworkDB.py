import sqlite3
import networkClasses.py
import main.py


conn = sqlite3.connect('NetworkDB.db')
cur = conn.cursor()

# Création des tables
cur.execute("""
CREATE TABLE IF NOT EXISTS Client (
    nom TEXT PRIMARY KEY,
    prix INT,
    PortSortie INT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Server (
    nom TEXT PRIMARY KEY,
    prix INT,
    TableauDesNomsDesClients TEXT,
    PortEntree INT,
    PrixTotalServ INT,
    FOREIGN KEY (TableauDesNomsDesClients) REFERENCES Client(nom)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Network (
    networkClasses.port_sortie LIST, 
    PrixTotalNet INT
)
""")

# Insertion des clients
clients = [(f'C{i}', 1000, None) for i in range(1, 17)]
cur.executemany("INSERT INTO Client (nom, prix, PortSortie) VALUES (?, ?, ?)", clients)

# Insertion des serveurs (exemple avec 3 serveurs)
servers = [
    ('S1', 5000, 'C1', 1, 6000),
    ('S2', 5000, 'C2', 2, 6000),
    ('S3', 5000, 'C3', 3, 6000),
]
cur.executemany("INSERT INTO Server (nom, prix, TableauDesNomsDesClients, PortEntree, PrixTotalServ) VALUES (?, ?, ?, ?, ?)", servers)

# Insertion réseau (exemple)
network = [
    ('1,2,3', 18000),
]
cur.executemany("INSERT INTO Network (ListPort, PrixTotalNet) VALUES (?, ?)", network)

conn.commit()
cur.close()
conn.close()
