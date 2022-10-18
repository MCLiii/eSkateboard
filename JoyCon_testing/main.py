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
while(True):
    data = joycon.get_status()["analog-sticks"]["right"]
    horizontal = (data['horizontal'] - 2174)/10
    vertical = (data['vertical'] - 1856)/10
    print(horizontal, ", ", vertical)
    time.sleep(0.01)

    plot1.set_xdata(horizontal)
    plot1.set_ydata(vertical)

    figure.canvas.draw()
    figure.canvas.flush_events()
    plt.show()