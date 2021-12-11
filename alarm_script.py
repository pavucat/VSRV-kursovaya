import paho.mqtt.client as mqtt
import smtplib

HOST = "192.168.56.101"
PORT = 1883

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('home.id14562443.alarm@gmail.com', '89104057638')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

   

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    if payload == "1":
        smtpObj.sendmail("home.id14562443.alarm@gmail.com", "andrey150791@gmail.com", "Alarms have been triggered!")
        print("Alarms have been triggered!")
    else:
        print("received message: "+payload)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT)
    client.subscribe("/home/sensors/motion_alarm")

    client.loop_forever()


if __name__ == "__main__":
    main()
