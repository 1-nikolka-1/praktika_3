import numpy as np
import matplotlib.pyplot as plt

def simulate_flight(duration, timestep):
    # Задаем начальные условия
    position = np.array([0, 0, 0])  # [x, y, z] позиция самолета
    velocity = np.array([100, 0, 0])  # [vx, vy, vz] скорость самолета
    acceleration = np.array([-9.8, 0, 0])  # [ax, ay, az] ускорение самолета
    time = np.arange(0, duration, timestep)  # временной интервал

    positions = []  # список позиций самолета
    velocities = []  # список скоростей самолета

    for t in time:
        # Вычисляем силы аэродинамики (например, сопротивление воздуха)
        drag = -0.5 * velocity  # простейшая модель сопротивления воздуха

        # Обновляем ускорение и скорость самолета
        acceleration += drag
        #velocity += acceleration * timestep
        np.add(velocity, acceleration * timestep, out=velocity, casting="unsafe")

        # Обновляем позицию самолета
        #position += velocity * timestep
        np.add(position, velocity * timestep, out=velocity, casting="unsafe")

        positions.append(position.copy())
        velocities.append(velocity.copy())

    # Возвращаем списки позиций и скоростей для анализа
    return positions, velocities

# Задаем параметры моделирования
duration = 10  # продолжительность полета (в секундах)
timestep = 0.1  # временной шаг (в секундах)

# Вызываем функцию моделирования
positions, velocities = simulate_flight(duration, timestep)

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
plt.plot(velocities[:, 0], label='X velocity')
plt.plot(velocities[:, 1], label='Y velocity')
plt.plot(velocities[:, 2], label='Z velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.legend()
plt.title('Velocity Components')

plt.show()