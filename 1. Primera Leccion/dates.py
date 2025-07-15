# Dates

from datetime import datetime, date, time, timedelta

# Obtener la fecha y hora actual
now = datetime.now()

print('\nFecha y Hora Actual\n')

# Imprime la fecha y hora completa
print(now)

print(f'\nAño: {now.year}')
print(f'Mes: {now.month}')
print(f'Dia: {now.day}')
print(f'Hora: {now.hour}')
print(f'Minuto: {now.minute}')
print(f'Segundo: {now.second}')
print(f'Microsegundo: {now.microsecond}\n')


# Timestamp

# Esto representa los segundos desde 1970
time_stamp = now.timestamp()

print(f'Timestamp: {time_stamp}\n')


# Crear fecha manualmente
print('Fecha manual\n')

# Año, mes, dia, hora, minuto, segundo
fecha_ejemplo = datetime(2025, 12, 25, 15, 30, 0)

print(fecha_ejemplo)


# Imprimir elementos de una fecha
def imprimir_fecha(fecha):
    print(f'Mes: {fecha.month}')
    print(f'Dia: {fecha.day}')
    print(f'Hora: {fecha.hour}')
    print(f'Minuto: {fecha.minute}')
    
print('\nImprimir Fecha')
print(imprimir_fecha(fecha_ejemplo))


# Clase Date
print('\nClase Date\n')

fecha_actual = date.today()

print(f'Fecha actual: {fecha_actual}')
print(f'Año: {fecha_actual.year}')
print(f'Mes: {fecha_actual.month}')
print(f'Dia: {fecha_actual.day}\n')


# Crear una fecha especifica
fecha_manual = date(2027, 1, 15)

print(f'Fecha manual: {fecha_manual}\n')


# Clase Time
print('\nClase Time\n')

hora_actual = time(3,41,30)

print(hora_actual)
print(f'Hora: {hora_actual.hour}')
print(f'Minuto: {hora_actual.minute}')
print(f'Segundo: {hora_actual.second}\n')


# TimeDelta
print('\nUso de Timedelta\n')

# timedelta permite sumar o restar tiempo a una fecha

# Se definen los dias y las horas
delta = timedelta(days=7, hours=8)


# Sumar a la fecha actual
nueva_fecha = now + delta
print(f'Fecha actual: {now}')
print(f'Fecha con +7 dias y +8 horas: {nueva_fecha}')


# Restar tiempo: 30 dias
fecha_resta = now - timedelta(days=30)

print(f'Fecha con -30 dias: {fecha_resta}\n')


# Diferencia entre dos fechas
print('\nDiferencia entre las fechas\n')

fecha_futura = datetime(2025,12, 31)

diferencia = fecha_futura - now

print(f'Falta {diferencia.days} dias y {diferencia.seconds // 3600} horas para el {fecha_futura.date()}\n')