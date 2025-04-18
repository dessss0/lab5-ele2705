# This client is a demo only. The real client is on the device

import socket
import json
import argparse

from commands.command_factory import get_command
from utils.choose_command import choose_command
from utils.create_response import create_response
from utils.echo_reply import echo_reply
from utils.init_board import initialize_board

import Adafruit_BBIO.GPIO as GPIO

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--device", help="Client device. Will indicate which config file to use", default="bb")
args = parser.parse_args()

with open(f"experiments/{args.device}_config.json") as config_file:
	config = json.load(config_file)


# Consigne 1 : Dans le fichier experiments/bb_config, mettez l'adresse IP dans la variable "host" et le port dans la variable "port".
# Ces informations seront communiquées avec vous pendant la séance.
HOST = config["host"]  # L'adresse IP du serveur
PORT = config["port"]  # Le port utilisé par le serveur

initialize_board(config)

# Consigne 2 : Ouvrez un socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with s:
    while True:

        # Écouter le bouton et lire le capteur
        command_str = choose_command(config)     
        command = get_command(command_str)
        response = command(config)
        data = create_response(response)

        # Consigne 3 : La variable data contient les données à envoyer. Envoyer ces données au serveur en utilisant la fonction sendto().
        # N'oubliez pas d'utiliser la fonction encode() pour envoyer les données en format binaire.
        s.sendto(data.encode(), (HOST, PORT))

        # Print server echo reply
        # Consigne 4 : recevez la réponse du serveur avec la fonction recvfrom(). Recevez 1024 bytes dans la fonction.
        # Indice : La fonction recvfrom() retourne deux valeurs : les données reçues et l'adresse IP + port de la source.
        reply, addr = s.recvfrom(1024)

        # Consigne 5 : Assurez vous que la source de la réponse est celle du serveur
        if adrr[0] == HOST and addr[1] == PORT:

             
        # Cette commande est pour afficher la réponse et pour allumer la LED
            echo_reply(reply, config)

print("Connection terminated.")
