import serial
import time
import config

port = 0
def init_serial():
	serial_port = config.configFile.get_radonSensor_serial_port()
	serial_baudrate = config.configFile.get_radonSensor_serial_baudrate()
	global port 
	port = serial.Serial(serial_port,serial_baudrate)
	port.timeout = None

def read():
	#try:
	return port.readline()
	'''
	except:
		print("sensor error")
	'''
def write(content):
	#try:
	port.write(content)
	'''
	except:
		print("sensor error")
	'''
def init():
	init_serial()

	

if __name__=="__main__":
	init()
	while True:
		#print(read())
		string = read()
		string = time.asctime( time.localtime(time.time()) )+":"+string
		with open('test.txt', 'w') as f:
			f.write(string)
	