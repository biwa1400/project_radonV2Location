import urllib2
import serial
# private module
import config

port = 0

def changeMode_Debug():
	# read sw_debug_mode.xml file
	sw_debug_mode_string = ''
	# get sw_debug_mode.xml file Path
	file = open(config.configFile.get_dongleConfig_FilePath())
	# read content of the file
	for line in file:
		sw_debug_mode_string = sw_debug_mode_string + line
				
	# POST the setting file	
	req = urllib2.Request(url = "http://192.168.8.1/CGI",data =sw_debug_mode_string)
	res_data = urllib2.urlopen(req)
	res = res_data.read()

def port_read():
	try:
		return port.read(size=1024)
	except:
		print("dongle error")

def port_write(content):
	try:
		port.write(content)
	except:
		print("dongle error")
	
def init_serial():
	serial_port = config.configFile.get_e3372_serial_port()
	serial_baudrate = config.configFile.get_e3372_serial_baudrate()
	global port 
	port = serial.Serial(serial_port,serial_baudrate)
	port.timeout = 0.1
	
def sendCommand_silence():
	command = config.configFile.get_e3372_command_silent()
	port_write(command.encode())
		
	
def get_location():
	command = config.configFile.get_e3372_command_location()
	port_read()
	port_write(command.encode())
	readString = port_read()
	for string in readString.split("\r\n"):
		if string.find('+CREG') is 0:
			returnString = string.split(",")
			return (returnString[2].strip('"'),returnString[3].strip('"'))

def init():
	changeMode_Debug()
	init_serial()
	sendCommand_silence()
