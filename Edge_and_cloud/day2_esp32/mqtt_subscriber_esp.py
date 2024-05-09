import paho.mqtt.client as mqtt
import esp_broker_congig
import uuid
import json
import mysql.connector
import time

def on_connect(client, userdata, flags, rc):
    try:
        print("Connected with result code " + str(rc))
        client.subscribe(esp_broker_congig.channelName1)
        # client.subscribe("cdac/docker/t2")
    except Exception as e:
        print("Exception in Subscriber block",e)

def on_message(client, userdata, msg):
    try:
        print(msg.topic + " " + str(msg.payload))
        print("data recieved",msg.payload.decode())
        # print(type(msg.payload.decode()))

        data_cleaning = msg.payload.decode()
        data_in_json_format = json.loads(data_cleaning)
        #print(type(msg.payload.decode()))
        #print(data_in_json_format['temperature'])
        temperature_data = data_in_json_format["temperatur"]
        humidity_data = data_in_json_format["humidit"]
        # door_status_data = data_in_json_format["door_status"]
        time_data = time.time()
        # current_time = data_in_json_format["curr_time"]

        
       # print(temperature_data)
        #print(humidity_data)
        # print(door_status_data)
        print(time_data)
        # cnx = mysql.connector.connect(
        #     user = "shivam",
        #     passwd = "shivam12",
        #     host = "localhost",
        #     database = "Sensor"
        # )

        # cur = cnx.cursor()
        # val = (temperature_data, humidity_data, time_data)
        # cur.execute("insert into Esp32 values (%s, %s, %s);", val)


        # cnx.commit()

    except Exception as e:
        print("Exception in on message block",e)

def main_handler():
    try:
        mqtt_client_id = uuid.uuid4().hex

        print(mqtt_client_id)
        client = mqtt.Client(client_id=mqtt_client_id)
        client.username_pw_set(username="diot",password="diot123")

        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(esp_broker_congig.broker_address, esp_broker_congig.mqtt_port, esp_broker_congig.keep_alive)

        client.loop_forever()
    except Exception as e:
        print("Exception in main",e)    

main_handler()
