import sqlite3
import networkSystem

def create_database():

    net = networkSystem.Network("IPI1-DEV")
    serv1 = networkSystem.Server("S1")
    serv2 = networkSystem.Server("S2")     
    serv3 = networkSystem.Server("S3")

    conn = sqlite3.connect('NetworkDB1.db')
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
        (serv1.name, net.port_input[0], 5000, serv1.client, net.port_input, serv1.price),
        (serv2.name, net.port_input[1], 5000,serv2.client , net.port_input, serv2.price),
        (serv3.name, net.port_input[2], 5000,serv3.client , net.port_input, serv3.price)
    ]
    cur.executemany("INSERT INTO Server (name, price, ClientsNameTable, port_input, TotalPriceServ) VALUES (?, ?, ?, ?, ?)", servers)

    network = [
        (str(net.port_output), 18000),
    ]
    cur.executemany("INSERT INTO Network (ListPort, TotalPriceNet) VALUES (?, ?)", network)

    conn.commit()
    cur.close()
    conn.close()
