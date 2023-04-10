#declaramos una variable
try:
    archivo=open('prueba.txt','w')#la w es de write
except Exception as e:
    print(e)
finally:
    archivo.close()#Con esto se debe cerrar el archivo