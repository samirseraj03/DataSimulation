
from datetime import datetime , timedelta
import re


def chop_microseconds(delta):
    return delta.replace(microsecond=0)
       

def parse_multipart_form_data(data):
    """Parses multipart/form-data encoded data into a JSON object.

    Args:
        data: The multipart/form-data encoded data as a string.

    Returns:
        A dictionary representing the parsed form data.
    """

    boundary = re.search(r"boundary=(.*)", data, re.DOTALL).group(1)
    parts = data.split(f"--{boundary}")

    form_data = {}
    for part in parts[1:-1]:
        lines = part.splitlines()
        name = re.search(r'name="(.*)"', lines[1]).group(1)
        value = "\n".join(lines[2:-2])
        form_data[name] = value

    return form_data



if __name__ == '__main__':


    list = {
       'simulation_id' : 'SAM105',
       'name' : 'For IA' ,
       'status' : 'Pending',
       'start_date' : chop_microseconds(datetime.today()),
       'end_date' : chop_microseconds(datetime.today() + datetime.timedelta(days = 1) ),
       'machine_id' : 'MACHINE_F'
    }

    print (list)
    print (chop_microseconds(datetime.today()))
