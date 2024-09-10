import numpy as np
import matplotlib.pyplot as plt

def simulate_flight(duration, timestep, velocity):
    # Задаем начальные условия и параметры моделирования
    position = np.array([0, 0, 0])  # [x, y, z] позиция самолета
    attitude = np.array([0, 0, 0])  # [roll, pitch, yaw] углы самолета
    angular_velocity = np.array([0, 0, 0])  # [roll_rate, pitch_rate, yaw_rate] угловые скорости
    angle_of_attack = 5  # угол атаки (в градусах)

    # Коэффициенты для модели аэродинамических сил
    drag_coefficient = 0.1  # коэффициент сопротивления
    lift_coefficient = 0.1  # коэффициент подъемной силы

    time = np.arange(0, duration, timestep)  # временной интервал

    positions = []  # список позиций самолета
    attitude_data = []  # список углов самолета

    for t in time:
        # Вычисляем силы аэродинамики
        drag = -0.5 * drag_coefficient * velocity**2  # сила сопротивления
        lift = 0.5 * lift_coefficient * velocity**2 * np.sin(np.deg2rad(angle_of_attack))  # подъемная сила

        # Вычисляем моменты, вызываемые аэродинамическими силами
        roll_moment = 0  # Момент скручивания
        pitch_moment = 0  # lift * velocity * np.sin(np.deg2rad(angle_of_attack))  # Момент тангажа (от подъемной силы)
        yaw_moment = 0  # Момент газа

        # Вычисляем угловые ускорения
        roll_acceleration = roll_moment  # Ускорение крена
        pitch_acceleration = pitch_moment  # Ускорение тангажа
        yaw_acceleration = yaw_moment  # Ускорение рыскания

        # Обновляем положение и ориентацию самолета в пространстве
        np.add(position, velocity * timestep, out=position, casting="unsafe")
        np.add(attitude, angular_velocity * timestep, out=attitude, casting="unsafe")

        #position += velocity * timestep
        #attitude += angular_velocity * timestep

        # Обновляем скорости вращения самолета
        angular_velocity[0] += roll_acceleration * timestep
        angular_velocity[1] += pitch_acceleration * timestep
        angular_velocity[2] += yaw_acceleration * timestep

        positions.append(position.copy())
        attitude_data.append(attitude.copy())

    # Возвращаем списки позиций и углов для анализа
    return positions, attitude_data

# Задаем параметры моделирования
duration = 10  # продолжительность полета (в секундах)
timestep = 0.1  # временной шаг (в секундах)
velocity = 100  # постоянная скорость (в м/с)

# Вызываем функцию моделирования
positions, attitude_data = simulate_flight(duration, timestep, velocity)

# Визуализация результатов
positions = np.array(positions)
attitude_data = np.array(attitude_data)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('X position')
plt.ylabel('Y position')
plt.title('Flight Path')

plt.subplot(1, 2, 2)
plt.plot(attitude_data[:, 0], label='Roll')
plt.plot(attitude_data[:, 1], label='Pitch')
plt.plot(attitude_data[:, 2], label='Yaw')
plt.xlabel('Time')
plt.ylabel('Attitude')
plt.title('Attitude')
plt.legend()

plt.show()