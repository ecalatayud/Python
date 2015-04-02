
""" Script para actualizar los wars de una subida de nuevo software """


from os import walk, listdir, remove, path
from fnmatch import filter
from shutil import copy, copyfile, move, rmtree
import zipfile



dir_subidas=("/dir_app/app1", "/dir_app/app2")
dir_new_fich="/dir/wars/to/update/"
listado_wars = []


""" Creamos listado de  los nuevos wars """
for war in listdir(dir_new_fich):
        if war.endswith(".war"):
                listado_wars.append(war)

if not listado_wars:
        print "No hay wars para subir"

for war in listado_wars:
        nuevo_war = 0
        dir_war = war.split("-")[0]
        if dir_war == "esmt":
                dir_war = dir_war + "-" + war.split("-")[1]
				
""" Excepción para war con "-" antes del nombre """

                if dir_war != "nombre-war":
                        dir_war = war.split("-")[0]
        print dir_war
        for dir in dir_subidas:
                directorio = str(dir) + "/" + str(dir_war) + ".war"
                if path.exists(directorio):
                        print "Procedemos a borrar " + directorio
                        rmtree(directorio)
                        print "Descomprimimos " + war + " en la ruta " + directorio
                        print ""
                        zip_war = zipfile.ZipFile(dir_new_fich + "/" + war, "r")
                        zip_war.extractall(directorio)
                else:
                        nuevo_war = nuevo_war + 1
        if nuevo_war == 2:
                print "No hay desplegada version anterior de war, es nuevo o ha habido algun error."
                print ""

