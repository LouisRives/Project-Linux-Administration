import psutil

disque_utilisation = psutil.disk_usage('/')
print(f"disque_total:%sGo"%(round((disque_utilisation.total / 2**30),2)))
print(f"disque_utilise:%sGo"%(round((disque_utilisation.used / 2**30),2)))
print(f"disque_libre:%sGo"%(round((disque_utilisation.free / 2**30),2)))

