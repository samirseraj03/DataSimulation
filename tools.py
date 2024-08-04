
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




if __name__ == '__main__':

    data = [
    [6, "SIM789", "MACHINE_B", 10, 0.55],
    [7, "SIM789", "MACHINE_B", 20, 0.5],
    [8, "SIM789", "MACHINE_B", 30, 0.45],
    [9, "SIM789", "MACHINE_B", 40, 0.4],
    [10, "SIM789", "MACHINE_B", 50, 0.35]
]

    print(generate_chart(data))


    # list = {
    #    'simulation_id' : 'SAM105',
    #    'name' : 'For IA' ,
    #    'status' : 'Pending',
    #    'start_date' : chop_microseconds(datetime.today()),
    #    'end_date' : chop_microseconds(datetime.today() + datetime.timedelta(days = 1) ),
    #    'machine_id' : 'MACHINE_F'
    # }

    # print (list)
    # print (chop_microseconds(datetime.today()))
