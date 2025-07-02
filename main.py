from networkSystem import *
from networkView import *
from NetworkDB import create_database
import os

if __name__ == "__main__":
    try:
        server_1 = Server("S1", 10000)
        server_2 = Server("S2")
        server_3 = Server("S3", 10000)
        server_4 = Server("S4", 10000)

        client1 = Client("c1")
        client2 = Client("c2", 2000)
        client3 = Client("c3", 3000)
        client4 = Client("c4", 1100)
        client5 = Client("c5", 2000)
        client6 = Client("c6", 3000)
        client7 = Client("c7")
        client8 = Client("c8", 1200)
        client9 = Client("c09", 1200)
        client10 = Client("c10")
        client11 = Client("c11", 2000)
        client12 = Client("c12", 1300)
        client13 = Client("c13")
        client14 = Client("c14", 1100)
        client15 = Client("c15", 3000)
        client16 = Client("c16", 3000)

        printer1 = Printer("P1", "143.453.23.45", 500)
        printer2 = Printer("P2", "145.453.23.45", 300)
        printer3 = Printer("P3", "145.453.23.45", 200)

        server_1.bind([client1, client4, client8, client12, printer1])
        server_2.bind([client9, printer2])
        server_3.bind([client14, printer3])

        network1 = Network("IPI Network")
        network1.add_server(server_1)
        network1.add_server(server_2)
        network1.add_server(server_3)
        """network1.add_server(server_4)""" #Pour raise une erreur

        db_path = "NetworkDB1.db"
        if os.path.exists(db_path):
            os.remove(db_path)
        create_database(network1)
        
        view = networkView([network1])
        print(view)
        view.graph()
    except Exception as e:
        print("\t", str(e))