import paho.mqtt.client as mqtt
import broker_config
import uuid
import json
import mysql.connector

def on_connect(client, userdata, flags, rc):
    try:
        print("Connected with result code " + str(rc))
        client.subscribe(broker_config.mqtt_subscriber_topic)
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
        print(type(msg.payload.decode()))

        temperature_data = data_in_json_format["temperature"]
        humidity_data = data_in_json_format["humidity"]
        door_status_data = data_in_json_format["door_status"]
        # time_data = time.time()
        current_time = data_in_json_format["curr_time"]

        
        print(temperature_data)
        print(humidity_data)
        print(door_status_data)
        print(current_time)
        cnx = mysql.connector.connect(
            user = "shivam",
            passwd = "shivam12",
            host = "localhost",
            database = "Sensor"
        )

        cur = cnx.cursor()
        val = (temperature_data, humidity_data, door_status_data,current_time)
        cur.execute("insert into sensorval values (%s, %s, %s, %s);", val)


        cnx.commit()

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
        client.connect(broker_config.broker_address, broker_config.mqtt_port, broker_config.keep_alive)

        client.loop_forever()
    except Exception as e:
        print("Exception in main",e)    

main_handler()