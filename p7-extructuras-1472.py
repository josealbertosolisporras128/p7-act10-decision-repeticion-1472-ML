# estructuras p7 act 10
# jose solis nc 1472
print("-------PRIMEROS 2 EJEMPLOS-------")
edad_usuario = 18
edad_minima = 21

if edad_minima > edad_usuario:
  print("No tienes la edad suficiente para ingresar.")

print("--------------")
stock_disponible = 15
pedido = 50

if pedido > stock_disponible:
  print("Advertencia: El pedido supera el inventario disponible.")

print("------SEGUNDOS 2 EJEMPLOS--------")
nota_obtenida = 85
nota_maxima = 85

if nota_obtenida > nota_maxima:
  print("Error: La nota no puede ser mayor al máximo.")
elif nota_obtenida == nota_maxima:
  print("¡Felicidades! Obtuviste la calificación perfecta.")

print("--------------")
bateria_actual = 20
nivel_alerta = 20

if bateria_actual < nivel_alerta:
  print("Batería muy baja: Por favor conecta el cargador.")
elif bateria_actual == nivel_alerta:
  print("Atención: Tu batería acaba de llegar al límite de reserva.")

print("-------TERCEROS 2 EJEMPLOS-------")
goles_local = 3
goles_visitante = 1

if goles_visitante > goles_local:
  print("El equipo visitante gana el partido.")
elif goles_local == goles_visitante:
  print("El partido termina en empate.")
else:
  print("El equipo local gana el partido.")

print("--------------")
precio_laptop = 1200
precio_telefono = 800

if precio_telefono > precio_laptop:
  print("El teléfono es más caro que la laptop.")
elif precio_laptop == precio_telefono:
  print("Ambos productos tienen el mismo precio.")
else:
  print("La laptop es más cara que el teléfono.")

print("-------CUARTOS 2 EJEMPLOS-------")
tareas = ["Enviar correo", "Asistir a la reunión", "Revisar informe"]

for tarea in tareas:
  print("Tarea pendiente:", tarea)

print("--------------")
usuarios = ["Carlos", "Ana", "Beatriz"]

for usuario in usuarios:
  print("Hola " + usuario + ", ¡bienvenido de nuevo!")

print("-------QUINTOS 2 EJEMPLOS-------")
contador = 5

while contador > 0:
  print("Despegue en:", contador)
  contador -= 1  # Equivale a: contador = contador - 1

print("¡Despegue!")

print("--------------")
intentos = 1

while intentos <= 3:
  print("Intento fallido número:", intentos)
  intentos += 1

print("Cuenta bloqueada por demasiados intentos.")

print("jose solis nc 1472")