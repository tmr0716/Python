print('----------------------------------- Classroom Day 10 -----------------------------------')
import torch

print('====================================== Tensors & Autograd ======================================')
x = torch.tensor([[1,2],[3,4]], dtype=torch.float32, requires_grad=True)
y = x**2 + 3*x + 4
y.backward(torch.ones_like(x))
print(x.grad)

a = torch.rand(3,3)
b = torch.ones(3,3)
print(a+b, a*b, a@b)

print('====================================== GPU Acceleration ======================================')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.rand(3,3).to(device)

print('====================================== Neural Network Building Blocks ======================================')
import torch.nn as nn
class SimpleNet(nn.Module):
    def __init__(self):
        super() .__init__()
        self.fc = nn.Linear(1,1)
    def forward(self,x):
        return self.fc(x)
    
# print('====================================== Training Loop Pattern ======================================')

# loss_fn = nn.MSELoss()
# opt = torch.optim.SGD(model.parameters(), lr=0.01)
# for epoch in range(100):
#     y_pred = model(x)
#     loss = loss_fn(y_pred, y)
#     opt.zero_grad()
#     loss.background()
#     opt.step()

print('====================================== Dataset + Dataloader ======================================')
from torch.utils.data import Dataset, DataLoader

class StudentDataset(Dataset):
    def __init__(self, df):
        self.x = torch.tensor(df["age"].values, dtype=torch.float32).unsqueeze(1)
        self.y = torch.tensor(df["marks_clean"].values, dtype=torch.float32).unsqueeze(1)
    def __getitem__(self, idx): return self.x[idx], self.y[idx]
    def __len__(self): return len(self.x)