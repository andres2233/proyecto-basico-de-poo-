import heapq


productos = {'carne ': 10, 'celulares' : 20 , 'computador1': 100, 'computador2' : 200, 'computador2 ': 200 , 'carne':  10 }

def app():
    opciones()
    respuesta = int(input( 'que opciones quieres??? \n'))
    
    tru = True
    while tru :
        if respuesta == 1 :
            productos_stock = productos.items()
            print('los productos disponibles son : ', productos_stock)
            print('la cantidad de productos disponibles son :', len(productos) )
            print()
            producto_c = input(' quieres saber cual es el productos mas caro ?? \n')
            producto_caro = True
            while producto_caro : 
                if producto_c == 'si' : 
                    print( 'los productos mas caros son : ' , heapq.nlargest(3, productos, productos.get ) , '\n ') 
                    producto_caro = False
                    tru = False
                    app()

                else: 
                    print( 'saliendo a la central \n ')
              
                    app()
       
    
        elif respuesta == 2:

            ordenadores = { 'pc1 ' :200, 'pc2' : 230 , 'pc3' : 1800, 'pc1 ' : 200}
            portatil2 = {'Notepad++', 'Atom', 'Eclipse', 'NetBeans', 'PyCharm'}
            portatil1 = {'Notepad++', 'PyCharm', 'Visual Studio Code', 'IntelliJ IDEA'}
            pregunta = input('quieres saber que pcs tenemos en stock ??? \n ')
            tt = True
            while tt :

                if pregunta == 'si' : 
                    print('nuestros ordenadores son :',  len(ordenadores) ) 
                    diferencia = input ( 'quieres saber la diferencia entre los diferentes ordenadores ?? \n')
                    if diferencia == 'si': 
                        pc = portatil1.difference(portatil2)
                        pc2 = portatil2.difference(portatil1)
                        diferencia_total = pc.symmetric_difference(pc2)
                        print('la diferenci entre la pc1 y la pc2 son : ', pc)
                        print('la diferencia entre la pc2 y la pc1 son : ', pc2)
                        print('la diferencia completa es :', diferencia_total)


                    else: 
                        print(  'redirijiendp a la central' ) 
        elif respuesta == 3 : 
            nombre()
        elif respuesta == 4:
            escribir()
            tru = False



        else: 
            break 


        
def nombre ():
    nombre = input("cual es tu nombre?? \n ")
    print( 'tu nombre invertido es : ', nombre[::-1])

def opciones():
    print ('bienvenido a supermerdos live ')
    print('1 ) saber los productos')
    print('2) saber que computadores hay ')
    print('3 ) si quieres saber como seria tu nombre alreves  ')
    print('4) escribir un archivo ')
    

def escribir(): 
    with open('archivo.txt', 'w') as wr:
        texto = input( 'que quieres escribir ???')
        wr.write(texto)
app()