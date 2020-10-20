import serial

Fs = 1000   #Frecuencia de muestreo en Hz
t = 5       #segundos de lectura

serial_com = 'COM5'  # seleccionar el COM adecuado
ser = serial.Serial(serial_com, baudrate = 115200, timeout=10)

for x in range(Fs*t):
        try:
            dat = int(ser.readline())
        except:
            dat = 0
        print(dat)

