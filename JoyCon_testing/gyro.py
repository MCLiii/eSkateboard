import threading

import numpy as np
from pyjoycon import JoyCon, get_R_id
import time
import matplotlib.pyplot as plt

joycon_id = get_R_id()
joycon = JoyCon(*joycon_id)

horizontal = 0
vertical = 0
plt.ion()
figure, ax = plt.subplots(figsize=(10, 10))
plot1, = ax.plot(horizontal,vertical,marker="o", markersize=20)
plt.xticks(np.linspace(-200,200))
plt.yticks(np.linspace(-200,200))
plt.xlabel("lol idk wtf")
_x = [0]
_y = [0]

def thread():
    x = 0
    y = 0
    global _x
    global _y
    while(True):
        data = joycon.get_status()['gyro']
        if (data['z']/10 != x) and (data['y']/10 != y):
            x = data['z'] / 10
            y = data['y'] / 10
        _x.append(_x[len(_x)-1]+x)
        _y.append(_y[len(_y)-1]+y)
        #print(_x, ", ", _y)
        time.sleep(0.1)


x = threading.Thread(target=thread)
x.start()

while(True):

    #time.sleep(0.01)

    plot1.set_xdata(_x)
    plot1.set_ydata(_y)

    figure.canvas.draw()
    figure.canvas.flush_events()
    plt.show()