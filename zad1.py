def is_criticality_balanced(temperature, neutrons_produced_per_second):
    return (
            temperature < 800 and
            neutrons_produced_per_second > 500 and
            temperature * neutrons_produced_per_second < 500000
            )


print(is_criticality_balanced(100, 100))

print(is_criticality_balanced(700, 700))

print(is_criticality_balanced(700, 1000))
