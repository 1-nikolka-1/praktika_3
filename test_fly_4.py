class RollController:
    def __init__(self, kp):
        self.kp = kp

    def control(self, desired_roll, current_roll):
        # Вычисление ошибки
        error = desired_roll - current_roll

        # Вычисление управляющего сигнала
        control_signal = self.kp * error

        return control_signal


# Функция, которая симулирует изменение текущего крена
def simulate_roll_change(current_roll, control_signal, aero_coefficients):
    # Расчёт изменения крена на основе управляющего сигнала и аэродинамических коэффициентов
    roll_change = calculate_roll_change(control_signal, aero_coefficients)

    # Обновление текущего крена
    current_roll += roll_change

    return current_roll


# Функция для расчёта изменения крена на основе управляющего сигнала и аэродинамических коэффициентов
def calculate_roll_change(control_signal, aero_coefficients):
    # Расчет момента от аэродинамических сил
    aero_moment = aero_coefficients['aero_center'][0] * control_signal

    # Расчет момента от геометрии самолета
    geometry_moment = aero_coefficients['geometry']['moment'] * control_signal

    # Общий момент
    total_moment = aero_moment + geometry_moment

    # Расчет изменения крена на основе момента и других факторов
    roll_change = total_moment / aero_coefficients['geometry']['inertia']

    return roll_change


# Заданный крен
desired_roll = 10

# Аэродинамические коэффициенты самолета
aero_coefficients = {
    'aero_center': (0, 0, 0),
    'geometry': {...}
}

# Коэффициент пропорциональной составляющей контроллера
kp = 0.5

# Создание контроллера крена
roll_controller = RollController(kp)

# Начальное значение текущего крена
current_roll = 0

# Симуляция изменения крена и стабилизация с помощью ЭГРП
for _ in range(10):  # здесь можно указать нужное количество шагов симуляции
    # Вычисление управляющего сигнала
    control_signal = roll_controller.control(desired_roll, current_roll)

    # Применение управляющего сигнала к модели изменения крена
    current_roll = simulate_roll_change(current_roll, control_signal, aero_coefficients)

    # Вывод текущего крена
    print("Текущий крен:", current_roll)
