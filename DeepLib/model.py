import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(1)

GROUP_SIZE = 3

class Net(nn.Module):
    #This defines the structure of the NN.
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3,bias = False)
        self.conv2 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv3 = nn.Conv2d(16, 32, kernel_size=3,bias = False)
        self.conv4 = nn.Conv2d(32, 16, kernel_size=1,bias = False)
        self.conv5 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv6 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv7 = nn.Conv2d(16, 16, padding = 1, kernel_size=3,bias = False)
        self.conv8 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv9 = nn.Conv2d(16, 10, kernel_size=1,bias = False)
        self.batch1 = nn.BatchNorm2d(16)
        self.batch2 = nn.BatchNorm2d(16)
        self.batch3 = nn.BatchNorm2d(32)
        self.batch4 = nn.BatchNorm2d(16)
        self.batch5 = nn.BatchNorm2d(16)
        self.batch6 = nn.BatchNorm2d(16)
        self.batch7 = nn.BatchNorm2d(16)
        self.batch8 = nn.BatchNorm2d(16)
        self.pool = nn.MaxPool2d(2,2)
        self.dropout1 = nn.Dropout2d(0.1)
        self.dropout2 = nn.Dropout2d(0.1)
        self.dropout3 = nn.Dropout2d(0.1)
        self.dropout4 = nn.Dropout2d(0.1)
        self.dropout5 = nn.Dropout2d(0.1)
        self.dropout6 = nn.Dropout2d(0.1)
        self.dropout7 = nn.Dropout2d(0.1)
        self.avgpool = nn.AvgPool2d(5)

    def forward(self, x):
        x = self.dropout1(self.batch1(F.relu(self.conv1(x))))
        x = self.dropout2(self.batch2(F.relu(self.conv2(x))))
        x = self.dropout3(self.batch3(F.relu(self.conv3(x))))
        x = self.pool(F.relu(self.conv4(x)))
        x = self.dropout4(self.batch4(F.relu(self.conv5(x))))
        x = self.dropout5(self.batch5(F.relu(self.conv6(x))))
        x = self.dropout6(self.batch6(F.relu(self.conv7(x))))
        x = self.dropout7(self.batch7(F.relu(self.conv8(x))))
        x = self.avgpool(self.conv9(x))
        x = x.view(-1,10)

        return F.log_softmax(x, dim=1)

class Net1(nn.Module):
    #This defines the structure of the NN.
    
    def __init__(self):
        super(Net1, self).__init__()
        DROPOUT =0.1
        self.conv1 = nn.Conv2d(1, 12, kernel_size=3,bias = False)
        self.conv2 = nn.Conv2d(12, 12, kernel_size=3,bias = False)
        self.conv3 = nn.Conv2d(12, 20, kernel_size=3,bias = False)
        self.conv4 = nn.Conv2d(20, 16, kernel_size=1,bias = False)
        self.conv5 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv6 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv7 = nn.Conv2d(16, 16, padding = 1, kernel_size=3,bias = False)
        self.conv8 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv9 = nn.Conv2d(16, 10, kernel_size=1,bias = False)
        self.batch1 = nn.BatchNorm2d(12)
        self.batch2 = nn.BatchNorm2d(12)
        self.batch3 = nn.BatchNorm2d(20)
        self.batch4 = nn.BatchNorm2d(16)
        self.batch5 = nn.BatchNorm2d(16)
        self.batch6 = nn.BatchNorm2d(16)
        self.batch7 = nn.BatchNorm2d(16)
        self.batch8 = nn.BatchNorm2d(16)
        self.pool = nn.MaxPool2d(2,2)
        self.dropout1 = nn.Dropout2d(DROPOUT)
        self.dropout2 = nn.Dropout2d(DROPOUT)
        # self.dropout3 = nn.Dropout2d(DROPOUT)
        self.dropout4 = nn.Dropout2d(DROPOUT)
        self.dropout5 = nn.Dropout2d(DROPOUT)
        # self.dropout6 = nn.Dropout2d(DROPOUT)
        # self.dropout7 = nn.Dropout2d(DROPOUT)
        self.avgpool = nn.AvgPool2d(5)

    def forward(self, x):
        x = self.dropout1(self.batch1(F.relu(self.conv1(x))))
        x = self.dropout2(self.batch2(F.relu(self.conv2(x))))
        x = self.batch3(F.relu(self.conv3(x)))
        x = self.pool(F.relu(self.conv4(x)))
        x = self.dropout4(self.batch4(F.relu(self.conv5(x))))
        x = self.dropout5(self.batch5(F.relu(self.conv6(x))))
        x = self.batch6(F.relu(self.conv7(x)))
        x = self.batch7(F.relu(self.conv8(x)))
        x = self.avgpool(self.conv9(x))
        x = x.view(-1,10)

        return F.log_softmax(x, dim=-1)

class Net3(nn.Module):
    #This defines the structure of the NN.
    
    def __init__(self):
        DROPOUT_VALUE = 0
        super(Net3, self).__init__()
        self.conv1 = nn.Conv2d(1, 7, kernel_size=3,bias = False)
        self.conv2 = nn.Conv2d(7, 16, kernel_size=3,bias = False)
        # self.conv3 = nn.Conv2d(12, 12, kernel_size=3,bias = False)
        self.conv4 = nn.Conv2d(16, 12, kernel_size=1,bias = False)
        self.conv5 = nn.Conv2d(12, 16, kernel_size=3,bias = False)
        self.conv6 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv7 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        # self.conv8 = nn.Conv2d(11, 11, kernel_size=3,bias = False)
        self.conv9 = nn.Conv2d(16, 10, kernel_size=1,bias = True)
        self.batch1 = nn.BatchNorm2d(7)
        self.batch2 = nn.BatchNorm2d(16)
        self.batch3 = nn.BatchNorm2d(16)
        self.batch4 = nn.BatchNorm2d(16)
        self.batch5 = nn.BatchNorm2d(16)
        self.batch6 = nn.BatchNorm2d(16)
        self.batch7 = nn.BatchNorm2d(16)
        # self.batch8 = nn.BatchNorm2d(8)
        self.pool = nn.MaxPool2d(2,2)
        self.dropout1 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout2 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout3 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout4 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout5 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout6 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout7 = nn.Dropout2d(DROPOUT_VALUE)
        self.avgpool = nn.AvgPool2d(5)

    def forward(self, x):
        x = self.dropout1(self.batch1(F.relu(self.conv1(x))))
        x = self.dropout2(self.batch2(F.relu(self.conv2(x))))
        # x = self.dropout3(self.batch3(F.relu(self.conv3(x))))
        x = self.pool(F.relu(self.conv4(x)))
        x = self.dropout4(self.batch4(F.relu(self.conv5(x))))
        x = self.dropout5(self.batch5(F.relu(self.conv6(x))))
        x = self.dropout6(self.batch6(F.relu(self.conv7(x))))
        # x = self.dropout7(self.batch7(F.relu(self.conv8(x))))
        x = self.avgpool(self.conv9(x))
        x = x.view(-1,10)

        return F.log_softmax(x, dim=-1)

class Net2(nn.Module):
    #This defines the structure of the NN.
    
    def __init__(self):
        DROPOUT_VALUE = 0.1
        super(Net2, self).__init__()
        self.conv1 = nn.Conv2d(1, 7, kernel_size=3,bias = False)
        self.conv2 = nn.Conv2d(7, 16, kernel_size=3,bias = False)
        # self.conv3 = nn.Conv2d(12, 12, kernel_size=3,bias = False)
        self.conv4 = nn.Conv2d(16, 12, kernel_size=1,bias = False)
        self.conv5 = nn.Conv2d(12, 16, kernel_size=3,bias = False)
        self.conv6 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        self.conv7 = nn.Conv2d(16, 16, kernel_size=3,bias = False)
        # self.conv8 = nn.Conv2d(11, 11, kernel_size=3,bias = False)
        self.conv9 = nn.Conv2d(16, 10, kernel_size=1,bias = False)
        self.batch1 = nn.BatchNorm2d(7)
        self.batch2 = nn.BatchNorm2d(16)
        self.batch3 = nn.BatchNorm2d(16)
        self.batch4 = nn.BatchNorm2d(16)
        self.batch5 = nn.BatchNorm2d(16)
        self.batch6 = nn.BatchNorm2d(16)
        self.batch7 = nn.BatchNorm2d(16)
        # self.batch8 = nn.BatchNorm2d(8)
        self.pool = nn.MaxPool2d(2,2)
        self.dropout1 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout2 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout3 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout4 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout5 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout6 = nn.Dropout2d(DROPOUT_VALUE)
        self.dropout7 = nn.Dropout2d(DROPOUT_VALUE)
        self.avgpool = nn.AvgPool2d(5)

    def forward(self, x):
        x = self.dropout1(self.batch1(F.relu(self.conv1(x))))
        x = self.dropout2(self.batch2(F.relu(self.conv2(x))))
        # x = self.dropout3(self.batch3(F.relu(self.conv3(x))))
        x = self.pool(F.relu(self.conv4(x)))
        x = self.dropout4(self.batch4(F.relu(self.conv5(x))))
        x = self.dropout5(self.batch5(F.relu(self.conv6(x))))
        x = self.dropout6(self.batch6(F.relu(self.conv7(x))))
        # x = self.dropout7(self.batch7(F.relu(self.conv8(x))))
        x = self.avgpool(self.conv9(x))
        x = x.view(-1,10)

        return F.log_softmax(x, dim=-1)


class Block(nn.Module):
    def __init__(self, input_size, output_size, padding=1, norm='bn', usepool=True, miniblock = False):
        """Initialize Block

        Args:
            input_size (int): Input Channel Size
            output_size (int): Output Channel Size
            padding (int, optional): Padding to be used for convolution layer. Defaults to 1.
            norm (str, optional): Type of normalization to be used. Allowed values ['bn', 'gn', 'ln']. Defaults to 'bn'.
            usepool (bool, optional): Enable/Disable Maxpolling. Defaults to True.
        """
        super(Block, self).__init__()
        self.usepool = usepool
        self.conv1 = nn.Conv2d(input_size, output_size, 3, padding=padding)
        if norm == 'bn':
            self.n1 = nn.BatchNorm2d(output_size)
        elif norm == 'gn':
            self.n1 = nn.GroupNorm(GROUP_SIZE, output_size)
        elif norm == 'ln':
            self.n1 = nn.GroupNorm(1, output_size)
        self.conv2 = nn.Conv2d(output_size, output_size, 3, padding=padding)
        if norm == 'bn':
            self.n2 = nn.BatchNorm2d(output_size)
        elif norm == 'gn':
            self.n2 = nn.GroupNorm(GROUP_SIZE, output_size)
        elif norm == 'ln':
            self.n2 = nn.GroupNorm(1, output_size)
        self.conv3 = nn.Conv2d(output_size, output_size, 3, padding=padding)
        self.trans1 = nn.Conv2d(output_size, output_size, 1)
        self.trans2 = nn.Conv2d(output_size, output_size, 1)
        self.trans3 = nn.Conv2d(output_size, output_size, 1)
        if norm == 'bn':
            self.n3 = nn.BatchNorm2d(output_size)
        elif norm == 'gn':
            self.n3 = nn.GroupNorm(GROUP_SIZE, output_size)
        elif norm == 'ln':
            self.n3 = nn.GroupNorm(1, output_size)
        if usepool:
            self.pool = nn.MaxPool2d(2, 2)
        self.trans_mapping = {1:self.trans1,2:self.trans2,3:self.trans3}

    def __call__(self, x,mapping, layers=3):
        """
        Args:
            x (tensor): Input tensor to this block
            layers (int, optional): Number of layers in this block. Defaults to 3.

        Returns:
            tensor: Return processed tensor
        """
        x = self.conv1(x)
        x = self.n1(x)
        x = F.relu(x)
        if layers >= 2:
            x = self.conv2(x)
            x = self.n2(x)
            x = F.relu(x)
        if layers >= 3:
            x = self.conv3(x)
            x = self.n3(x)
            x = F.relu(x)
        # if mapping ==1:
        #     x = self.trans1(x)
        # if mapping ==2:
        #     x = self.trans2(x)
        # if mapping ==3:
        #     x = self.trans3(x)
        if self.usepool:
            x = self.trans_mapping[mapping](x)
            x = self.pool(x)
        return x


class CifarNet(nn.Module):
    """ Network Class

    Args:
        nn (nn.Module): Instance of pytorch Module
    """

    def __init__(self, base_channels=12, layers=3, drop=0.05, norm='bn'):
        """Initialize Network

        Args:
            base_channels (int, optional): Number of base channels to start with. Defaults to 4.
            layers (int, optional): Number of Layers in each block. Defaults to 3.
            drop (float, optional): Dropout value. Defaults to 0.01.
            norm (str, optional): Normalization type. Defaults to 'bn'.
        """
        super(CifarNet, self).__init__()

        self.base_channels = base_channels
        self.drop = drop
        self.no_layers = layers

        # Conv
        self.block1 = Block(3, self.base_channels, norm=norm)
        self.dropout1 = nn.Dropout(self.drop)
        self.block2 = Block(self.base_channels,
                            self.base_channels*2, norm=norm)
        self.dropout2 = nn.Dropout(self.drop)
        self.block3 = Block(self.base_channels*2,
                            self.base_channels*2, norm=norm, usepool=False)
        self.dropout3 = nn.Dropout(self.drop)

        self.gap = nn.AdaptiveAvgPool2d(1)
        self.flat = nn.Conv2d(self.base_channels*2, 10, 1)

    def forward(self, x, dropout=True):
        """Convolution function

        Args:
            x (tensor): Input image tensor
            dropout (bool, optional): Enable/Disable Dropout. Defaults to True.

        Returns:
            tensor: tensor of logits
        """
        # Conv Layer
        x = self.block1(x, layers=self.no_layers-1,mapping=1)
        if dropout:
            x = self.dropout1(x)
        x = self.block2(x, layers=self.no_layers,mapping=2)
        if dropout:
            x = self.dropout2(x)
        x = self.block3(x, layers=self.no_layers,mapping=3)

        # Output Layer
        x = self.gap(x)
        x = self.flat(x)
        x = x.view(-1, 10)

        # Output Layer
        return F.log_softmax(x, dim=1)


class NetInitial(nn.Module):
    def __init__(self):
        super(NetInitial, self).__init__()
        self.conv1 = nn.Sequential(nn.Conv2d(1, 8, 3)) 
        self.conv2= nn.Sequential(nn.Conv2d(8, 8, 3))
        self.conv3= nn.Sequential(nn.MaxPool2d(2, 2),nn.Conv2d(8, 16, 1))
        self.conv4 = nn.Sequential(nn.Conv2d(16, 16, 3))
        self.conv5 = nn.Sequential(nn.Conv2d(16, 16, 3))
        self.conv6 = nn.Sequential(nn.MaxPool2d(2, 2),nn.Conv2d(16, 32, 1))
        self.conv7 = nn.Sequential(nn.Conv2d(32, 32, 3))
        self.conv8= nn.Sequential(nn.Conv2d(32, 10, 2))
    def forward(self, x, dropout=False):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = F.relu(self.conv5(x))
        x = F.relu(self.conv6(x))
        x = F.relu(self.conv7(x))
        x = self.conv8(x)

        # x = F.relu(self.conv1(x), 2) # 28>26 | 1>3 | 1>1
        # x = F.relu(F.max_pool2d(self.conv2(x), 2)) #26>24>12 | 3>5>6 | 1>1>2
        # x = F.relu(self.conv3(x), 2) # 12>10 | 6>10 | 2>2
        # x = F.relu(F.max_pool2d(self.conv4(x), 2)) # 10>8>4 | 10>14>16 | 2>2>4

        x = x.view(-1, 10)
        return F.log_softmax(x, dim=1)