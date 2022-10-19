import numpy as np
from pyjoycon import JoyCon, get_R_id
import time
import matplotlib.pyplot as plt

joycon_id = get_R_id()
joycon = JoyCon(*joycon_id)

horizontal = 0
vertical = 0

while(True):
    data = joycon.get_status()
    horizontal = (data["analog-sticks"]["right"]['horizontal'] - 2174)/10
    vertical = (data["analog-sticks"]["right"]['vertical'] - 1856)/10
    #print("x",horizontal, ", y", vertical)
    gyro = data["gyro"]
    print("x", gyro['x'], ", y", gyro['y'],"z",gyro['z'])
    time.sleep(0.3)