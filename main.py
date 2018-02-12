import dongle
import radonSensor
import mqtt
import config

import time
import json

def settingSensor(client, userdata, message):
	command = message.payload.decode("utf-8")+"\r\n"
	radonSensor.write(command.encode())

if __name__=="__main__":
	dongle.init()
	radonSensor.init()
	mqtt.init()
	mqtt.setOnMessageFunction(settingSensor)
	print('start')
	
	mqtt.send_SP('start')	
	while True:

		radonString = radonSensor.read()
		#radonString = 'TX,A437,0006,24,13,00'
		#time.sleep(5)
		
		try:
			title,sensorName,radonValue,temp,humi,state = radonString.split(',')
			radonValue=int(radonValue)
			temp = int(temp)
			humi = int(humi)
			state = int(state)
			
			LAC,CID = dongle.get_location()
			MCC = config.configFile.get_cellNetwork_MCC()
			MNC = config.configFile.get_cellNetwork_MNC()
			sendJson={
				'RV':radonValue,
				'T':temp,
				'H':humi,
				'S':state,
				'LAC':LAC,
				'CID':CID,
				'MCC':MCC,
				'MNC':MNC
			}
			jsonString = json.dumps(sendJson)
			mqtt.send_VL(jsonString)
		
		
		except:
			if radonString !='':
				mqtt.send_SP(radonString)
	



