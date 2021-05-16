import socket
import struct
import configparser
import subprocess

class wakeonlan():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config/targets.ini')
        self.machines = self.config['machine']['machines'].split(',')        

    def wake(self, target):
        if target in self.machines:
            mac = self.config[target]['mac']
            
            proc = subprocess.Popen(['sudo','etherwake', mac])

            print(f"Acordando {target}, mac: {mac}")
            
        else:
            print("Maquina não reconhecida")