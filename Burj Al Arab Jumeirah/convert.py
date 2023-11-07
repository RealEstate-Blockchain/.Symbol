from PIL import Image
image = "ark/kpilaz-27dubai7large.webp"
im = Image.open(image).convert("RGB")
im.save("out.png","png")
