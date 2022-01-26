 
import torch
import torchvision
from torch.utils.data import DataLoader
 
def get_trans():
    # 设置一个转换的集合，先把数据转换到tensor，再归一化为均值.5，标准差.5的正态分布
    trans = torchvision.transforms.Compose(
        [
            torchvision.transforms.ToTensor(),  # ToTensor方法把[0,255]变成[0,1]
            torchvision.transforms.Normalize( [0.5], [0.5] )
            # 变成mean(均值)=0，std（标准差standard deviation）=1的分布
        ]
    )
    return trans
 
DOWNLOAD_MNIST=True
train_data = torchvision.datasets.MNIST( root="./mnist",  # 设置数据集的根目录
    train=True,  # 是否是训练集
    transform=get_trans(),  # 对数据进行转换
    download=DOWNLOAD_MNIST
                                         )
test_data = torchvision.datasets.MNIST( root="./mnist", train=False,  # 测试集，所以false
    transform=get_trans(), download=DOWNLOAD_MNIST
                                        )
def get_trainLoader(BATCH_SIZE):
    # 第二个参数是数据分块之后每一个块的大小，第三个参数是是否大乱数据
    train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
    return train_loader
 
def get_testLoader(BATCH_SIZE):
    test_loader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=False)
    return test_loader
 
def get_cuda_available():
    available=torch.cuda.is_available()
    return available
 
def get_test_data_len():
    return len(test_data)