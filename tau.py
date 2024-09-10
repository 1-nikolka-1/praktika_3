from control.matlab import *
from sympy import *
import matplotlib.pyplot as plt


V = 150
g = 9.81
Mza = -2
yfi = 0.04
ya = 0.5
Mzfi = -4.1
Mzwz = -0.18
Mzda = -0.1
Kwz = (Mza * yfi - Mzfi * ya) / (Mzwz * ya + Mza)             # -0.9425837320574162
Twz = (Mzda * yfi - Mzfi) / (Mza * yfi - Mzfi * ya)           # 2.0791878172588834
Ua = -((Mzwz * yfi + Mzfi) / (Mzwz * ya + Mza))               # -1.9651674641148325
T0 = 1 / (- Mzwz * ya - Mza)                                  # 0.47846889952153115
J = 1/2 * ((ya - Mzwz - Mza) / (- Mzwz * ya - Mza)**0.5)      # 0.9268973815805399
P = Symbol("P")

dny_fi_p = V * Kwz / (g * 57.3) * (((Twz - Ua / Kwz) * P + 1) / (T0**2 *P**2 + 2 * J * T0 * P + 1))
# -0.25152871363696*(1 - 0.00568527918781703*P)/(0.228932487809345*P**2 + 0.886983140268459*P + 1)

n_wz = 1 / (Twz * P + 1)
# 1/(2.07918781725888*P + 1)

num = [-0.25152871363696 * -0.00568527918781703, -0.25152871363696]
den = [-0.25152871363696 * 0.228932487809345, -0.25152871363696 * 0.886983140268459, -0.25152871363696]
w = tf(num, den)

y, x = step(w)
plt.figure(1)
plt.plot(x, y, "b")
plt.title("Переходный процесс ф.1")
plt.ylabel('Amplitude')
plt.xlabel('Time(sec)')
plt.grid(True)

plt.figure(3)
mag, phase, omega = bode(w, dB=True)
plt.plot()
plt.suptitle("ЛАФЧХ ф.1")

num = [1]
den = [2.07918781725888, 1]
w = tf(num, den)

y, x = step(w)
plt.figure(2)
plt.plot(x, y, "b")
plt.title("Переходный процесс ф.2")
plt.ylabel('Amplitude')
plt.xlabel('Time(sec)')
plt.grid(True)

plt.figure(4)
mag, phase, omega = bode(w, dB=True)
plt.plot()
plt.suptitle("ЛАФЧХ ф.2")
plt.show()
