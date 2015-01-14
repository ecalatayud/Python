from os import walk, listdir, remove
from fnmatch import filter
from shutil import copy, copyfile

jars_viejos_y_nuevos = {}
dir_subidas=["/software/final/destination/one", "/software/final/destination/two"]
dir_new_fich="/new/jars/location"

""" Search files in directory tree from part of the filename"""
def busca_fich(fichero, directorio):
        for root, dirnames, file in walk(directorio):
                for match in filter(file, fichero + "*"):
                        return root + "/" + match


""" Dictionary with the jar name without version as keys """
for jar in listdir(dir_new_fich):
        if jar.endswith(".jar"):
                jar_sin_ver=jar.split("-")[0]
                jars_viejos_y_nuevos[jar_sin_ver] = []

if not jars_viejos_y_nuevos:
        print "No hay jars para subir"

""" for each key we add the old jar version as their values """
for dir in dir_subidas:
        for jar_nuevo in jars_viejos_y_nuevos:
                        jars_viejos_y_nuevos[jar_nuevo].append(busca_fich(jar_nuevo, dir))


""" Deleting old jar versions and copy new ones on same location """
""" Except buzonesCore jar wich name can't change jar name"""
for key in jars_viejos_y_nuevos:
        if jars_viejos_y_nuevos[key] != [None, None]:
                for jar in jars_viejos_y_nuevos[key]:
                        if jar != None:
                                if key == "buzonesCore":
                                        print "Borramos " + str(jar)
                                        remove(jar)
                                        new_jar = busca_fich(key, dir_new_fich)
                                        print "Copiamos " + str(new_jar) + " en " + str(jar)
                                        copyfile(new_jar, jar)
                                else:
                                        print "Borramos " + str(jar)
                                        remove(jar)
                                        new_jar = busca_fich(key, dir_new_fich)
                                        new_dir = jar.rsplit("/",1)[0]
                                        print "Copiamos " + str(new_jar) + " en " + str(new_dir)
                                        copy(new_jar, new_dir)

        else:
                print ""
                print "No existen versiones anteriores de " + key
                print ""
