import torch.nn as nn
import torch
import time
import tools
 
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1=nn.Sequential(
            nn.Conv2d(          #(1,28,28)
                in_channels=1,
                out_channels=16,
                kernel_size=5,
                stride=1,
                padding=2   #padding=(kernelsize-stride)/2
            ),#(16,28,28)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)#(16,14,14)
 
        )
        self.conv2=nn.Sequential(#(16,14,14)
            nn.Conv2d(16,32,5,1,2),#(32,14,14)
            nn.ReLU(),#(32,14,14)
            nn.MaxPool2d(2)#(32,7,7)
        )
        self.out=nn.Linear(32*7*7,10)
    def forward(self,x):
        x = self.conv1( x )
        x = self.conv2( x ) #(batch,32,7,7)
        x=x.view(x.size(0),-1) #(batch,32*7*7)
        output=self.out(x)
        return output
print("start")
EPOCH=50#总的训练次数
BATCH_SIZE=20#批次的大小
LR=0.03#学习率#交叉熵损失函数不需要太大的学习率
DOWNLOAD_MNIST=False#运行代码的时候是否下载数据集
 
 
cnn=CNN()
cuda_available=tools.get_cuda_available()
if cuda_available==True:
    cnn.cuda()
 
optimizer=torch.optim.Adam(cnn.parameters(),lr=LR)
loss_function=nn.CrossEntropyLoss()
 
train_loader=tools.get_trainLoader(BATCH_SIZE)
test_loader=tools.get_testLoader(BATCH_SIZE*10)
 
 
 
#训练过程
for ep in range(EPOCH):
    # 记录把所有数据集训练+测试一遍需要多长时间
    startTick = time.clock()
    for data in train_loader:  # 对于训练集的每一个batch
        img, label = data
        if cuda_available:
            img = img.cuda()
            label = label.cuda()
 
        out = cnn( img )  # 送进网络进行输出
        loss = loss_function( out, label )  # 获得损失
 
        optimizer.zero_grad()  # 梯度归零
        loss.backward()  # 反向传播获得梯度，但是参数还没有更新
        optimizer.step()  # 更新梯度
 
    num_correct = 0  # 正确分类的个数，在测试集中测试准确率
    for data in test_loader:
        img, label = data
        if cuda_available:
            img = img.cuda()
            label = label.cuda()
 
        out = cnn( img )  # 获得输出
 
        _, prediction = torch.max( out, 1 )
        # torch.max()返回两个结果，
        # 第一个是最大值，第二个是对应的索引值；
        # 第二个参数 0 代表按列取最大值并返回对应的行索引值，1 代表按行取最大值并返回对应的列索引值。
        num_correct += (prediction == label).sum()  # 找出预测和真实值相同的数量，也就是以预测正确的数量
 
    accuracy = num_correct.cpu().numpy() / tools.get_test_data_len()  # 计算正确率，num_correct是gpu上的变量，先转换成cpu变量
    timeSpan = time.clock() - startTick
    print( "第%d迭代期，准确率为%f,耗时%dS" % (ep + 1, accuracy, timeSpan) )