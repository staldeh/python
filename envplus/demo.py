from subprocess import PIPE, Popen

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])


# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 1.16

cpu_temps = [get_cpu_temperature()] * 5
print (cpu_temps)
print (cpu_temps[1:])
print (cpu_temps[:3])
