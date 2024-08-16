# 3 jercicios Practicos
# 3.1 Calculo de ecuación de movimiento:
"""
Considere una particula que se rije por las ecuaciones de movimiento de la mecanica clasica, esta a su vez tiene:
- Una posición inicial = 30m
- Una velocidad inicial de = 15 metros sobre segundo
- Un aceleración constante de = 5 metros sobre segundo al cuadrado

Genere una función para determinar
- La posición a los 15 segundos
- El desplazamiento entre 50 segundos y 20 segundos
- Cuál es la posición a los 5 minutos.
"""

def ec_moved(t, pos_inicial, vel_inicial, acel):
    pos = pos_inicial + (vel_inicial*t) + (0.5*acel)*(t**2)
    return pos

def ec_moved_desplazamiento(t_inicial, t_final, vel_inicial, acel):
    desplazamiento = vel_inicial*t_final + 0.5*acel*t_final**2 - vel_inicial*t_inicial - 0.5*acel*t_inicial**2
    return desplazamiento

pos_inicial = 30
vel_inicial = 15
acel_costante = 5
timpo_15 = 15

ecmoved = ec_moved(timpo_15, pos_inicial, vel_inicial, acel_costante)
print(f'La posición a los 15 segundos es: {ecmoved} m')

t_50_20 = [50, 20]

desplazamiento = ec_moved(50, pos_inicial, vel_inicial, acel_costante) - ec_moved(20, pos_inicial, vel_inicial, acel_costante)

print(f'El desplazamiento entre 50 segundos y 20 segundos es: {desplazamiento} m')

t_5_minutos = 5*60

pos_5_min = ec_moved(t_5_minutos, pos_inicial, vel_inicial, acel_costante)

print(f'La posición a los 5 minutos es: {pos_5_min} m')