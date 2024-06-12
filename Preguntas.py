#----importaciones----#
import random
#---------------------------------------------------------------------------------------------------#
#RESPUESTAS DE LAS PRIMERAS PREGUNTAS:
#y= x²+x respuesta [0]
#9x²-4y²=36 respuesta [2]
#4x-y=7 respuesta [3]
#x²+y²=9 respuesta [1]
preguntas1 = {"y= x²+x":["x=(0,0)(-1,0) y= (0,0)","x= (-1,0)(1,0) y= (0,5)(0,-5)",
                         "x= (1,0)(0,1) y= (0,0)","x= (1,0)(1,0) y= (0,0)(0,1)"],
              "9x²-4y²=36":["x = (2,0)(-2,0) y = (0,4)(0,-4)","x= (3,0)(-3,0) y=(0,6)(0,-6)",
                            "x= (2,0)(-2,0) y= No tiene corte con y","x=(2,0)(2,0) y=(0,5)(0,-5)"],
              "4x-y=7":["x= (0,7/4) y= (7,0)","x= (-7/4,0) y= (0,7)",
                        "x= No hay corte con x y= (0,7)","x= (7/4,0) y=(0,-7)"],
              "x²+y²=9": ["x= (2,0)(-2,0) y= (0,2)(0,-2)","x= (3,0)(-3,0) y= (0,3)(0,-3)",
                          "x= (2,0)(-2,0) y= (0,2)(0,-2)","x= (4,0)(-4,0) y= (0,4)(0,-4)"]}
respuestas1 = {"y= x²+x": 0,"9x²-4y²=36": 2,"4x-y=7": 3,"x²+y²=9": 1 }
#---------------------------------------------------------------------------------------------------#
#RESPUESTAS DE LA SEGUNDA PREGUNTA
#Pasa por el punto (-2,-1) y tiene pendiente 1/2 respuesta [2]
#Pasa por los puntos (-2,1) y (3,4) respuesta [0]
#Tiene pendiente 0 y pasa por los puntos (1,3) [1]
#Pasa por los puntos (-3,-1) y (4,2) respuesta [3]
preguntas2 = {"Pasa por el punto (-2,-1) y tiene pendiente 1/2":["y= -x-1","y= x-1","y= 1/2x","y= 2/x-1"],
              "Pasa por los puntos (-2,1) y (3,4)":["y= 3/5x + 11/5","y= 5/3x + 4/3","y= 2/5x + 1/5","y= 2/5x - 1/5"],
              "Tiene pendiente 0 y pasa por los puntos (1,3)": ["y= 0","y= 3","y= -3","y= 2"],
              "Pasa por los puntos (-3,-1) y (4,2)":["y= 3/7x + 3","y= -3/7x + 2/3","y= 7/3x + 2","y= 3/7x + 2/7"]}
respuestas2 = {"Pasa por el punto (-2,-1) y tiene pendiente 1/2": 2,"Pasa por los puntos (-2,1) y (3,4)": 0,
               "Tiene pendiente 0 y pasa por los puntos (1,3)": 1,"Pasa por los puntos (-3,-1) y (4,2)": 3}
#----------------------------------------------------------------------------------------------------#
#RESPUESTAS DE LA TERCERA PREGUNTA
#Verificar si las ecuaciones 2x+3y=4,-3x+2y=7 son paralelas o perpendiculares respuesta [2]
#Que valor de k hace que 2(k+3)x-y=4 y 3x+2y=7 sean paralelas y perpendiculares [3]
preguntas3 = {"Verificar si las ecuaciones 2x+3y=4,-3x+2y=7 son paralelas o perpendiculares": ["Son perpendiculares y paralelas",
                                                                                               "No son perpendiculares pero si paralelas",
                                                                                               "Son perpendiculares pero no paralelas",
                                                                                               "No me se la respuesta"],
             "Que valor de k hace que 2(k+3)x-y=4 y 3x+2y=7 sean paralelas y perpendiculares":["Perpendicular: k= 7/3 Paralela: k= -2/3",
                                                                                               "Perpendicular: k= -7/3 Paralela: k= 2/3",
                                                                                               "Perpendicular: k= 1 Paralela: k= 0",
                                                                                               "Perpendicular: k= -15/4 Paralela: k= -8/3"]}
respuestas3 = {"Verificar si las ecuaciones 2x+3y=4,-3x+2y=7 son paralelas o perpendiculares": 2,
               "Que valor de k hace que 2(k+3)x-y=4 y 3x+2y=7 sean paralelas y perpendiculares": 3}
#----------------------------------------------------------------------------------------------------#
#RESPUESTAS DE LA CUARTA PREGUNTA
#A que conica corresponde la siguiente ecuacion: x²/9-y²/4=1 respuesta [0]
#A que conica corresponde la siguiente ecuacion: y-3 = -(x-2)²+3 respuesta [1]
#A que conica corresponde la siguiente ecuacion: (x-3)²+(y+2)²=25 [2]
#A que conica corresponde la siguiente ecuacion: x²/5²+y²/3² [3]
preguntas4 = {"A que conica corresponde la siguiente ecuacion: x²/9-y²/4=1":["Hiperbola","Parabola","Circunferencia","Elipse"],
              "A que conica corresponde la siguiente ecuacion: y-3 = -(x-2)²+3":["Hiperbola","Parabola","Circunferencia","Elipse"],
              "A que conica corresponde la siguiente ecuacion: (x-3)²+(y+2)²=25":["Hiperbola","Parabola","Circunferencia","Elipse"],
              "A que conica corresponde la siguiente ecuacion: x²/5²+y²/3²":["Hiperbola","Parabola","Circunferencia","Elipse"]}
#--------#
respuestas4 = {"A que conica corresponde la siguiente ecuacion: x²/9-y²/4=1": 0,"A que conica corresponde la siguiente ecuacion: y-3 = -(x-2)²+3": 1,
               "A que conica corresponde la siguiente ecuacion: (x-3)²+(y+2)²=25": 2,"A que conica corresponde la siguiente ecuacion: x²/5²+y²/3²": 3}
#-----------------------------------------------------------------------------------------------------#
#RESPUESTAS DE LA QUINTA PREGUNTA
#f(x)= -x²-x-4: calcular f(-9),f(2),f(4) respuesta [2]
#f(x)= √x-4 - 3x, calcular f(7),f(3),f(5) [0]
preguntas5 = {"f(x)= -x²-x-4: calcular f(-9),f(2),f(4)":["f(-9)= -85  f(2)= -6 f(4)= -18 ","f(-9)= -60  f(2)= -4  f(4)= -22 ",
                                                         "f(-9)= -76  f(2)= -10  f(4)= -24 ","f(-9)= -90 f(2)=  -14 f(4)= -26"],
              "f(x)= √x-4 - 3x, calcular f(7),f(3),f(5)":["f(13)= -36 f(4)= -12 f(8)= -22","f(13)= -30  f(4)= -10 f(8)= -22",
                                                          "f(13)= -25  f(4)= -8 f(8)= -5 ","f(13)= 30  f(4)= 10  f(8)= 22 "],
                "f(x)= 2x²-3x+5, calcular f(-1),f(4),f(10)":["f(-1)=8, f(4)= 30, f(10)= 180","f(-1)= 10, f(4)= 25, f(10)= 175",
                                                             "f(-1)=12, f(4)= 22, f(10)= 165","f(-1)=7, f(4)= 20, f(10)= 170"],
                "f(x)= 2x-4x²+3x-5, calcular f(2),f(5),f(9)":["f(2)= 0 ,f(5)= 10 ,f(9)= -50","f(2)= 10 ,f(5)= -20 ,f(9)= 100",
                                                               "f(2)= 1 ,f(5)= -5 ,f(9)= -45","f(2)= -11 ,f(5)= -80 ,f(9)= -284"]}
respuestas5 = {"f(x)= -x²-x-4: calcular f(-9),f(2),f(4)": 2,"f(x)= √x-4 - 3x, calcular f(7),f(3),f(5)":0,
               "f(x)= 2x²-3x+5, calcular f(-1),f(4),f(10)": 1,"f(x)= 2x-4x²+3x-5, calcular f(2),f(5),f(9)": 3}
#------------------------------------------------------------------------------------------------------#
preguntas6 = {"Encontrar el dominio de: f(x)= √2x+7": ["[-7/2,+ꝏ)","(-7/2,+ꝏ)","Todos los reales excepto x>-7/2","(-7/2,0]"]
              ,"Encontrar el dominio de: f(x)= √9-x²":["(-ꝏ,+ꝏ)","[-3,3]","[0,+ꝏ)","(-ꝏ,0]"],
              "Encontrar el dominio de: f(x)= √8-3x":["(-ꝏ,8/3)","[0,4]","(-ꝏ,8/3]","(4,+ꝏ)"],
              "Encontrar el dominio de: f(x)= √x²-25":["[-5,5]","[-5,5)","(-5,5)","(-ꝏ,-5]U[5,+ꝏ)"]}
respuestas6 = {"Encontrar el dominio de: f(x)= √2x+7": 0,"Encontrar el dominio de: f(x)= √9-x²": 1,
               "Encontrar el dominio de: f(x)= √8-3x": 2,"Encontrar el dominio de: f(x)= √x²-25": 3}
#----------------#
generar_pregunta = [preguntas1,preguntas2,preguntas3,preguntas4,preguntas5,preguntas6]
generar_respuesta = [respuestas1,respuestas2,respuestas3,respuestas4,respuestas5,respuestas6]
    