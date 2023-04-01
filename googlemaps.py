import pywhatkit    #conda activate pywhatkit_ent, conda deactivate
import random

lat = random.uniform(-90, 90)
lng = random.uniform(-180, 180)
x = "https://www.google.com/maps/search/?api=1&query={},{}".format(lat, lng)

pywhatkit.sendwhatmsg_instantly(
    phone_no="phone number",
    message=(f'{x}')
)