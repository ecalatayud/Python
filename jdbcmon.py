#=======================================================
# Weblogic JDBC connections monitoring script
#=======================================================
connect("user","password","t3://IP:Port")
try:
 fp=open('/tmp/ActiveConn.log','a+')
 poolrtlist=adminHome.getMBeansByType('JDBCConnectionPoolRuntime')

 for poolRT in poolrtlist:
  pname = poolRT.getName()
  pmaxcapacity = poolRT.getAttribute("MaxCapacity")
  paccc = poolRT.getAttribute("ActiveConnectionsCurrentCount")
  server= str(poolRT).split(',')[2].split('=')[1]
  pstate = poolRT.getAttribute("State")
  print>>fp, '%15s %10s %7d %7d %10s' % (server,pname,pmaxcapacity,paccc,pstate)
  print ' '
except:
  print 'Error:'
  dumpStack()
  pass
disconnect()

