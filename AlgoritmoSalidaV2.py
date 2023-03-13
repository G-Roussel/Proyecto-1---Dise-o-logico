# -*- coding: utf-8 -*-
import subprocess

#valores de entrada
in1 = ""
in2 = ""
#cantidad de bits
bits = ""
#pasos multiplicacion
p1 = ""
p2 = ""
p3 = ""
p4 = ""
#resultado
r = "1010101"




comandos = [r"\documentclass[11pt]{beamer}",
                         r"\usetheme{Warsaw}",
                        
                        r"\usepackage[utf8]{inputenc}",
                        r"\usepackage[spanish]{babel}"
                        r"\usepackage{amsmath}",
                        r"\usepackage{amsfonts}",
                        r"\title{Implementacion con Multiplicador combinacional}",
                        r"\begin{document}",
                        r"    \begin{frame}",
                        r"        \maketitle",
                        r"    \end{frame}",
                        
                        r"    \section{Prueba}",
                        r"    \begin{frame}{Valores de entrada de usuario}",
                        r"        \begin{itemize}",
                        r"        \item Cantidad de bits de los factores a multiplicar es : ",
                        r"        \item Valores de cada factor: X * Y",
                        r"        \item Nombre de archivo de configuración: beamer",
                        r"        \end{itemize}",
                        r"    \end{frame}",
                        
                        r"    \section{Desarrollo de la multiplicacion binaria}",
                        r"    \begin{frame}{Desarrollo de la multiplicacion binaria}",
                        r"        \begin{itemize}",
                        r"        \item Paso 1: conversión a binario de cada factor:",
                        r"        \item    Factor X ->",
                        r"        \item    Factor Y ->",
                        r"        \item Resultado de la multiplicación parcial: Z",
                        r"        \item Resultado de la multiplicación total: ",
                        r"        \end{itemize}",
                        r"    \end{frame}",
                        
                        r"    \section{Instituto Tecnológico de Costa Rica}",          
                        r"    \begin{frame}{Instituto Tecnológico de Costa Rica}",
                        r"        Integrantes:",
                        r"        \begin{itemize}",
                        r"        \item George Briceño Celestino",
                        r"        \item Daniel Chassoul Orella",
                        r"        \item Kendall Fallas Padilla",
                        r"        \end{itemize}",
                        r"        Curso Diseño Lógico ",
                        r"        \newline",
                        r"        I Semestre 2023",
                        r"    \end{frame}",

                        r"\end{document}"]





com1 = "\n".join(comandos)

com2= str(com1)


subprocess.call(["texmaker", com1])
