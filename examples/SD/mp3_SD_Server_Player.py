import network
import socket
import os
import gc

from machine import SDCard

# =========================
# SD CARD
# =========================

SD_CMD = 15
SD_D0 = 17
SD_D1 = 18
SD_D2 = 13
SD_D3 = 14
SD_CLK = 16

sd = SDCard(
    slot=1,
    width=4,
    cmd=SD_CMD,
    data=(SD_D0, SD_D1, SD_D2, SD_D3),
    sck=SD_CLK,
    freq=20000000
)

os.mount(sd, "/sd")

# =========================
# WIFI
# =========================

SSID = "WIFI"
PASSWORD = "22222222"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Conectando WiFi...")

while not wlan.isconnected():
    pass

ip = wlan.ifconfig()[0]

print("Conectado!")
print("IP:", ip)

# =========================
# SERVER
# =========================

addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(5)

print("Servidor listo")
print("Abrir en navegador:")
print("http://" + ip)

# =========================
# LOOP PRINCIPAL
# =========================

while True:

    gc.collect()

    client, addr = server.accept()

    print("Cliente:", addr)

    try:

        request = client.recv(4096).decode()

        print(request)

        # =========================================
        # MP3
        # =========================================

        if "GET /sd/" in request:

            ruta = request.split(" ")[1]

            archivo = ruta.replace("%20", " ")

            try:

                tamaño = os.stat(archivo)[6]

                inicio = 0

                # =================================
                # RANGE REQUEST
                # =================================

                if "Range: bytes=" in request:

                    rango = request.split("Range: bytes=")[1]
                    rango = rango.split("\r\n")[0]

                    inicio = int(rango.split("-")[0])

                restante = tamaño - inicio

                f = open(archivo, "rb")

                f.seek(inicio)

                # =================================
                # HEADERS
                # =================================

                header = (
                    "HTTP/1.1 206 Partial Content\r\n"
                    "Content-Type: audio/mpeg\r\n"
                    "Accept-Ranges: bytes\r\n"
                    "Content-Length: %d\r\n"
                    "Content-Range: bytes %d-%d/%d\r\n"
                    "Connection: close\r\n\r\n"
                ) % (
                    restante,
                    inicio,
                    tamaño - 1,
                    tamaño
                )

                client.send(header)

                # =================================
                # STREAM
                # =================================

                while True:

                    data = f.read(8192)

                    if not data:
                        break

                    try:
                        client.send(data)

                    except:
                        break

                f.close()

            except Exception as e:

                print("ERROR MP3:", e)

        # =========================================
        # HTML
        # =========================================

        else:

            client.send(
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n\r\n"
            )

            client.send("""
<!DOCTYPE html>
<html>

<head>

<meta charset="utf-8">

<title>ESP32 MP3</title>

<style>

body{
    background:#111;
    color:white;
    font-family:Arial;
    padding:20px;
}

.song{
    background:#222;
    padding:15px;
    margin-bottom:10px;
    border-radius:10px;
    cursor:pointer;
}

.song:hover{
    background:#333;
}

audio{
    width:100%;
    margin-bottom:20px;
}

</style>

</head>

<body>

<h1>ESP32 MP3</h1>

<audio id="player" controls preload="none"></audio>

""")

            archivos = os.listdir("/sd")

            for archivo in archivos:

                if archivo.endswith(".mp3"):

                    bloque = """
<div class="song" onclick="playSong('/sd/%s')">
%s
</div>
""" % (archivo, archivo)

                    client.send(bloque)

            client.send("""
<script>

const player = document.getElementById("player");

function playSong(url){

    // cortar stream actual
    player.pause();

    // vaciar source actual
    player.removeAttribute("src");

    player.load();

    // pequeño delay para cerrar socket anterior
    setTimeout(() => {

        player.src = url;

        player.load();

        player.play();

    }, 200);
}

</script>

</body>
</html>
""")

    except Exception as e:

        print("ERROR GENERAL:", e)

    try:
        client.close()
    except:
        pass
