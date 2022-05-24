#Librería
import cv2  # clase estatica
import numpy as np # clase dinamica por as np



bgr=np.zeros((200,800,3),dtype=np.uint8) #metodos de entrada np(que llama a la clase dinamica de numpy).zeros metodo de entrada
#np.zeros((de shape, 200 en altura, 800 en ancho , 3 en tres valores donde se va a agregar el color ))
#uint8 es un entero de 8 bits sin signo que puede representar valores 0..255


"""
    Inicialización del arreglo con ceros con np.zeros()
Numpy dispone de una función con la que se pueden crear arrays de un tamaño dado inicializados con ceros.
 Esta función es np.zeros() y tiene la siguiente forma:
        --------------> np.zeros(shape, dtype=float, order='C') <--------------   
donde
shape: son las dimensiones del array Numpy que se desea construir.
         *Si es un escalar creará un vector, mientras si se indica una tupla se obtendrá una matriz.
dtype: es un parámetro opcional en el que se indica el tipo de dato.
         *Por defecto se utiliza el tipo de dato float.
order: es un parámetro opcional con el que se indica como se llenarán las matrices: 
         F primero las filas o C primero las columnas. Siendo el valor por defecto C.
"""


bgr[:,:,:]=(200,200,120) #brg[:,:,:]=(*del rgb dispuesto en las tres partes de color 255,255,255)
bgr[120,:,:]=(0,0,255) #brg[x,:,:]=(*del rgb dispuesto en las tres partes de color) da una linea horizontal
bgr[:,120,:]=(0,0,255)#brg[:,y,:]=(*del rgb dispuesto en las tres partes de color) da una linea vertical
#bgr[250,250,:]=(0,0,255) # brg[posicionx,posiciony,dondeagregacolor] da un pixel 
cv2.imshow('BGR',bgr)  #metodo imshow # Usando el método cv2.imshow() permite la visualización de la imagen
# ('nombre de la ventana',parametro-variable en donde se muestra)

cv2.waitKey(0) ##espera a que el usuario presione cualquier tecla #(esto es necesario para evitar que el kernel de Python se cuelgue). El 0 evita que la pantalla se cierre
cv2.destroyAllWindows() # metodo.finaliza el proceso y cierra todas las ventanas abiertas 