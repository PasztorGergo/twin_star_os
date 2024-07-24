from bluedot.btcomm import BluetoothClient

ENGINEAR_MAC = "2C:CF:67:1B:D9:91"

def on_received(enginear_db):
    astro_db = None
    with open("db.txt") as fp:
        fp.readline();
        astro_db = fp.readline().replace("\n", "")

    if enginear_db == "req" or enginear_db.split("\t")[-1] == "con":
        client.send(astro_db)

    with open("db.txt", "w") as fp:
        fp.write(f"{enginear_db}\n{astro_db}")
    
def update_to_enginear():
    with open("db.txt") as fp:
        fp.readline();
        astro_db = fp.readline().replace("\n", "")
        client.send(astro_db)

def req_to_enginear():
    client.send("req")

client = BluetoothClient(ENGINEAR_MAC,on_received)