import json

class ConfigFile:
	def __init__(self):
		with open('/home/pi/project_radon/config.json', 'r') as jsonFile:
			data = json.load(jsonFile)
			self.__sensorName=data['sensorName']
			self.__sw_debug_mode_filePath = data['filePath']['sw_debug_mode']
			self.__e3372_serial_port = data['e3372_serialConfig']['serial_port']
			self.__e3372_serial_baudrate = data['e3372_serialConfig']['serial_baudrate']
			self.__e3372_command_silent = data['e3372_command']['silent']
			self.__e3372_command_location = data['e3372_command']['location']
			self.__mqtt_host = data['mqtt']['host']
			self.__mqtt_port = data['mqtt']['port']
			self.__mqtt_username = data['mqtt']['username']
			self.__mqtt_password = data['mqtt']['password']
			self.__mqtt_topic_sendVL = data['mqtt']['topic_sendVL']
			self.__mqtt_topic_sendSP = data['mqtt']['topic_sendSP']
			self.__mqtt_topic_recv = data['mqtt']['topic_recv']
			self.__radonSensor_serial_port = data['radonSensor']['serial_port']
			self.__radonSensor_serial_baudrate = data['radonSensor']['serial_baudrate']
			self.__cellNetwork_MCC = data['cellNetwork']['MCC']
			self.__cellNetwork_MNC = data['cellNetwork']['MNC']
	
	def replaceSensorName(self,content):
		return content.replace('sensorName',self.__sensorName)
	
	def get_sensor_name(self):
		return self.__sensorName
	
	def get_dongleConfig_FilePath(self):
		return self.__sw_debug_mode_filePath
		
	def get_e3372_serial_port(self):
		return self.__e3372_serial_port
		
	def get_e3372_serial_baudrate(self):
		return self.__e3372_serial_baudrate
		
	def get_e3372_command_silent(self):
		return self.__e3372_command_silent
		
	def get_e3372_command_location(self):
		return self.__e3372_command_location
		
	def get_mqtt_host(self):
		return self.__mqtt_host
		
	def get_mqtt_port(self):
		return self.__mqtt_port
	
	def get_mqtt_username(self):
		return self.replaceSensorName(self.__mqtt_username)
	
	def get_mqtt_password(self):
		return self.__mqtt_password
		
	def get_mqtt_topic_sendVL(self):
		return self.replaceSensorName(self.__mqtt_topic_sendVL)
	
	def get_mqtt_topic_sendSP(self):
		return self.replaceSensorName(self.__mqtt_topic_sendSP)
		
	def get_mqtt_topic_recv(self):
		return self.replaceSensorName(self.__mqtt_topic_recv)
		
	def get_radonSensor_serial_port(self):
		return self.__radonSensor_serial_port
		
	def get_radonSensor_serial_baudrate(self):
		return self.__radonSensor_serial_baudrate

	def get_cellNetwork_MCC(self):
		return self.__cellNetwork_MCC
		
	def get_cellNetwork_MNC(self):
		return self.__cellNetwork_MNC
		
configFile = ConfigFile()

		
if __name__=="__main__":
	print(configFile.get_dongleConfig_FilePath())