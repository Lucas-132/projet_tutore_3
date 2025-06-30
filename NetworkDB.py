import sqlite3
import networkClasses
import main


net = networkClasses.Network()  # 👈 on crée une instance








conn = sqlite3.connect('NetworkDB.db')
cur = conn.cursor()

# Nettoyage (dev only)
cur.execute("DROP TABLE IF EXISTS Client")
cur.execute("DROP TABLE IF EXISTS Server")
cur.execute("DROP TABLE IF EXISTS Network")

# Création des tables avec champs de type TEXT pour les listes
cur.execute("""
CREATE TABLE IF NOT EXISTS Client (
    nom TEXT PRIMARY KEY,
    prix INT,
    port_sortie TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Server (
    nom TEXT PRIMARY KEY,
    prix INT,
    TableauDesNomsDesClients TEXT,
    port_entree TEXT,
    PrixTotalServ INT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Network (
    ListPort TEXT, 
    PrixTotalNet INT
)
""")

# Insertion des clients (C1 à C16) avec port_sortie de networkClasses
clients = [(f'C{i}', 1000, str(net.port_sortie)) for i in range(1, 17)]
cur.executemany("INSERT INTO Client (nom, prix, port_sortie) VALUES (?, ?, ?)", clients)

# Insertion de serveurs avec port_entree de networkClasses
servers = [
    ('S1', 5000, 'C1', str(net.port_entree), 6000),
    ('S2', 5000, 'C2', str(net.port_entree), 6000),
    ('S3', 5000, 'C3', str(net.port_entree), 6000),
]
cur.executemany("INSERT INTO Server (nom, prix, TableauDesNomsDesClients, port_entree, PrixTotalServ) VALUES (?, ?, ?, ?, ?)", servers)

# Insertion réseau avec liste de ports sous forme de texte
network = [
    (str(net.port_sortie), 18000),
]
cur.executemany("INSERT INTO Network (ListPort, PrixTotalNet) VALUES (?, ?)", network)

conn.commit()
cur.close()
conn.close()
