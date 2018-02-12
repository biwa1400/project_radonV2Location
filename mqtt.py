import paho.mqtt.client as mqtt
import time

import config

mqttClient = 0
def block_connect():
	mqtt_username = config.configFile.get_mqtt_username()
	mqtt_password = config.configFile.get_mqtt_password()
	
	global mqttClient 
	mqttClient = mqtt.Client(client_id=mqtt_username)
	while True:
		try:
			mqttClient.username_pw_set(mqtt_username, mqtt_password)  
			HOST = config.configFile.get_mqtt_host()
			port = config.configFile.get_mqtt_port()
			mqttClient.connect(HOST, port, 60)
			mqttClient.loop_start()
			break
		except:
			print ("in init except")
			time.sleep(5)

def send(topic,sendContent):
	try:
		mqttClient.publish(topic,sendContent)
	except:
		print ("mqtt error")
		block_connect()

def send_VL(sendContent):
	sendVLTopic = config.configFile.get_mqtt_topic_sendVL()
	send(sendVLTopic,sendContent)
	
def send_SP(sendContent):
	sendSPTopic = config.configFile.get_mqtt_topic_sendSP()
	print(sendSPTopic)
	send(sendSPTopic,sendContent)

def init():
	block_connect()
	mqttClient.on_message=on_message
	recvTopic = config.configFile.get_mqtt_topic_recv()
	mqttClient.subscribe(recvTopic)

def setOnMessageFunction(function):
	mqttClient.on_message=function
	
def on_message(client, userdata, message):
	print("message received " ,str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)
	print("message qos=",message.qos)
	print("message retain flag=",message.retain)
	

if __name__=="__main__":
	init()
	while True:	
		#send('hehe')
		time.sleep(5)
	
	