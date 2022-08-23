import serial
import time
import serial.tools.list_ports
portData = serial.tools.list_ports.comports()
print(len(portData))

for i in portData:
    print(i)

def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports

def findArduino(portsFound):

    commPort =""
    newConnection = len(portsFound)

    for i in range(0,newConnection):
        port = portsFound[i]
        strPort = str(port)

        if 'Arduino' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
            break

    return commPort

def arduinodata():

    ser = serial.Serial('COM3',9600)
    time.sleep(2)
    for i in range(50):
        line = ser.readline().decode()
        print(str(line))
        '''
        if line:
            string = line.decode()
            print(string)
            '''

    ser.close()

if __name__ == '__main__':

     arduinodata()

