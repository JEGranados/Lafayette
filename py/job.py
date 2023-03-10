import time, serial, csv, os, json
from datetime import datetime

# Declare variables
arduino_port = "/dev/ttyUSB0"
baud = "9600"
usb="/media/alecasti/ESD-USB"

# Get current directory
dir = os.path.dirname(os.path.realpath(__file__))
csv_name = ""
json_name = ""
sensor_data = []

# Connect to Arduino
def connect():
    print("Connecting to Arduino...")
    while not os.path.exists(arduino_port):
        print("Waiting for Arduino...")
        time.sleep(1)
    arduino = serial.Serial(arduino_port, baud)
    print("Connected to Arduino")
    return arduino

# Save data to CSV
def saveCSV():
    with open(csv_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sensor_data)
    f.close()

# Save data to JSON
def saveJson():  
    
    jsonstr = {
        "time": sensor_data[-1][0],
        "sensor": sensor_data[-1][1],
        "val": int((sensor_data[-1][2])),
        "on": not bool(sensor_data[-1][3])
    }
    with open(json_name, 'a', encoding='UTF8') as f:
        json.dump(jsonstr,f)
        f.write('\n')
    f.close()

# Get data from Arduino
def getData():
    try: 
        dataPuerto=arduino.readline()
        dataString = dataPuerto.decode('utf-8')
        data=dataString[0:][:-2]
        readings = data.split(",")
        timestamp = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        readings.insert(0, timestamp)
        sensor_data.append(readings)
        print("Saving data...")
        saveCSV()
        saveJson()
    except Exception as e:
        #print(e)
        raise "Arduino not connected"

def checkUSB():
    if os.path.exists(usb):
        print("USB connected")
        return True
    else:
        print("USB not connected")
        return False

def copy():
   if checkUSB():
        print("Copying files...")
        os.system("cp " + dir + "/*.csv " + usb)
        os.system("cp " + dir + "/*.json " + usb)
        print("Files copied")
        os.system("rm " + dir + "/*.csv")
        os.system("rm " + dir + "/*.json")


# Main loop
while True:
    arduino = connect()
    sensor_data.clear()
    filedataname = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    csv_name= dir + "/data " + filedataname + ".csv"
    json_name= dir + "/data " + filedataname + ".json"

    # collect the samples
    try:
        while arduino.is_open == True:
            getData()        
              
    except:
        print("Data collection complete!") 
        arduino.close()
        copy()
   

        


   
