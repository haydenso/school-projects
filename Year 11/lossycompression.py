# Exercise experimenting with lossy compression
from PIL import Image # Python image library... pip install pillow
import requests 

url = "https://apod.nasa.gov/apod/image/1908/5D4_5485seeley_1067.jpg"
response = requests.get(url)
# Check the download was successful, error message if not
if response.status_code != 200:
    print('Problem with download. Status code: ', response.status_code)
    exit()

# Save the file
with open('original.jpg', 'wb') as f:
    f.write(response.content)

# Open the image via PIL
image = Image.open("original.jpg")

# Create several versions of decreasing compression quality
for n in range(100,0,-10): # From 100 until 0, increments of -10
    quality = n
    image.save(f'quality-{quality}.jpg', optimize=True, quality=quality)