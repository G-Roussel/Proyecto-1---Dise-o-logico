
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


file = open("beamer.tex" , "w")

file.write(r"\documentclass[11pt]{beamer}")
file.write("\n")
file.write(r"\usetheme{Warsaw}")
file.write("\n")
file.write(r"\usepackage[utf8]{inputenc}")
file.write("\n")
file.write(r"\usepackage[spanish]{babel}")
file.write("\n")
file.write(r"\usepackage{amsmath}")
file.write("\n")
file.write(r"\usepackage{amsfonts}")
file.write("\n")
file.write(r"\title{Implementacion con Multiplicador combinacional}")
file.write("\n")
file.write(r"\begin{document}")
file.write("\n")

file.write(r"    \begin{frame}")
file.write("\n")
file.write(r"        \maketitle")
file.write("\n")
file.write(r"    \end{frame}")
file.write("\n")


    
file.write(r"    \section{Prueba}")
file.write("\n")
file.write(r"    \begin{frame}{Valores de entrada de usuario}")
file.write("\n")
file.write(r"        \begin{itemize}")
file.write("\n")
file.write(r"        \item Cantidad de bits de los factores a multiplicar es : X")
file.write("\n")
file.write(r"        \item Valores de cada factor: X * Y")
file.write("\n")
file.write(r"        \item Nombre de archivo de configuración: beamer")
file.write("\n")
file.write(r"        \end{itemize}")
file.write("\n")
file.write(r"    \end{frame}")
file.write("\n")
    
file.write(r"    \section{Desarrollo de la multiplicacion binaria}")
file.write("\n")
file.write(r"    \begin{frame}{Desarrollo de la multiplicacion binaria}")
file.write("\n")
file.write(r"        \begin{itemize}")
file.write("\n")
file.write(r"        \item Paso 1: conversión a binario de cada factor:")
file.write("\n")
file.write(r"        \item    Factor X ->")
file.write("\n")
file.write(r"        \item    Factor Y ->")
file.write("\n")
file.write(r"        \item Resultado de la multiplicación parcial: Z")
file.write("\n")
file.write(r"        \item Resultado de la multiplicación total: ")
file.write(r)
file.write("\n")
file.write(r"        \end{itemize}")
file.write("\n")
file.write(r"    \end{frame}")
file.write("\n")
    
file.write(r"    \section{Instituto Tecnológico de Costa Rica}")
file.write("\n")
file.write(r"    \begin{frame}{Instituto Tecnológico de Costa Rica}")
file.write("\n")
file.write(r"        Integrantes:")
file.write("\n")
file.write(r"        \begin{itemize}")
file.write("\n")
file.write(r"        \item George Briceño Celestino")
file.write("\n")
file.write(r"        \item Daniel Chassoul Orella")
file.write("\n")
file.write(r"        \item Kendall Fallas Padilla")
file.write("\n")
file.write(r"        \end{itemize}")
file.write("\n")
file.write(r"        Curso Diseño Lógico ")
file.write("\n")
file.write(r"        \newline")
file.write("\n")
file.write(r"        I Semestre 2023")
file.write("\n")
file.write(r"    \end{frame}")
file.write("\n")
    
file.write(r"\end{document}")


file.close()
