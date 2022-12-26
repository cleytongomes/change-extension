import os
import shutil
import configparser

# Config Parser
cfg = configparser.ConfigParser()
cfg.read('config.ini')

# Paths de origem e destino
origem = cfg["Paths"]["origem"]
destino = cfg["Paths"]["destino"]

# Nova Extensão
extensao = cfg["Extensao"]["default"]

# Varre os arquivos na pasta
for arquivo in os.listdir(origem):

    # Nome novo com a extensão nova
    novo_arquivo = arquivo.split(".")[0] + extensao

    # Copia o arquivo
    shutil.copyfile( os.path.join(origem,arquivo), os.path.join(destino,novo_arquivo))


print("Arquivos copiados")