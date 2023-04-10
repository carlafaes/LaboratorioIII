#declaramos una variable
try:
    archivo=open('prueba.txt','w')#la w es de write
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally:
    archivo.close()#Con esto se debe cerrar el archivo