def fail_safe(temperature, neutrons_produced_per_second, threshold):
    result = temperature * neutrons_produced_per_second

    limit = threshold * 0.1

    if threshold - limit <= result <= threshold + limit:
        return "NORMAL"

    if result < threshold - limit:
        return "LOW"

    return "HIGH"

print(fail_safe(10, 10, 90))
print(fail_safe(10, 10, 120))
print(fail_safe(10, 10, 110))
print(fail_safe(10, 10, 111))