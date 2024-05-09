import paho.mqtt.client as mqtt_diot
import time
import json
import broker_config
import random
from datetime import datetime

def on_publish(client,userdata,result):
    try:
        # print(result)
        if result > 0:
            print(f"Message is published {result} times")
        else:
            print("failed to send message")
    except Exception as e:
        print("Exception in on publish method ",e)

def connectivity_management(broker_address,broker_port):
    try:
        # Create Mqtt client
        global mqtt_client
        mqtt_client = mqtt_diot.Client()
        # Register callback
        mqtt_client.on_publish = on_publish
        # Connect with broker
        mqtt_client.connect(broker_address,broker_port)
    except Exception as e:
        print(e)

def send_telemetry():
    try:
        temp_reading = 11
        humi_reading = 50

        for reading_publish in range(sample_unit):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            random.shuffle(broker_config.valid_door_status)
            print(broker_config.valid_door_status)
            sensor_data = {
                "temperature" : random.randint(broker_config.valid_temp_sensor_interval[0], broker_config.valid_temp_sensor_interval[1]),
                "humidity"  : random.randint(broker_config.valid_humi_sensor_interval[0],broker_config.valid_humi_sensor_interval[1]),
                "door_status" : broker_config.valid_door_status[0],
                "curr_time" : current_time
            }
            mqtt_client.publish(broker_config.publisher_topic_name,json.dumps(sensor_data))
            print("Info : Published Message ", sensor_data)
            time.sleep(5)
    except Exception as e:
        print(e)


def main_handler(sample_unit):
    connectivity_management(broker_config.broker_address,broker_config.mqtt_port)
    send_telemetry()

    # run forever
    # mqtt_client.loop_forever

# calling main handler 
sample_unit = 40
main_handler(sample_unit)