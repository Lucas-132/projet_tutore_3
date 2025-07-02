def create_database(net):
    import sqlite3
    import networkSystem

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


    clients = [
        (f'C{i}', 1000, net.port_output[i-1].name if hasattr(net.port_output[i-1], "name") else str(net.port_output[i-1]))
        for i in range(1, 17)
    ]
    cur.executemany("INSERT INTO Client (name, price, port_output) VALUES (?, ?, ?)", clients)
    
    print("Contenu de net.port_input :", net.port_input)
    servers = []
    for idx, serv in enumerate(net.port_input):
        if serv != 0:
            if not hasattr(serv, "global_price"):
                serv.global_server_cost()
            servers.append((
                serv.name,
                serv.price,
                ",".join([client.name for client in serv.client]),
                idx + 1, 
                serv.global_price
            ))
    cur.executemany(
        "INSERT INTO Server (name, price, ClientsNameTable, port_input, TotalPriceServ) VALUES (?, ?, ?, ?, ?)",
        servers
    )

    network = [
        (str(net.port_output), 18000),
    ]
    cur.executemany("INSERT INTO Network (ListPort, TotalPriceNet) VALUES (?, ?)", network)

    conn.commit()
    cur.close()
    conn.close()
