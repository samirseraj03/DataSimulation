
from datetime import datetime , timedelta
import matplotlib.pyplot as plt
import io
import base64


def chop_microseconds(delta):
    return delta.replace(microsecond=0)
 

# Generar gráfico
def generate_chart(data):

    seconds = [row[3] for row in data]
    loss = [row[4] for row in data]

    plt.title("Simple grafic")
    plt.figure(figsize=(10, 6))

    plt.xlabel("Seconds")
    plt.ylabel("Loss")
    plt.plot(seconds, loss , marker='o')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')




