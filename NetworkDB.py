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
    name TEXT PRIMARY KEY,
    price INT,
    port_output TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Server (
    name TEXT PRIMARY KEY,
    price INT,
    ClientsNameTable TEXT,
    port_input TEXT,
    TotalPriceServ INT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Network (
    ListPort TEXT, 
    TotalPriceNet INT
)
""")


clients = [(f'C{i}', 1000, net.port_output[i-1]) for i in range(1, 17)]
cur.executemany("INSERT INTO Client (name, price, port_output) VALUES (?, ?, ?)", clients)

servers = [
    ('S1', 5000, 'C1', str(net.port_input), 6000),
    ('S2', 5000, 'C2', str(net.port_input), 6000),
    ('S3', 5000, 'C3', str(net.port_input), 6000),
]
cur.executemany("INSERT INTO Server (name, price, ClientsNameTable, port_input, TotalPriceServ) VALUES (?, ?, ?, ?, ?)", servers)

network = [
    (str(net.port_output), 18000),
]
cur.executemany("INSERT INTO Network (ListPort, TotalPriceNet) VALUES (?, ?)", network)

conn.commit()
cur.close()
conn.close()
