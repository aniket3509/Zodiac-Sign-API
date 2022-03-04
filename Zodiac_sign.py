import datetime
from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['Get'])
def zodiac():
        date = datetime.datetime.now()
        day = int(date.strftime("%d"))
        month = date.strftime("%B")
        if month == 'December':
                astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
        elif month == 'January':
                astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
        elif month == 'February':
                astro_sign = 'Aquarius' if (day < 19) else 'pisces'
        elif month == 'March':
                astro_sign = 'Pisces' if (day < 21) else 'aries'
        elif month == 'April':
                astro_sign = 'Aries' if (day < 20) else 'taurus'
        elif month == 'May':
                astro_sign = 'Taurus' if (day < 21) else 'gemini'
        elif month == 'June':
                astro_sign = 'Gemini' if (day < 21) else 'cancer'
        elif month == 'July':
                astro_sign = 'Cancer' if (day < 23) else 'leo'
        elif month == 'August':
                astro_sign = 'Leo' if (day < 23) else 'virgo'
        elif month == 'September':
                astro_sign = 'Virgo' if (day < 23) else 'libra'
        elif month == 'October':
                astro_sign = 'Libra' if (day < 23) else 'scorpio'
        elif month == 'November':
                astro_sign = 'scorpio' if (day < 22) else 'sagittarius'

        astro_sign_dict = {'Sign': astro_sign} 
        astro_sign_json = json.dumps(astro_sign_dict)
        #print(astro_sign_json)
        return astro_sign_json

if ( __name__ == '__main__'):
        app.run(port=7777)

