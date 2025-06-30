from networkClasses import *

if __name__ == "__main__":
  server_1 = Server("S1")
  server_2 = Server("S2", 10000)
  server_3 = Server("S3", 7000)
  
  client1 = Client("c1")
  client2 = Client("c2", 2000)
  client3 = Client("c3", 3000)

  print(server_1.nom, server_1.prix, server_1.client)

  server_1.bind(client1)

  print(server_1.nom, server_1.prix, server_1.client)
