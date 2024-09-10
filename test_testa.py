from control.matlab import *
import matplotlib.pyplot as plt
""" Создадим LTI-объект с именем w, для этого выполним:"""
num= [1,]
den= [0.0012, 0.04, 1]
w= tf(num, den)
y,x=impulse(w)
plt.plot(x,y,"r")
plt.title('impulse Responsse ')
plt.ylabel('Amplitude')
plt.xlabel('Time(sec)')
plt.grid(True)
plt.show()


y,x=step(w)
plt.plot(x,y,"b")
plt.title('Step Responsse ')
plt.ylabel('Amplitude')
plt.xlabel('Time(sec)')
plt.grid(True)
plt.show()