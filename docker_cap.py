#!/usr/bin/env python3.6

import subprocess
import docker 

def listar():
    client = docker.from_env()
    get_all = client.containers.list(all)

    for cada_conteiner in get_all:
        conectando = client.containers.get(cada_conteiner.id)
        print("Container: %s imagem: %s comando: %s"%(conectando.short_id, conectando.attrs['Config']['Image'],conectando.attrs['Config']['Cmd']))

def criar(imagem,comando):
    client = docker.from_env()
    executando = client.containers.run(imagem,comando)
    print(executando)

#def procurar()

listar()        