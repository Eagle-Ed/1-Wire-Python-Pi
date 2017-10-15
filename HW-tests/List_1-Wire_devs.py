import ow
ow.init('localhost:4304')
sensorlist = ow.Sensor('/').sensorList()
for sensor in sensorlist:
    print(sensor)
    print('Device Found')
    print('Address: ' + sensor.address)
    print('Family: ' + sensor.family)
    print('ID: ' + sensor.id)
    print('Type: ' + sensor.type)
    print('PIO:  ' + sensor.PIO_ALL)
    print('PIO A:  ' + sensor.PIO_A)
    print('PIO B:  ' + sensor.PIO_B)
    print('sensed:  ' + sensor.sensed_ALL)
    print('sensed A:  ' + sensor.sensed_A)
    print('sensed B:  ' + sensor.sensed_B)
    print('Attributes:  '),
    print sensor.entryList()
    print(' ')
