import ow
import time

# Sensor Setup
# ============
#
# S1: /3A.C26934000000 - DS2413
#   PIO A: In
#   PIO B: Out
#
# S2: /3A.8A3134000000 - DS2413
#   PIO A: Out
#   PIO B: In
#
# S3: /3A.1F5834000000 - DS2413
#   PIO A: In
#   PIO B: In
#
# S4: /3A.4C6A34000000 - DS2413
#   PIO A: Out
#   PIO B: ?
#
# 
# In to Out assignment
# ====================
#
# S1 In A  to  S1 Out B
# S2 In B  to  S2 Out A
# S3 In A  to  S4 Out A*
# S3 In B  to  S4 Out A*

# * If the state of either S3 In A or B changes, S4 Out A will toggle

ow.init('localhost:4304')
# 
s1 = ow.Sensor( '/3A.C26934000000' )
s2 = ow.Sensor( '/3A.8A3134000000' )
s3 = ow.Sensor( '/3A.1F5834000000' )
s4 = ow.Sensor( '/3A.4C6A34000000' )

PIO_1B = '1'
PIO_2A = '1'
PIO_4A = '1'
Sens_3A = '0'
Sens_3B = '0'
block = 'false'

def init_PIO():
	# set all output ports initally to '1'
	s1.PIO_B = PIO_1B
	s2.PIO_A = PIO_2A
	s4.PIO_A = PIO_4A

def read_and_set_taster():	
	# this function reads puh buttons and toggles the assigned output
	# S1 In A  to  S1 Out B
	# S2 In B  to  S2 Out A
	global PIO_1B
	global PIO_2A
	global block
	# Taster A
	# pressing this button will toggles the output
	if s1.sensed_A == '0' and block == 'false':
		block = 'true'
		if PIO_1B == '0':
			PIO_1B = '1'
		else:
			PIO_1B = '0'
		s1.PIO_B = PIO_1B
	elif s1.sensed_A == '1':
		block = 'false'
	# Taster B
	# as long as the button is pressed the outpput is set to '0'
	if s2.sensed_B == '0':
		PIO_2A = '0'
	else:
		PIO_2A = '1'
	s2.PIO_A = PIO_2A

def read_and_set_switch():
	# this function reads switches
	# S3 In A  to  S4 Out A*
	# S3 In B  to  S4 Out A*
	# * If the state of either S3 In A or B changes, S4 Out A will toggle
	global Sens_3A
	global Sens_3B
	global PIO_4A
	if s3.sensed_A <> Sens_3A or s3.sensed_B <> Sens_3B:
		Sens_3A = s3.sensed_A
		Sens_3B = s3.sensed_B
		if PIO_4A == '0':
			PIO_4A = '1'
		else:
			PIO_4A = '0'
		s4.PIO_A = PIO_4A
		print('PIO_4A: ' + PIO_4A)
	
	
init_PIO()
while True:
	read_and_set_taster()
	read_and_set_switch()
	time.sleep(0.1)

