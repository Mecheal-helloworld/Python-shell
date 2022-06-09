from PIL import Image
from torchvision import transforms

img = Image.open('F:\\学习\\毕业设计\\结题\\数据集\\Flavia\\1\\1001.jpg')
resize = transforms.Resize((400, 400))
img = resize(img)
toten = transforms.ToTensor()
img = toten(img)
print(img)
print(img.max())
imga = img==1
print(imga)

resize = transforms.Resize((550, 550))
img = resize(img)
resize = transforms.RandomCrop(448, padding=8)
img = resize(img)
resize = transforms.RandomHorizontalFlip()
img = resize(img)
img.save('C:\\Users\\ASUS\\Desktop\\1.jpg')