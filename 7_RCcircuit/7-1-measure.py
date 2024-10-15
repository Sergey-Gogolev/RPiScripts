import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
levels = 256
maxVolts = 3.28

def decimal_to_binary(x):
    return [int(n) for n in bin(x)[2:].zfill(8)]

def binary_to_decimal(a):
    s = ''
    for x in a:
        
        s += str(x)
    return int(s, 2)

def val_to_led(volts):
    ledsignal = [0]*8
    for i in range(8):
        if volts >= maxVolts*(i+1)/8:
            ledsignal[i] = 1
    return ledsignal


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

measure_values = []

try:
    begining_time = time.time()
    val = 0
    volts = 0
    while (volts < 2.66):
        signal = [0,0,0,0,0,0,0,0]
        for i in range(8):
            signal[i] = 1
            GPIO.output(dac, signal)
            time.sleep(0.005)
            compval = GPIO.input(comp)
            if compval == 1:
                signal[i] = 0
            else:
                signal[i] = 1
        val = binary_to_decimal(signal)
        volts = val/levels * 3.3
        measure_values.append(volts)
        print("ADC val = {:^3} -> {}, input voltage = {:.2f}".format(val, signal, volts))
        GPIO.output(led,0)
        GPIO.output(led, val_to_led(volts))

    GPIO.output(troyka,0)

    while (volts > 0.06):
        signal = [0,0,0,0,0,0,0,0]
        for i in range(8):
            signal[i] = 1
            GPIO.output(dac, signal)
            time.sleep(0.005)
            compval = GPIO.input(comp)
            if compval == 1:
                signal[i] = 0
            else:
                signal[i] = 1
        val = binary_to_decimal(signal)
        volts = val/levels * 3.3
        measure_values.append(volts)
        print("ADC val = {:^3} -> {}, input voltage = {:.2f}".format(val, signal, volts))
        GPIO.output(led,0)
        GPIO.output(led, val_to_led(volts))
    
    ending_time = time.time()
    MesuaringDuration = ending_time - begining_time
    MesuaringPeriod = MesuaringDuration/len(measure_values)
    DiscretizationFrequency = 1/MesuaringPeriod
    QuatizationStep = maxVolts/levels

    with open('settings.txt','w') as datafile:
        datafile.write("Mesuaring duration = {:.3f} S".format(MesuaringDuration))
        datafile.write('\n')
        datafile.write("Mesuaring period = {:.7f} S".format(MesuaringPeriod))
        datafile.write('\n')
        datafile.write("Discretization frequency = {:.3f} HZ".format(DiscretizationFrequency))
        datafile.write('\n')
        datafile.write("QuatizationStep = {:.3f} V".format(QuatizationStep))

    str_measure_values = [str(x) for x in measure_values]
    with open('data.txt','w') as datafile:
        datafile.write("\n".join(str_measure_values))
    

    plt.plot(measure_values)
    plt.show()
except KeyboardInterrupt:
    print('Program was stopped by User')
else:
    print('No exceptions')

finally:

    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    print()
    print('VSE')
    print()