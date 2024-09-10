import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Константы
g = 9.81  # ускорение свободного падения, м/с^2
m = 15000  # масса самолета, кг
rho = 1.225  # плотность воздуха, кг/м^3
S = 38  # площадь крыла самолета, м^2
CL = 0.5  # коэффициент подъемной силы
CD0 = 0.04  # коэффициент лобового сопротивления безразмерный
K = 0.04  # коэффициент сопротивления


# Системы уравнений
def dynamics(state, t):
    # Разбор состояния
    x, v, a = state

    # Расчет аэродинамических сил
    l = 0.5 * rho * v**2 * S * CL  # подъемная сила
    d = 0.5 * rho * v**2 * S * (CD0 + K * CL**2)  # лобовое сопротивление

    # Уравнения движения
    x_dot = v
    v_dot = (l - d - m * g) / m
    a_dot = 0

    return np.array([x_dot, v_dot, a_dot])


# Начальные условия
t0 = 0  # начальное время, с
tf = 30  # конечное время, с
dt = 0.01  # шаг интегрирования, с
t = np.arange(t0, tf, dt)

x0 = 500  # начальное положение, м
v0 = 150  # начальная скорость, м/с
a0 = 9.81  # начальное ускорение, м/с^2
state0 = np.array([x0, v0, a0])

# Интегрирование системы уравнений
states = [state0]
for i in range(1, len(t)):
    state = states[i-1]
    t_step = [t[i-1], t[i]]
    next_state = odeint(dynamics, state, t_step)[-1]
    states.append(next_state)

# Извлечение значений
x = [state[0] for state in states]
v = [state[1] for state in states]
a = [state[2] for state in states]

# Графики
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.xlabel('Время, с')
plt.ylabel('Положение, м')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v)
plt.xlabel('Время, с')
plt.ylabel('Скорость, м/с')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a)
plt.xlabel('Время, с')
plt.ylabel('Ускорение, м/с^2')
plt.grid(True)

plt.tight_layout()
plt.show()
