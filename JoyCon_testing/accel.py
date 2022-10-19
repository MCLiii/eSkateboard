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
x=0
y=0
z=0

def thread():

    global x
    global y
    global z
    while(True):
        data = joycon.get_status()["accel"]
        x = data['x']/50
        y = data['y']/50
        z = data['z']/50
        print(x,",",y,",",z)
        time.sleep(0.1)


t = threading.Thread(target=thread)
t.start()

while(True):

    #time.sleep(0.01)

    plot1.set_xdata(x)
    plot1.set_ydata(z)

    figure.canvas.draw()
    figure.canvas.flush_events()
    plt.show()