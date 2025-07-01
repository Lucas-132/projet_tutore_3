from networkSystem import *
from networkView import *
from NetworkDB import create_database
import os
import NetworkDB

if __name__ == "__main__":
    server_1 = Server("S1")
    server_2 = Server("S2", 10000)
    server_3 = Server("S3", 7000)
    server_4 = Server("S4", 4000)
    server_5 = Server("S5", 8000)

    client1 = Client("c1")
    client2 = Client("c2", 2000)
    client3 = Client("c3", 3000)
    client4 = Client("c4")
    client5 = Client("c5", 2000)
    client6 = Client("c6", 3000)
    client7 = Client("c7")
    client8 = Client("c8", 2000)
    client9 = Client("c9", 3000)
    client10 = Client("c10")
    client11 = Client("c11", 2000)
    client12 = Client("c12", 3000)
    client13 = Client("c13")
    client14 = Client("c14", 2000)
    client15 = Client("c15", 3000)
    client16 = Client("c16", 3000)

    printer1 = Printer("p1", "192.168.100.1")

    server_1.bind([client1, client2])
    server_2.bind([client3])
    server_3.bind([])
    server_4.bind([])
    server_5.bind([])

    network1 = Network("IPI1-DEV")
    network1.add_server(server_1)
    network1.add_server(server_2)
    network1.add_server(server_3)

    network2 = Network("IPI2-RESEAU")
    network2.add_server(server_4)
    network2.add_server(server_5)


    
    view = networkView([network1, network2])
    print(view)
    
    db_path = "NetworkDB1.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    create_database(network1)