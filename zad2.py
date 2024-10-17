def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "Zielony"
    elif efficiency >= 60:
        return "Pomarańczowy"
    elif efficiency >= 30:
        return "Czerwony"

    return "Czarny"


print(reactor_efficiency(10, 10, 100))
print(reactor_efficiency(1, 10, 100))
print(reactor_efficiency(5, 10, 100))