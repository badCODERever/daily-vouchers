from PIL import Image
im=Image.open('E:\\random.png')
print(im.mode)
if not im.mode == 'RGB':
  im = im.convert('RGB')
im.convert('RGB')
print(im.mode)
im.save(
