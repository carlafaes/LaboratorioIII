archivo=open('prueba.txt', 'r',encoding='utf-8')#r es de read, a es de append, w es de write, x crea un archivo,t especifica el tipo de archivo (texto o text), b tipo de archivo binario, w+ se utiliza para leer y tambien escribir informacion,r+ para escribir y leer informacion
#print(archivo.read())
#print(archivo.read(5))#muestra las 5 primeras letras de la primer palabra
print(archivo.readline())# lee la linea completa