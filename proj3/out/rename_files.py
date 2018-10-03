import os
import PIL.Image as Image
for file in os.listdir("."):
	if file.endswith(".png"):
		Image.open(file).convert("RGB").save(f"{file[:-4]}.jpg",'JPEG')
		os.remove(file)

