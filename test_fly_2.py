import numpy as np
import matplotlib.pyplot as plt

def simulate_flight(duration, timestep, velocity):
    # Задаем начальные условия и параметры моделирования
    position = np.array([0, 0, 0])  # [x, y, z] позиция самолета
    angle_of_attack = 0  # угол атаки (в градусах)

    # Коэффициенты для модели аэродинамических сил
    drag_coefficient = 0.04  # коэффициент сопротивления
    lift_coefficient = 0.5  # коэффициент подъемной силы

    time = np.arange(0, duration, timestep)  # временной интервал

    positions = []  # список позиций самолета
    velocities = []  # список скоростей самолета

    for t in time:
        # Вычисляем силы аэродинамики
        drag = -0.5 * drag_coefficient * velocity**2  # сила сопротивления
        lift = 0.5 * lift_coefficient * velocity**2 * np.sin(np.deg2rad(angle_of_attack))  # подъемная сила

        # Обновляем позицию и скорость самолета
        np.add(position, velocity * timestep, out=position, casting="unsafe")
        #position += velocity * timestep
        velocity += (drag + lift) * timestep

        positions.append(position.copy())
        velocities.append(velocity.copy())

    # Возвращаем списки позиций и скоростей для анализа
    return positions, velocities

# Задаем параметры моделирования
duration = 10  # продолжительность полета (в секундах)
timestep = 0.1  # временной шаг (в секундах)
velocity = 150  # постоянная скорость (в м/с)

# Вызываем функцию моделирования
positions, velocities = simulate_flight(duration, timestep, velocity)

# Визуализация результатов
positions = np.array(positions)
velocities = np.array(velocities)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('X position')
plt.ylabel('Y position')
plt.title('Flight Path')

plt.subplot(1, 2, 2)
plt.plot(velocities)
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Velocity')

plt.show()