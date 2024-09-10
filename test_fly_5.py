import control
import numpy as np
import matplotlib.pyplot as plt


def stabilize_aoa(target_aor, aircraft_coeffs):
    # Параметры передаточной функции
    num = [1]
    den = [0.0012, 0.04, 1]

    # Создание объекта передаточной функции
    transfer_function = control.TransferFunction(num, den)

    # Задание входных данных
    time = np.linspace(0, 10, 100)  # Время моделирования
    input_ = np.ones_like(time) * target_aor  # Заданный крен

    # Вычисление выходных данных
    yout = control.forced_response(transfer_function, time, input_)

    # Вывод результатов
    plt.plot(time, yout[0])
    plt.xlabel('Time')
    plt.ylabel('Current AoR')
    plt.title('Stabilized AoR')
    plt.grid(True)
    plt.show()


# Входные данные
target_aor = 70.0   # Заданный крен
aircraft_coeffs = {  # Аэродинамические коэффициенты самолета
    'Cx': 0.04,
    'Cy': 0.5,
    'Cz': 0.1
}

# Запуск моделирования
stabilize_aoa(target_aor, aircraft_coeffs)
