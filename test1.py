# 1. Implemente uma função recursiva que percorra um diretório especificado e liste todos os arquivos e subdiretórios nele contidos, em qualquer profundidade.

import os

def listar_direc(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        print(full_path)
        
        if os.path.isdir(full_path):
            listar_direc(full_path)


listar_direc("./direc")
