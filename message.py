import pywhatkit    #conda activate pywhatkit_ent, conda deactivate
import random

random_word_list = ['Kuzum', 'Bebeğim', 'Canim',
                    'Balim', 'Tatlim', 'Hayatim', 'Aşkim', 'Kuşum']
random_number = random.randint(3, 5)
int = random.sample(random_word_list, random_number)
for x in int:
    print(x)
    pywhatkit.sendwhatmsg_instantly(
            phone_no="+905367028874",
            message=(f'{x}')
)
