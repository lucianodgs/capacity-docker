#!/usr/bin/env python3.6

import subprocess
import docker 

def connectar():
    #client = docker.from_env()
    #client = docker.DockerClient(base_url='tcp://192.168.187.135:2375')
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')  
    return(client)  

def listar():
    client = connectar()
    get_all = client.containers.list(all)

    for cada_conteiner in get_all:
        conectando = client.containers.get(cada_conteiner.id)
        print("Container: %s imagem: %s comando: %s status %s"%(conectando.short_id, conectando.attrs['Config']['Image'],conectando.attrs['Config']['Cmd'],conectando.attrs['State']['Status']))

def criar(imagem,comando):
    client = connectar()
    executando = client.containers.run(imagem,comando)
    print(executando)

def procurar(busca):
    client = connectar()
    get_all = client.containers.list(all)
    for cada_container in get_all:
        conectando = client.containers.get(cada_container.id)
        imagem_container = conectando.attrs['Config']['Image']
        if str(busca).lower() in str(imagem_container).lower():

            print("Conteiner: %s |Busca: %s |nome:%s" %(cada_container.short_id,busca, imagem_container))



#procurar("hello")        
listar()