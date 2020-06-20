import random
import json
import requests
import textwrap

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# slack token; do not upload to git
tokenFile = ''
with open('token.json') as json_file:
    tokenFile = json.load(json_file)
token = tokenFile['token']

randomText = ['guys i cannot take it no more, srsly', 'i qimt, afectivly imedietly', 'much sad, very quit', 'goobdye crul dev worl', 'screw u guys, im out', 'sry guys, i qit']
randString = str(random.choice(randomText))

def quits():
    image = Image.open('cheems.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=35)

    color_text = 'rgb(255, 255, 255)' # white
    color_stroke = 'rgb(0, 0, 0)' # black
    
    # thin border, standard text
    margin = 75
    offset = 150
    for line in textwrap.wrap(randString, width=15):
        draw.text((margin-1, offset), line, font=font, fill=color_stroke)
        draw.text((margin+1, offset), line, font=font, fill=color_stroke)
        draw.text((margin, offset-1), line, font=font, fill=color_stroke)
        draw.text((margin, offset+1), line, font=font, fill=color_stroke)
        draw.text((margin, offset), line, font=font, fill=color_text)
        offset += font.getsize(line)[1]

    # "date"
    today = datetime.today().date()
    today_datetime = today.strftime('%d.%m.%Y')
    draw.text((225, 300), f"Date: {today_datetime}", font=ImageFont.truetype('arial.ttf', size=10), fill='rgb(0, 0, 0)')

    # "signed"
    draw.text((225, 315), f"Signed: ", font=ImageFont.truetype('arial.ttf', size=10), fill='rgb(0, 0, 0)')

    image.save('cheems_quits.png')

    img = open('cheems_quits.png','rb').read()
    f = {"file": img}

    # slack handler
    payload = {
    "token": token,
    "channels": ["C012REL3YUW"],
    "text":"hey",
    "filename":"cheems_quits.png"}

    response = requests.post('https://slack.com/api/files.upload', params=payload, files=f)

    print(f'Slack Response: {response.content}')

    return response.content