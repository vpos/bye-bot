import random
import json
import requests
import textwrap

from PIL import Image, ImageDraw, ImageFont

token = ""

randomText = ['guys i cannot take it no more, srsly', 'i qit', 'much sad, very quit', 'goobdye crul dev worl', 'screw u guys, im out', 'sry guys, i qit']
randString = str(random.choice(randomText))

image = Image.open('cheems.png')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=35)

color_text = 'rgb(255, 255, 255)' # white
color_stroke = 'rgb(0, 0, 0)' # black
 
# thin border
margin = 75
offset = 150
for line in textwrap.wrap(randString, width=15):
    draw.text((margin-1, offset), line, font=font, fill=color_stroke)
    draw.text((margin+1, offset), line, font=font, fill=color_stroke)
    draw.text((margin, offset-1), line, font=font, fill=color_stroke)
    draw.text((margin, offset+1), line, font=font, fill=color_stroke)
    draw.text((margin, offset), line, font=font, fill=color_text)
    offset += font.getsize(line)[1]

image.save('cheems_quits.png')

img = open('cheems_quits.png','rb').read()
f = {"file": img}

payload = {
"token": token,
"channels": ["C012REL3YUW"],
"text":"hey",
"filename":"cheems_quits.png"}

response = requests.post('https://slack.com/api/files.upload', params=payload, files=f)

print(f'Slack Response: {response.content}')