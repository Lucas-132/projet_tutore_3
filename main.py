from networkClasses import *

if __name__ == "__main__":
  server_1 = Server("S1")
  server_2 = Server("S2", 10000)
  server_3 = Server("S3", 7000)
  
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

  server_1.bind([client1, client4, client5, client10])
  server_2.bind([client2])
  server_3.bind([client3])

  network = Network()
  network.add_server(server_1)
  network.add_server(server_2)
  network.add_server(server_3)

  print(network.port_entree)
  print(network.port_sortie)

  network.delete_server(server_1)

  print(network.port_entree)
  print(network.port_sortie)