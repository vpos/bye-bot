import random
import json
import requests
import textwrap

from imgurpython import ImgurClient
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# slack token; do not upload to git
tokenFile = ''
with open('token.json') as json_file:
    tokenFile = json.load(json_file)
slack_webhook_url = tokenFile['slackHookUrl']
imgur_id = tokenFile['imgur_id']
imgur_secret = tokenFile['imgur_secret']

randomText = ['guys i cannot take it no more, srsly', 'i qimt, afectiv imedietly', 'much sad, very quit', 'goobdye crul dev worl', 'screw u guys, im out', 'sry guys, i qit']

def quits(name):
    randString = str(random.choice(randomText))
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
    now = datetime.now()
    today = datetime.today().date()
    today_datetime = today.strftime('%d.%m.%Y')
    draw.text((210, 300), f"Date: {today_datetime}", font=ImageFont.truetype('arial.ttf', size=10), fill='rgb(0, 0, 0)')

    # "signed"
    draw.text((210, 315), f"Signed: {name}", font=ImageFont.truetype('arial.ttf', size=10), fill='rgb(0, 0, 0)')

    image.save('cheems_quits.png')

    # upload img section
    client_id = imgur_id
    client_secret = imgur_secret

    client = ImgurClient(client_id, client_secret)
    response_upload = client.upload_from_path('cheems_quits.png', config=None, anon=True)

    print(f'{now}: Upload Response: {response_upload}')

    img_url = response_upload['link']

    payload = {
        "text": "I hereby submit my official resignation letter.",
    "attachments": [
        {
            "color": "#000000",
            "title": "Bye",
            "image_url": img_url
            }
        ]
    }

    response_slack = requests.post(slack_webhook_url, data=json.dumps(payload),
        headers={'Content-Type': 'application/json'})

    print(f'{now}: Slack Response: {response_slack}')

    return response_slack.content