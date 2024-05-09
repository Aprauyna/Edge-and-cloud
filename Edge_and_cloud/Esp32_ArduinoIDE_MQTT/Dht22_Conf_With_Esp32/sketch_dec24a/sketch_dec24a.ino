/*
 * 
 * This is sample code written for PG-DESD students of ACTS Batch to work with MQTT protocol
 * 
 */
#include <WiFi.h>
#include <PubSubClient.h>    
#include <esp_wifi.h>
#include "DHT.h"
#include <ArduinoJson.h>

// Set the custom MAC address in case your ESP32 is not regsitered with the acts network
uint8_t newMACAddress[] = {0x24, 0x6F, 0x28, 0xAA, 0x9B, 0x94};//24:6F:28:AA:9B:94
DynamicJsonDocument sensor_data_payload(1024);
#define DHTTYPE DHT22
uint8_t DHTPin = 4;
char sensor_data_format_for_mqtt_publish[1024];
const char* ssid =   "Rushi pg";                          //ssid - service set Identifier (Replace it with your ssid name)
const char* password =  "Rushi@1234";                     // replace with ssid paasword
const char* mqttBroker = "localhost";                  // broker address - replace it with your broker address/cloud broker - test.mosquitto.org
//const char* mqttBrokerv1 = "test.mosquitto.org";  
const int   mqttPort = 1883;                            // broker port number
const char* clientID = "techemotes";                   // client-id
//const char* clientIDv1 = "techemotes1";   
const char* channelName1 = "cdac/diot"; // topic names for publish
//const char* channelName2 =  "cdac/diot/room/humi";   
DHT dht(DHTPin, DHTTYPE);
float h;
float t;
WiFiClient MQTTclient;
//WiFiClient MQTTclientv1;
PubSubClient client(MQTTclient);
//PubSubClient clientv1(MQTTclientv1);
long lastReconnectAttempt = 0;
boolean reconnect()
{
  if (client.connect(clientID)) {
    //client.subscribe(channelName); // Subscribe to channel.
    Serial.println("ESP32 IP ADDRESS : ");
    Serial.println(WiFi.localIP());
  }
  return client.connected();
}
//boolean reconnect_v1()
//{
//  if (clientv1.connect(clientIDv1)) {
//    //client.subscribe(channelName); // Subscribe to channel.
//    Serial.println("Subscribed");
//  }
//  return clientv1.connected();
//}
void setup() {
  Serial.begin(115200);
  pinMode(DHTPin, INPUT);
  dht.begin();
  Serial.println("Attempting to connect...");
  WiFi.mode(WIFI_STA);
  esp_wifi_set_mac(WIFI_IF_STA, &newMACAddress[0]);
  WiFi.begin(ssid, password); // Connect to WiFi.
  if (WiFi.waitForConnectResult() != WL_CONNECTED)
  {
    Serial.println("Couldn't connect to WiFi.");
  }
  Serial.println("ESP32 IP ADDRESS : ");
  Serial.println(WiFi.localIP());
  client.setServer(mqttBroker, mqttPort); // Connect to broker
//  clientv1.setServer(mqttBrokerv1, mqttPort); // Connect to broker
//  Serial.println("Connected to Broker");
  lastReconnectAttempt = 0;
}
void loop() {
  if (!client.connected())
  {
    long now = millis();
    if (now - lastReconnectAttempt > 5000) { // Try to reconnect.
      lastReconnectAttempt = now;
      if (reconnect())
      { // Attempt to reconnect.192.168.1.5
        lastReconnectAttempt = 0;
      }
    }
  }
//   if (!clientv1.connected())
//  {
//    long now = millis();
//    if (now - lastReconnectAttempt > 5000) { // Try to reconnect.
//      lastReconnectAttempt = now;
//      if (reconnect_v1())
//      { // Attempt to reconnect.192.168.1.5
//        lastReconnectAttempt = 0;
//      }
//    }
//  }
  else 
  { //Connected.
    client.loop();
//    clientv1.loop();
    t = dht.readTemperature(); // Gets the values of the temperature
    h = dht.readHumidity(); // Gets the values of the humidity 

    sensor_data_payload["temperature"] = t;
    sensor_data_payload["humidity"] = h;
    serializeJson(sensor_data_payload, sensor_data_format_for_mqtt_publish);
    
    delay(2000);
    Serial.println(h);
    Serial.println(t);
  
    client.publish(channelName1, sensor_data_format_for_mqtt_publish);  //(topicname, payload)
//    clientv1.publish(channelName2, String(h).c_str()); 
//    clientv1.publish(channelName1, String(t).c_str());  //(topicname, payload)
//    client.publish(channelName2, String(humidity).c_str()); 
//    Serial.println("Message Published");
    delay(1000);
  }
}
