import paho.mqtt.client as mqtt #импорт библиотеки paho
import smtplib #импорт библиотеки smtplib

HOST = "192.168.0.104" #адрес брокера
PORT = 1883 #порт подключения к брокеру (стандартный порт протокола MQTT

smtpObj = smtplib.SMTP('smtp.gmail.com', 587) #создание объекта класса SMTP для подключения к серверу
smtpObj.starttls()#так как подключение идёт через 587 порт, включаем шифрование
smtpObj.login('home.id14562443.alarm@gmail.com', '89104057638')# вход в учётную запись для отправки сообщения

def on_connect(client, userdata, flags, rc): #данная функция вызывается сразу после попытки установки соединения с брокером
    print("Connected with result code " + str(rc)) #вывод результата попытки соединения с брокером

   

def on_message(client, userdata, msg): #данная функция вызывается при приходе сообщения в топик, на который подписан данный клиент
    payload = msg.payload.decode() #переводим пришедшее сообщение в формат строки
    if payload == "1": #условие "если входящее сообщение - "1""
        smtpObj.sendmail("home.id14562443.alarm@gmail.com", "andrey150791@gmail.com", "Alarms have been triggered!")#отправка сообщения на указанную почту
        print("Alarms have been triggered!") #вывод в консоль сообщения о тревоге
    else:
        print("received message: "+payload) #вывод в консоль пришедшего сообщения

def main():
    client = mqtt.Client() #создание клиента MQTT
    client.on_connect = on_connect #добавление функции on_connect
    client.on_message = on_message #добавление функции on_message
    client.connect(HOST, PORT) #попытка подключения к брокеру
    client.subscribe("/home/sensors/motion_alarm") #подписка на топик датчика

    client.loop_forever()#функция loop_forever() нужна для беспрерывного подключения к брокеру до вызова функции disconnect()


if __name__ == "__main__": #функция main(будет вызываться только если скрипт запущен напрямую, а не импортирован
    main()
