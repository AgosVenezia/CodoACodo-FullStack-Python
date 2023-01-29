import sys

cont= 0
cont_ok= 0
cont_err= 0
f= open('F:\\archivo.txt')     #FileNotFoundError
#f= open('F:\Descargas\Cursos\Codo a Codo 4.0 - Full Stack Python\VSCode\CaC PYTHON\PYTHON\py-8\archivo.txt')     #FileNotFoundError
s= f.readline()
while True and s!='':
    try:
        i= int(s.rstrip())             #ValueError
        print(i)
        s= f.readline()
    except:
        if s=='':
            break
        print("Error: ", sys.exc_info()[0])   #Log Error:  <class 'ValueError'>
    else:
        cont_ok+=1 
    finally:
        cont+=1 
f.close()
print("Fin!")