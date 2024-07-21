#sudo rfcomm connect hci0 MAC-ADDR
import serial
import json

enginear = serial.Serial("/dev/rfcomm0",115200)

while(True):
    enginear_data = serial.readline().decode("ascii")
    enginear_db = None
    astro_db = None
    with open("db.txt") as fp:
        enginear_db = fp.readline().replace("\n", "").split("\t")
        astro_db = fp.readline().replace("\n", "")

        status = json.loads(enginear_data)
        enginear_db[0] = int(status["id"])
        enginear_db[1] = eval(status["eye"])
        enginear_db[2] = eval(status["lips"])
        enginear_db[3] = eval(status["rave"])
        enginear_db[4] = eval(status["patriotism"])
    with open("db.txt", "w") as fp:
        fp.write(f"{enginear_db}\n{"\t".join(astro_db)}")
