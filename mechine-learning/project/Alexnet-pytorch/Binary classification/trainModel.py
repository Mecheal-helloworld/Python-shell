from AlexNet import alexNet
from keras import Model
from keras.callbacks import ModelCheckpoint
from keras.utils import to_categorical
from keras.layers import Flatten, Dense, Input
from keras.layers import Convolution2D, MaxPooling2D
from keras.preprocessing import image
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import concatenate
import pandas
from keras.optimizers import SGD,Adam,RMSprop
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
import cv2
import os


IMG_CHANNELS=3 #PGB图像为三通道 R、G、B
#weight_decay = 0.0005 
IMG_ROWS=224  #图像的行像素
IMG_COLS=224  #图像的列像素
BATCH_SIZE=64 #batch大小
NB_EPOCH=10   #循环次数
NB_CLASSES=2  #分类  猫和狗两种
VERBOSE=1
#VALIDATION_SPLIT=0.2
#OPTIM=RMSprop()
x_test=np.empty((200,IMG_ROWS,IMG_COLS,3),np.float16)  #测试集两百张（200， 224， 224， 3）
x_train=np.empty((500,IMG_ROWS,IMG_COLS,3),np.float16)  #训练集五百张（500， 224， 224， 3）
train_data=np.zeros(500)  #训练集标签
test_data=np.zeros(200)  #测试集标签
#读入训练样本
for i in range(500):
    if i<250:
		#载入250张猫
        train_data[i]=1#猫的标签就是1
		#dog.8
        imagepath = "D:/python_pro/deep_learning_al/data/train/cats/cat." + str(i)+ ".jpg"#猫照片存储路径
        image1 = cv2.imread(imagepath)  #读入文件
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)  #转为RGB
        image1 = cv2.resize(image1,(IMG_ROWS,IMG_COLS))  #重新定义形状为（224， 224）
        #plt.imshow(image1)
        #plt.show()
        x_train[i,:,:,:]=image1   #训练集矩阵，四维（500， 224， 224， 3）

    else:
		#载入250张狗
        train_data[i]=0#狗的标签就是0
        imagepath = "D:/python_pro/deep_learning_al/data/train/dogs/dog." + str(i - 250)+ ".jpg" #狗照片路径
        image1 = cv2.imread(imagepath)  #读入文件
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)#转为RGB
        image1 = cv2.resize(image1, (IMG_ROWS, IMG_COLS))#重新定义形状为（224， 224）
        x_train[i, :, :, :] = image1 #训练集矩阵，四维（500， 224， 224， 3）
y_train=to_categorical(train_data) #训练集标签（500， 2）
x_train=np.array(x_train)  #完整训练集矩阵
#读入测试样本
for i in range(200):
    if i<100:
		#载入100张猫
        test_data[i]=1#猫的标签就是1
        imagepath =  "D:/python_pro/deep_learning_al/data/test/cats/cat."+str(i+250)+'.jpg'#猫照片存储路径
        image1 = cv2.imread(imagepath)#读入文件
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)#转为RGB
        image1 = cv2.resize(image1,(IMG_ROWS,IMG_COLS)) #重新定义形状为（224， 224）
        x_test[i,:,:,:]=image1

    else:
		#载入100张狗
        test_data[i]=0#狗的标签就是0
        imagepath=  "D:/python_pro/deep_learning_al/data/test/dogs/dog."+str(i+250-100)+'.jpg'#狗照片路径
        image1 = cv2.imread(imagepath)#读入文件
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)#转为RGB
        image1 = cv2.resize(image1, (IMG_ROWS, IMG_COLS))#重新定义形状为（224， 224）
        x_test[i, :, :, :] = image1
y_test=to_categorical(test_data) #测试集标签（200， 2）
#print(sys.getsizeof(x_test),sys.getsizeof(y_test))
x_test=np.array(x_test) #完整测试集矩阵（200， 224， 224， 3）
#归一化
#x_train.shape = (500, 224, 224, 3)
#x_test.shape = (200, 224, 224, 3)
x_train=x_train/255  #像素是8位的，所以0-255编程0-1除以255即可。
x_test = x_test/255

print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
# #数据多样化

# batch_size = 16

# train_datagen = ImageDataGenerator(
        # rescale=1./255,
        # shear_range=0.2,
        # zoom_range=0.2,
        # horizontal_flip=True)

# test_datagen = ImageDataGenerator(rescale=1./255)

# train_generator = train_datagen.flow_from_directory(
        # 'D:\python项目\deep_learning_al\train1', 
        # target_size=(224, 224),  
        # batch_size=batch_size,
        # class_mode='categorical')

# validation_generator = test_datagen.flow_from_directory(
        # 'D:\python项目\deep_learning_al\validation',
        # target_size=(224, 224),
        # batch_size=batch_size,
        # class_mode='categorical')	
		
		
		
input_shape = (224, 224, 3)

"""
创建alexnet网络模型
"""

#分类数量
nb_classes = 2

model = alexNet()

#检查保存断点文件夹是否存在,没有的话就创建一个

if not os.path.exists('alex_net_checkpoints'):
	os.mkdir('alex_net_checkpoints')
	
#优化使用随机梯度下降

AlexNet.compile(loss = 'categorical_crossentropy', optimizer = sgd, metrics = ['accuracy'])

checkpoint = ModelCheckpoint(monitor = 'val_acc', 
				filepath = "weights.best.hdf5",
				verbose = 1,
				mode = 'max',
				save_best_only = True)
							
							
#开始训练网络
AlexNet.fit(x_train, y_train, 
			batch_size = 64, 
			epochs = 5, 
			verbose = 1, 
			validation_data = (x_test, y_test),
			callbacks = [checkpoint]
			)
				
score = AlexNet.evaluate(x_test, y_test, verbose = 0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
# #训练模型，训练结果保存在history-callback中
# history_callback = AlexNet.fit_generator(
										# train_generator,
										# steps_per_epoch = 2000,
										# epochs = 80,
										# validation_data = validation_generator,
										# validation_steps = 800
										# )
										
# #训练完存储训练的结果和模型中的权重参数
# pandas.DataFrame(history_callback.history).to_csv('.\AlexNet_model.csv')
# AlexNet.save_weights('.\AlexNet_model.h5')
