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
        port_output TEXT PRIMARY KEY,
        price INT,
        name TEXT
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
        (i, 1000, net.port_output[i-1].name if hasattr(net.port_output[i-1], "name") else str(net.port_output[i-1]))
        for i in range(1, 17)
    ]
    cur.executemany("INSERT INTO Client (port_output, price, name) VALUES (?, ?, ?)", clients)
    
    
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
    # Adding outputs ports recap to str message
    message = ""
    port_output_names = [] # (this array is used to display the distribution of the clients inside the network)
    for output_port_number in range(len(net.port_output)):
        if net.port_output[output_port_number] != 0:
            port_output_names.append(net.port_output[output_port_number].binded_server.name)
        else :
            port_output_names.append(0)
    message += f"{port_output_names}"
    network = [
        (message, net.global_cost()),
    ]
    cur.executemany("INSERT INTO Network (ListPort, TotalPriceNet) VALUES (?, ?)", network)

    conn.commit()
    cur.close()
    conn.close()
