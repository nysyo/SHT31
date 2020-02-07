import serial
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import time
ser = serial.Serial('/dev/ttyACM0',9600)

x = []
t = []
h = []
start = time.time()
while time.time() - start < 3:
    a = ser.readline()
while True:
    value = [float(e) for e in ser.readline().decode().replace('\r\n','').split(',')]
    x.append(datetime.datetime.now())
    t.append((value[0]+value[1])/2)
    h.append((value[2]+value[3])/2)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(x,t,color='r',label='temperature')
    ax2.plot(x,h,color='b',label='humidity')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax1.set_title('Temperature and Humidity')
    ax1.set_ylim([10,25])
    ax2.set_ylim([40,70])
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2,l1+l2)
    
    plt.savefig('data.png')
