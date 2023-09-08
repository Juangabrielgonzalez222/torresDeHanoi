def checkInput(obj,val):
  if hasattr(obj,val):
    return obj.press[val] != 0
  return 0
def init():
  global nDiscos,pila,ingresarTexto,cargarDiscos,parte1,parte2,pilas,maderaY,movimientos,mensajeMovimientos,origen,destino,mensajeOrigen,mensajeDestino,error,espera,gano,mensajeMovimientosMinimos
  nDiscos=3
  maderaY=-8
  movimientos=0
  error=None
  mensajeMovimientos='Movimientos: 0'
  pilas=[]
  ingresarTexto=True
  parte1=True
  parte2=False
  cargarDiscos=False
  mensajeOrigen='Origen:'
  mensajeDestino='Destino:'
  mensajeMovimientosMinimos='Movimientos mínimos: '
  origen=None
  destino=None
  espera=0
  gano=False
  for i in range(3):
    pilas.append(PilaEncadenada())
def update():
  global nDiscos,ingresarTexto,parte1,parte2,origen,destino,mensajeMovimientos,mensajeOrigen,mensajeDestino,error,espera,movimientos,gano,mensajeMovimientosMinimos
  if touch.release or checkInput(keyboard,"ENTER"):
    if parte1:
      if nDiscos>1 and nDiscos<10:
        ingresarTexto=False
        for i in range(nDiscos-1,-1,-1):
          pilas[0].insertar(i)
        parte1=False
        parte2=True
    elif parte2:
      if touch.y>-80 and touch.y<63:
        pila=None
        if touch.x>-140 and touch.x<-70:
          pila=1
        if touch.x>-30 and touch.x<30:
          pila=2
        if touch.x>68 and touch.x<130:
          pila=3
        if not error:
          if origen==None:
            origen=pila
            mensajeOrigen='Origen: '+str(origen)
          else:
            destino=pila
            mensajeDestino='Destino: '+str(destino)
            #comprobar movimiento
            if destino:
              if origen!=destino:
                origen-=1
                destino-=1
                if not pilas[origen].vacia() and (pilas[destino].vacia() or pilas[origen].getValorTope() < pilas[destino].getValorTope()) :
                  aux=pilas[origen].suprimir()
                  pilas[destino].insertar(aux)
                  movimientos+=1
                  mensajeMovimientos='Movimientos: '+str(movimientos)
                  #comprobarVictoria
                  if pilas[2].getCantidad()==nDiscos:
                    gano=True
                    mensajeMovimientosMinimos+=str(2**nDiscos-1)
                    parte2=False
                else:
                  error='error'
            origen=None
            destino=None
            mensajeOrigen='Origen:'
            mensajeDestino='Destino:'
    elif gano:
      gano=False
      nDiscos=3
      movimientos=0
      mensajeMovimientos='Movimientos: 0'
      ingresarTexto=True
      parte1=True
      cargarDiscos=False
      mensajeOrigen='Origen:'
      mensajeDestino='Destino:'
      mensajeMovimientosMinimos='Movimientos mínimos: '
      for pila in pilas:
        pila.vaciar()
  if error:
    if espera>100:
      error=None
      espera=0
    else:
      espera+=1
  #inputs teclado
  if ingresarTexto:
    if checkInput(keyboard,"0"):
      nDiscos=int(str(nDiscos)+'0')
    if checkInput(keyboard,"1"):
      nDiscos=int(str(nDiscos)+'1')
    if checkInput(keyboard,"2"):
      nDiscos=int(str(nDiscos)+'2')
    if checkInput(keyboard,"3"):
      nDiscos=int(str(nDiscos)+'3')
    if checkInput(keyboard,"4"):
      nDiscos=int(str(nDiscos)+'4')
    if checkInput(keyboard,"5"):
      nDiscos=int(str(nDiscos)+'5')
    if checkInput(keyboard,"6"):
      nDiscos=int(str(nDiscos)+'6')
    if checkInput(keyboard,"7"):
      nDiscos=int(str(nDiscos)+'7')
    if checkInput(keyboard,"8"):
      nDiscos=int(str(nDiscos)+'8')
    if checkInput(keyboard,"9"):
      nDiscos=int(str(nDiscos)+'9')
    if checkInput(keyboard,'BACKSPACE'):
      nDiscos=str(nDiscos)
      if len(nDiscos)==1:
        nDiscos=0
      else:
        nDiscos=int(str(nDiscos)[:-1])
def draw():
  screen.clear()
  if gano:
    screen.fillRect(0,0,screen.width,screen.height,"rgb(153,197,197)")
    screen.drawText('Has completado el juego',0,70,30,'#000')
    screen.drawText(mensajeMovimientos,0,30,25)
    screen.drawText(mensajeMovimientosMinimos,0,0,25)
    screen.drawText('Clic para comenzar una nueva partida',0,-50,20)
  else:
    if parte1:
      screen.drawText("Ingrese la cantidad de discos, 2-9",0,30,15, "#FFF")
      screen.drawText("Clic para comenzar",0,-30,15, "#FFF")
      screen.drawSprite('campo',0,0)
      screen.drawText(str(nDiscos),0,0,15)
    if parte2:
      screen.fillRect(0,0,screen.width,screen.height,"rgb(153,197,197)")
      screen.drawSprite('madera',-100,maderaY)
      screen.drawSprite('madera',-0,maderaY)
      screen.drawSprite('madera',100,maderaY)
      screen.drawSprite('base',0,-90)
      screen.drawText(mensajeMovimientos,-screen.width/2+screen.textWidth(mensajeMovimientos, 20 )/2+12,86,20,'#000')
      screen.drawText(mensajeOrigen,screen.width/2-screen.textWidth(mensajeOrigen, 20 )/2-16,86,20,'#000')
      screen.drawText(mensajeDestino,screen.width/2 - screen.textWidth(mensajeOrigen, 20 )/2-18 ,62,20,'#000')
      #for pila in pilas:pila.dibujar()
      pilas[0].dibujar()
      pilas[1].dibujar(0)
      pilas[2].dibujar(100)
    if error:
      screen.drawSprite(error,0,0)
      screen.drawText('Invalido',0,-20,20)