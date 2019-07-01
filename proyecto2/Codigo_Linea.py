from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox





class Interfaz:

    def __init__(self):
        self.v = Tk()
        self.ancho = self.v.winfo_width()
        self.alto = self.v.winfo_height()
        self.v.title('Redes II - Proyecto 2: Codigos de Linea')
        self.v.geometry('500x500')
        self.initComponents()
    #Muestra la venta
    def show(self):
        self.v.mainloop()

    #Inicializa los componentes de la interfaz grafica
    def initComponents(self):
        self.v.grid_columnconfigure(1, weight = 1)
        self.titulo = Label(self.v, text= 'Codigos de linea')
        self.titulo.grid(row = 0, column = 0 , columnspan = 2, pady = (10,10))
        self.lb2 = Label(self.v, text= 'Ingrese la cadena binaria:')
        self.lb2.grid(row = 1, column = 0,padx = (30,10), pady =(5,5))
        self.binario = StringVar()
        self.txt = Entry(self.v, textvariable = self.binario)
        self.txt.configure(width = 25)
        self.txt.grid(row = 1, column = 1, padx = (10,10), pady = (5,5))
        self.lb3 = Label(self.v, text = 'Codigo de linea')
        self.lb3.grid(row = 2, column = 0, padx =(30,10), pady = (5,5))
        self.comboLineas = ttk.Combobox(self.v, state = 'readonly')
        self.comboLineas['values'] = ['NRZ','RZ','AMI','ADI','B3ZS(+v)','B3ZS(-v)','HDB3(+v)','HDB3(-v)','B6ZS(+v)','B6ZS(-v)','Manchester','CMI']
        self.comboLineas.configure(width = 22)
        self.comboLineas.grid(row = 2, column = 1, padx = (10,10), pady =(5,5))
        self.comboLineas.bind("<<ComboboxSelected>>", self.selecciona)
        self.addMenu()
        

    #Añade el menu a la interfaz grafica
    def addMenu(self):
        self.barra = Menu(self.v)
        self.barra.add_command(label = 'Salir',command = self.v.destroy)
        self.barra.add_command(label = 'Miembros del Grupo', command = self.mostrarI)
        self.v.config(menu = self.barra)
        
    #Convierte la cadena en una lista de enteros
    def lista_cadena(self, lista):
        lista_nueva = []
        for i in range(len(lista)):
            lista_nueva.append(list(lista[i]))
        
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                lista_nueva[i][j] = int(lista[i][j])
        
        return lista_nueva
    
    #Funcion que imprime los ciclos de reloj 
    def reloj(self, cadena):
        X1 = []
        Y1 = []
        coor = []
        X1.append(-0.5)
        X1.append(0)
        Y1.append(3)
        Y1.append(3)
        for i in range(len(cadena)):
            X1.append(i)
            X1.append(i+0.5)
            X1.append(i+0.5)
            X1.append(i+0.5)
            X1.append(i+0.5)
            X1.append(i+1)
            Y1.append(3.5)
            Y1.append(3.5)
            Y1.append(3.5)
            Y1.append(2.5)
            Y1.append(2.5)
            Y1.append(2.5)
            if i == len(cadena)-1:
                X1.append(i+1)
                X1.append(i+1.5)
                Y1.append(3)
                Y1.append(3)
        coor.append(X1)
        coor.append(Y1)
        return coor
        

    #Funcion que realiza la conversion al codigo de linea b3zs                
    def b3zs(self, cadena, ult_violacion):
        #Se recibe una lista por lo tanto se debe unir a cadena
        codigo = ''.join(str(e) for e in cadena)
       
        #Coordenadas de la grafica
        X = []
        Y = []
        #Arreglo de envio 
        Coor = []
        #Expresion regular que identifica 3 ceros
        tres_0 = re.compile('000')
        #Lista de las cadenas anteriores a 3 ceros consecutivos
        lista_anteriores = re.split('000', codigo)
        #Lista de los 3 ceros a reemplazar
        l30 = tres_0.findall(codigo)
        
        for i in range(len(l30)):
            if ult_violacion == 1:
                num_b = 1
            else: 
                num_b = 0
            #Obtiene la cadena anterior a cada 3 ceros consecutivos
            binario = lista_anteriores[i]
            for j in range(len(binario)): 
                #Cuenta el numero de pulsos que respetan la regla AMI
                if int(binario[j]) == 1:
                    num_b +=1
            #Si el numero de B es par
            if num_b % 2 == 0:
                #Violacion positiva 
                if ult_violacion == 1:
                    l30[i] = [-1,0,-1]
                    ult_violacion = -1
                   
                #Violacion negativa
                else:
                    l30[i] = [1,0,+1] 
                    ult_violacion = 1
                    
            #Si el numero B es impar            
            else: 
                #Violacion positiva
                if ult_violacion == 1:
                    l30[i] = [0,0,-1]
                    ult_violacion = -1
                   
                #Violacion negativa     
                else:
                    l30[i] = [0,0,+1]
                    ult_violacion = 1
                    
        
        lista_anteriores = self.lista_cadena(lista_anteriores)
        #Maneja el cambio de polaridad de los 1
        polaridad = 1
        j = 0
        #Impresion anterior del codigo de linea
        X.append(-0.5)
        X.append(0)
        Y.append(0)
        Y.append(0)
        for i in range(len(lista_anteriores)):
            #Impresion de las cadenas que no fueron sustituidas
            #Estas respetan el codigo AMI 
            for n in range(len(lista_anteriores[i])):
                if lista_anteriores[i][n] == 1: 
                    if polaridad == 1:
                        X.append(j)
                        X.append(j+0.5)
                        X.append(j+0.5)
                        X.append(j+1)
                        Y.append(1)
                        Y.append(1)
                        Y.append(0)
                        Y.append(0)
                        polaridad = -1
                        
                    else:
                        X.append(j)
                        X.append(j+0.5)
                        X.append(j+0.5)
                        X.append(j+1)
                        Y.append(-1)
                        Y.append(-1)
                        Y.append(0)
                        Y.append(0)
                        polaridad = 1 
                      
                else:
                    X.append(j)
                    X.append(j+1)
                    Y.append(0)
                    Y.append(0)
                j+= 1
               
        
            #Impresion de las sustituciones de B3ZS
            #Estas no siguen el patron AMI
            if (i < len(l30)):
                for k in range(len(l30[i])): 
                    if l30[i][k] == 1:
                        X.append(j)
                        X.append(j+0.5)
                        X.append(j+0.5)
                        X.append(j+1)
                        Y.append(1)
                        Y.append(1)
                        Y.append(0)
                        Y.append(0)
                        
                    elif l30[i][k] == -1:
                        X.append(j)
                        X.append(j+0.5)
                        X.append(j+0.5)
                        X.append(j+1)
                        Y.append(-1)
                        Y.append(-1)
                        Y.append(0)
                        Y.append(0)
                        
                    else: 
                        X.append(j)
                        X.append(j+1)
                        Y.append(0)
                        Y.append(0) 
                    j+= 1
            

                     
        Coor.append(X)
        Coor.append(Y)
        return Coor    

    #Funcion que realiza la conversion al codigo de linea b6zs
    def b6zs(self, cadena, ult_violacion):
            #Se recibe una lista por lo tanto se debe unir a cadena
            codigo = ''.join(str(e) for e in cadena)

            #Coordenadas de la grafica
            X = []
            Y = []
            #Arreglo de envio 
            Coor = []
            #Expresion regular que identifica 6 ceros
            seis_0 = re.compile('000000')
            #Lista de las cadenas anteriores a 6 ceros consecutivos
            lista_anteriores = re.split('000000', codigo)
            #Lista de los 6 ceros a reemplazar
            l30 = seis_0.findall(codigo)

            for i in range(len(l30)):
                if ult_violacion == 1:
                    num_b = 1
                else: 
                    num_b = 0
                #Obtiene la cadena anterior a cada 6 ceros consecutivos
                binario = lista_anteriores[i]
                for j in range(len(binario)): 
                    #Cuenta el numero de pulsos que respetan la regla AMI
                    if int(binario[j]) == 1:
                        num_b +=1
                #Si el numero de B es par
                if num_b % 2 == 0:
                    #Violacion positiva 
                    if ult_violacion == 1:
                        l30[i] = [0,1,-1,0,-1,1]
                        ult_violacion = -1

                    #Violacion negativa
                    else:
                        l30[i] = [0,-1,1,0,1,-1] 
                        ult_violacion = 1

                #Si el numero B es impar            
                else: 
                    #Violacion positiva
                    if ult_violacion == 1:
                        l30[i] = [0,1,-1,0,-1,1]
                        ult_violacion = -1

                    #Violacion negativa     
                    else:
                        l30[i] = [0,-1,1,0,1,-1] 
                        ult_violacion = 1


            lista_anteriores = self.lista_cadena(lista_anteriores)
            #Maneja el cambio de polaridad de los 1
            polaridad = 1
            j = 0
            #Impresion anterior del codigo de linea
            X.append(-0.5)
            X.append(0)
            Y.append(0)
            Y.append(0)
            for i in range(len(lista_anteriores)):
                #Impresion de las cadenas que no fueron sustituidas
                #Estas respetan el codigo AMI 
                for n in range(len(lista_anteriores[i])):
                    if lista_anteriores[i][n] == 1: 
                        if polaridad == 1:
                            X.append(j)
                            X.append(j+0.5)
                            X.append(j+0.5)
                            X.append(j+1)
                            Y.append(1)
                            Y.append(1)
                            Y.append(0)
                            Y.append(0)
                            polaridad = -1

                        else:
                            X.append(j)
                            X.append(j+0.5)
                            X.append(j+0.5)
                            X.append(j+1)
                            Y.append(-1)
                            Y.append(-1)
                            Y.append(0)
                            Y.append(0)
                            polaridad = 1 

                    else:
                        X.append(j)
                        X.append(j+1)
                        Y.append(0)
                        Y.append(0)
                    j+= 1

                #Impresion de las sustituciones de B6ZS
                #Estas no siguen el patron AMI
                if (i < len(l30)):
                    for k in range(len(l30[i])): 
                        if l30[i][k] == 1:
                            X.append(j)
                            X.append(j+0.5)
                            X.append(j+0.5)
                            X.append(j+1)
                            Y.append(1)
                            Y.append(1)
                            Y.append(0)
                            Y.append(0)

                        elif l30[i][k] == -1:
                            X.append(j)
                            X.append(j+0.5)
                            X.append(j+0.5)
                            X.append(j+1)
                            Y.append(-1)
                            Y.append(-1)
                            Y.append(0)
                            Y.append(0)

                        else: 
                            X.append(j)
                            X.append(j+1)
                            Y.append(0)
                            Y.append(0) 
                        j+= 1
               

            Coor.append(X)
            Coor.append(Y)
            return Coor    
    
    #Funcion que realiza la conversion al codigo de linea hdb3
    def hdb3(self, cadena, ult_violacion):
        #Se recibe una lista por lo tanto se debe unir a cadena
        codigo = ''.join(str(e) for e in cadena)
       
        #Coordenadas de la grafica
        X = []
        Y = []
        #Arreglo de envio 
        Coor = []
        #Expresion regular que identifica 3 ceros
        cuatro_0 = re.compile('0000')
        #Lista de las cadenas anteriores a 3 ceros consecutivos
        lista_anteriores = re.split('0000', codigo)
        #Lista de los 3 ceros a reemplazar
        l30 = cuatro_0.findall(codigo)
        
        for i in range(len(l30)):
            if ult_violacion == 1:
                num_b = 1
            else: 
                num_b = 0
            #Obtiene la cadena anterior a cada 3 ceros consecutivos
            binario = lista_anteriores[i]
            for j in range(len(binario)): 
                #Cuenta el numero de pulsos que respetan la regla AMI
                if int(binario[j]) == 1:
                    num_b +=1
            #Si el numero de B es par
            if num_b % 2 == 0:
                #Violacion positiva 
                if ult_violacion == 1:
                    l30[i] = [-1,0,0,-1]
                    ult_violacion = -1
                   
                #Violacion negativa
                else:
                    l30[i] = [1,0,0,1] 
                    ult_violacion = 1
                    
            #Si el numero B es impar            
            else: 
                #Violacion positiva
                if ult_violacion == 1:
                    l30[i] = [0,0,0,1]
                    ult_violacion = -1
                   
                #Violacion negativa     
                else:
                    l30[i] = [0,0,0,-1]
                    ult_violacion = 1
                    
        
        lista_anteriores = self.lista_cadena(lista_anteriores)
        #Maneja el cambio de polaridad de los 1
        polaridad = 1
        j = 0
        #Impresion anterior del codigo de linea
        X.append(-0.5)
        X.append(0)
        Y.append(0)
        Y.append(0)
        for i in range(len(lista_anteriores)):
            #Impresion de las cadenas que no fueron sustituidas
            #Estas respetan el codigo AMI 
            for n in range(len(lista_anteriores[i])):
                if lista_anteriores[i][n] == 1: 
                    if polaridad == 1:
                        X.append(j)
                        X.append(j+0.5)
                        X.append(j+0.5)
                        X.append(j+1)
                        Y.append(1)
                        Y.append(1)
                        Y.append(0)
                        Y.append(0)
                        polaridad = -1
                        
                    else:
                        X.append(j)
                        X.append(j+0.5)
                        X.append(j+0.5)
                        X.append(j+1)
                        Y.append(-1)
                        Y.append(-1)
                        Y.append(0)
                        Y.append(0)
                        polaridad = 1 
                      
                else:
                    X.append(j)
                    X.append(j+1)
                    Y.append(0)
                    Y.append(0)
                j+= 1
        
            #Impresion de las sustituciones de B3ZS
            #Estas no siguen el patron AMI
            if (i < len(l30)):
                for k in range(len(l30[i])): 
                    if l30[i][k] == 1:
                        X.append(j)
                        X.append(j+0.5)
                        X.append(j+0.5)
                        X.append(j+1)
                        Y.append(1)
                        Y.append(1)
                        Y.append(0)
                        Y.append(0)
                        
                    elif l30[i][k] == -1:
                        X.append(j)
                        X.append(j+0.5)
                        X.append(j+0.5)
                        X.append(j+1)
                        Y.append(-1)
                        Y.append(-1)
                        Y.append(0)
                        Y.append(0)
                        
                    else: 
                        X.append(j)
                        X.append(j+1)
                        Y.append(0)
                        Y.append(0) 
                    j+= 1
                 
        Coor.append(X)
        Coor.append(Y)
        return Coor      

    #Funcion que realiza la conversion al codigo de linea NRZ
    def NRZ(self, cadena):
        for i in range(len(cadena)):
                self.X.append(i)
                self.X.append(i+1)
                self.Y.append(cadena[i])
                self.Y.append(cadena[i])
                #Imprime la terminacion del codigo de linea
                if i == len(cadena)-1:
                    self.X.append(i+1)
                    self.X.append(i+1.5)
                    self.Y.append(0)
                    self.Y.append(0)
     
    #Funcion que realiza la conversion al codigo de linea RZ
    def RZ(self, cadena):
         for i in range(len(cadena)):
                if cadena[i] == 1:
                    self.X.append(i)
                    self.X.append(i+0.5)
                    self.X.append(i+0.5)
                    self.X.append(i+1)
                    self.Y.append(1)
                    self.Y.append(1)
                    self.Y.append(0)
                    self.Y.append(0)
                else:
                    self.X.append(i)
                    self.X.append(i+1)
                    self.Y.append(0)
                    self.Y.append(0)
                #Imprime la terminacion del codigo de linea
                if i == len(cadena)-1:
                    self.X.append(i+1)
                    self.X.append(i+1.5)
                    self.Y.append(0)
                    self.Y.append(0)
    
    #Funcion que realiza la conversion al codigo de linea AMI
    def AMI(self, cadena):
        polaridad = 1
        for i in range(len(cadena)):
            if cadena[i] == 1: 
                if polaridad == 1:
                    self.X.append(i)
                    self.X.append(i+0.5)
                    self.X.append(i+0.5)
                    self.X.append(i+1)
                    self.Y.append(1)
                    self.Y.append(1)
                    self.Y.append(0)
                    self.Y.append(0)
                    polaridad = -1
                else:
                    self.X.append(i)
                    self.X.append(i+0.5)
                    self.X.append(i+0.5)
                    self.X.append(i+1)
                    self.Y.append(-1)
                    self.Y.append(-1)
                    self.Y.append(0)
                    self.Y.append(0)
                    polaridad = 1 
            else:
                self.X.append(i)
                self.X.append(i+1)
                self.Y.append(0)
                self.Y.append(0) 
            #Imprime la terminacion del codigo de linea
            if i == len(cadena)-1:
                    self.X.append(i+1)
                    self.X.append(i+1.5)
                    self.Y.append(0)
                    self.Y.append(0)        
    
    #Funcion que realiza la conversion al codigo de linea ADI
    def ADI(self, cadena):
         for i in range(len(cadena)):
                if i % 2 != 0: 
                    if (cadena[i] == 1):
                        self.X.append(i)
                        self.X.append(i+1)
                        self.Y.append(0)
                        self.Y.append(0)
                    else:
                        self.X.append(i)
                        self.X.append(i+1)
                        self.Y.append(1)
                        self.Y.append(1) 
                else:
                    self.X.append(i)
                    self.X.append(i+1)
                    self.Y.append(cadena[i])
                    self.Y.append(cadena[i])
                #Imprime la terminacion del codigo de linea
                if i == len(cadena)-1:
                    self.X.append(i+1)
                    self.X.append(i+1.5)
                    self.Y.append(0)
                    self.Y.append(0) 
    
    #Funcion que realiza la conversion al codigo de linea CMI
    def CMI(self, cadena):
        polaridad = 1
        for i in range(len(cadena)):
            if cadena[i] == 1: 
                if polaridad == 1:
                    self.X.append(i)
                    self.X.append(i+1)
                    self.X.append(i+1)
                    self.X.append(i+1)
                    self.Y.append(1)
                    self.Y.append(1)
                    self.Y.append(0)
                    self.Y.append(0)
                    polaridad = -1
                else:
                    self.X.append(i)
                    self.X.append(i+1)
                    self.X.append(i+1)
                    self.X.append(i+1)
                    self.Y.append(-1)
                    self.Y.append(-1)
                    #Si el siguiente elemento es un 0 
                    # y la polaridad es negativa entonces se mantiene 
                    # la coordenada en -1
                    if (i+1 < len(cadena) and cadena[i+1] == 0 and polaridad == -1):
                        self.Y.append(-1)
                        self.Y.append(-1)
                    else:
                        self.Y.append(0)
                        self.Y.append(0)
                    polaridad = 1 
            else:
                self.X.append(i)
                self.X.append(i+0.5)
                self.X.append(i+0.5)
                self.X.append(i+0.5)
                self.X.append(i+0.5)
                self.X.append(i+1)
                self.Y.append(-1)
                self.Y.append(-1) 
                self.Y.append(0)
                self.Y.append(0)
                self.Y.append(1)
                self.Y.append(1)
            #Imprime la terminacion del codigo de linea
            if i == len(cadena)-1:
                    self.X.append(i+1)
                    self.X.append(i+1.5)
                    self.Y.append(0)
                    self.Y.append(0)

    #Funcion que realiza la conversion al codigo de linea Manchester
    def Manchester(self, cadena):
        for i in range(len(cadena)):
                if cadena[i] == 1:
                    self.X.append(i)
                    self.X.append(i+0.5)
                    self.X.append(i+0.5)
                    self.X.append(i+1)
                    self.Y.append(1)
                    self.Y.append(1)
                    self.Y.append(-1)
                    self.Y.append(-1)
                else:
                    self.X.append(i)
                    self.X.append(i+0.5)
                    self.X.append(i+0.5)
                    self.X.append(i+0.5)
                    self.X.append(i+0.5)
                    self.X.append(i+1)
                    self.Y.append(-1)
                    self.Y.append(-1) 
                    self.Y.append(0)
                    self.Y.append(0)
                    self.Y.append(1)
                    self.Y.append(1)
                #Imprime la terminacion del codigo de linea
                if i == len(cadena)-1:
                    self.X.append(i+1)
                    self.X.append(i+1.5)
                    self.Y.append(0)
                    self.Y.append(0)
    
    def crearGrafico(self,val,cod):
        self.X = []
        self.Y = []

        f = Figure(figsize=(4,3),dpi = 100)
        a = f.add_subplot(111)
     
        reloj = self.reloj(cod)
        #Impresion antes del codigo de linea
        self.X.append(-0.5)
        self.X.append(0)
        self.Y.append(0)
        self.Y.append(0)
        if val == 'NRZ':
            self.NRZ(cod)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(self.X,self.Y, color = 'r', label = 'NRZ')
            a.legend(loc = 'right')
        if val == 'RZ':
            self.RZ(cod)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(self.X,self.Y, color = 'r', label = 'RZ')
            a.legend(loc = 'right')
        if val == 'AMI':
            self.AMI(cod)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(self.X,self.Y, color = 'r', label = 'AMI')
            a.legend(loc = 'right')
        if val == 'ADI':
            self.ADI(cod)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(self.X,self.Y, color = 'r', label = 'ADI')
            a.legend(loc = 'right')

        if val == 'CMI':
            self.CMI(cod)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(self.X,self.Y, color = 'r', label = 'CMI')
            

        if val=='Manchester':
            self.Manchester(cod)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(self.X,self.Y, color = 'r', label = 'Manchester')
            

        if val == 'B3ZS(+v)':
            C = self.b3zs(cod,1)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(C[0],C[1], color = 'r', label = 'B3ZS')
            a.legend(loc = 'right')
        
        if val == 'B3ZS(-v)':
            C = self.b3zs(cod,-1)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(C[0],C[1], color = 'r', label = 'B3ZS')
            a.legend(loc = 'right')
            
        if val == 'B6ZS(+v)':
            C = self.b6zs(cod,1)
            a.plot(reloj[0], reloj[1], color = 'b',label = 'Reloj')
            a.plot(C[0],C[1], color = 'r', label = 'B6ZS')
            a.legend(loc = 'right')
        
        if val == 'B6ZS(-v)':
            C = self.b6zs(cod,-1)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(C[0],C[1], color = 'r', label = 'B6ZS') 
            a.legend(loc = 'right')
            
        if val == 'HDB3(+v)':
            C = self.hdb3(cod,1)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(C[0],C[1], color = 'r', label = 'HDB3')
            a.legend(loc = 'right')
        
        if val == 'HDB3(-v)':
            C = self.hdb3(cod,-1)
            a.plot(reloj[0], reloj[1], color = 'b', label = 'Reloj')
            a.plot(C[0],C[1], color = 'r', label = 'HDB3')
            a.legend(loc = 'right')    
                 
        canvas = FigureCanvasTkAgg(f,master = self.v)
        canvas.get_tk_widget().grid(row = 3, column = 0, columnspan = 2,pady = (40,40))

    
        
    #Funcion que maneja el evento del combobox
    def selecciona(self, event):
        validos = (0,1)
        cod = []
        val = self.comboLineas.get()
        aux = self.txt.get()
        aux = list(aux)
        for i in range(len(aux)):
            cod.append(int(aux[i]))
            if cod[i] not in validos:

                messagebox.showerror(message="Cadena de bits invalida", title="Error")
                self.txt.delete(0, END)
                self.comboLineas.set('')
                self.txt.focus()
                error= True

                val= 'empty'
                cod=[]
                break
        self.crearGrafico(val,cod)

    #Funcion que muestra la informacion de los estudiantes
    def mostrarI(self):
        nombres = ['Rony Rodriguez', 'Chrsithoper Portillo', 'Cinthya Cabrera', 'Hesler Gamez']
        #num_cuenta = ['20151031518','2015100','20161003851','20151003836']
        self.acerca = Toplevel()
        self.acerca.geometry('250x250')
        self.acerca.configure(bg = '#2980b9')
        self.frame = Frame(self.acerca)
        ancho_a = self.acerca.winfo_screenwidth()
        alto_a = self.acerca.winfo_screenheight()
        self.frame.configure(width = 240 , height = 240, bg= '#ecf0f1')
        self.frame.grid(row = 0, column = 0, padx = (ancho_a*0.02, ancho_a*0.02), pady = (alto_a*0.05,alto_a*0.05))
        #self.titulo = Label(self.frame,text = 'Integrantes')
        self.titulo.grid(row = 0, column = 0, columnspan = 2)

        i = 0
        for n in nombres:
            self.lbN = Label(self.frame, text = n)
            self.lbN.grid(row = i +1, column = 0, padx = (5,5), pady = (2,2))
            i += 1
        i = 0
        for num in num_cuenta:
            self.lbNum = Label(self.frame, text = num)
            self.lbNum.grid(row = i+1, column = 1, padx = (5,5), pady = (2,2))
            i+=1
            
               

if __name__ == "__main__":
    v = Interfaz()

    v.show()

