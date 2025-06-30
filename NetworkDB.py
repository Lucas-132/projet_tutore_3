import sqlite3
import networkClasses



net = networkClasses.Network() 


conn = sqlite3.connect('NetworkDB.db')
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS Client")
cur.execute("DROP TABLE IF EXISTS Server")
cur.execute("DROP TABLE IF EXISTS Network")


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


clients = [(f'C{i}', 1000, net.port_sortie[i-1]) for i in range(1, 17)]
cur.executemany("INSERT INTO Client (nom, prix, port_sortie) VALUES (?, ?, ?)", clients)

servers = [
    ('S1', 5000, 'C1', str(net.port_entree), 6000),
    ('S2', 5000, 'C2', str(net.port_entree), 6000),
    ('S3', 5000, 'C3', str(net.port_entree), 6000),
]
cur.executemany("INSERT INTO Server (nom, prix, TableauDesNomsDesClients, port_entree, PrixTotalServ) VALUES (?, ?, ?, ?, ?)", servers)

network = [
    (str(net.port_sortie), 18000),
]
cur.executemany("INSERT INTO Network (ListPort, PrixTotalNet) VALUES (?, ?)", network)

conn.commit()
cur.close()
conn.close()
