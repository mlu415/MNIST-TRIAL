import torch.nn as nn
import torch.nn.functional as F
import torch
# The network should inherit from the nn.Module
class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        # 1: input channals 32: output channels, 3: kernel size, 1: stride
        self.conv1 = nn.Conv2d(1, 32, 5, 1, 2)
        self.conv2 = nn.Conv2d(32, 64, 5, 1)
        # It will 'filter' out some of the input by the probability(assign zero)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        # Fully connected layer: input size, output size
        self.fc1 = nn.Linear(3136, 128)
        self.fc2 = nn.Linear(128, 10)
    # it is inherit from nn.Module, nn.Module have both forward() and backward()
    # In this case, forward() link all layers together,
    # backward is already implemented to compute the gradient descents.
    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output
