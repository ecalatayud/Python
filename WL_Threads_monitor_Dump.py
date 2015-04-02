""" Script para la monitorizacion de threads de servidores weblogic """
""" se genera un fichero csv para cada uno de los servidores con el número de cada tipo de threads """
""" Si algun servidor tiene mas de 20 en estado hogging genera un dump del server y lo envía por correo """

from time import localtime, strftime
import os

connect('user','passwd','t3://ip_admin_weblogic:puerto')

ThreadsHoggingToDump = 20

domainConfig()
servers=cmo.getServers()
for server in servers:
        domainRuntime()
        print server.getName()
        path = "/ServerRuntimes/" + server.getName() + "/ThreadPoolRuntime/ThreadPoolRuntime/"
        cd (path)
        now = strftime("%H:%M:%S")
        totalThreads = cmo.getExecuteThreadTotalCount()
        idleThrds = cmo.getExecuteThreadIdleCount()
        hoggingThreads = cmo.getHoggingThreadCount()
        csvName = "directorio de CSV" + server.getName() + "_Thread_Count.csv"
        fileCsv = open(csvName, "a")
        print >>fileCsv, now + ";" + str(totalThreads) + ";" + str(idleThrds) + ";" + str(hoggingThreads)
        fileCsv.close()
        if hoggingThreads >= ThreadsHoggingToDump:
                serverConfig()
                cd ('Servers/'+ server.getName())
                threadDump(serverName=server.getName())
                dumpFileName = 'Thread_Dump_' + server.getName() + '.txt'
                sendMail = "/usr/bin/uuencode " + dumpFileName + " " + dumpFileName + "| /usr/bin/mailx -s\"Weblogic con hogging threads >= 20\" correo_alarmas@dominio.com"
                os.system(sendMail)
