from PIL import Image, ImageDraw

hostFile = Image.open('a.png')


for i in range(0,512):
	for j in range(0,512):
		a = hostFile.getpixel((i,j))
		if a[3]!=255:
			print chr(a[3])
