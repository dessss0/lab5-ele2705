import socket


# Consigne 1 : Ajoutez les informations suivantes
# LISTEN_ADDRESS est l'adresse de l'interface qui écoute des paquets, et LISTEN_PORT et le port associé avec lui
# CONNECT_ADDRESS est l'adresse du destinataire, et CONNECT_PORT est le port destinataire
LISTEN_ADDRESS    = _
LISTEN_PORT       = _
CONNECT_ADDRESS   = _
CONNECT_PORT      = _


def forward(listenaddress, listenport, connectaddress, connectport):

    # private_socket est le socket entre le microprocesseur et votre machine
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as private_socket:
        private_socket.bind((listenaddress, listenport))
        while True:

            data, client_addr = private_socket.recvfrom(1024)

            # public_socket est le socket entre votre machine et le serveur
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as public_socket:
                public_socket.sendto(data, (connectaddress, connectport))
                response, server_addr = public_socket.recvfrom(1024)
            private_socket.sendto(response, client_addr)

if __name__ == "__main__":

    forward(LISTEN_ADDRESS, LISTEN_PORT, CONNECT_ADDRESS, CONNECT_PORT)
