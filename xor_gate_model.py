import torch
import torch.nn as nn
import torch.optim as optim
import os

# XOR 데이터셋
binary_input_tensor = torch.tensor([[0,0], [0,1], [1,0], [1,1]], dtype=torch.float32)
xor_output_tensor = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# XOR 모델 정의
class XORModel(nn.Module):
    def __init__(self):
        super(XORModel, self).__init__()
        self.hidden = nn.Linear(2, 4)  # 은닉층 (입력이 2개인 뉴런 4개)
        self.output = nn.Linear(4, 1)  # 출력층 (입력이 4개인 뉴런 1개)
        
    def forward(self, tensor):
        tensor = torch.relu(self.hidden(tensor))  # ReLU 활성화 함수
        tensor = torch.sigmoid(self.output(tensor))  # Sigmoid 출력
        return tensor

class XORGate():
    def __init__(self):
        self.model = XORModel()
        self.MODEL_FILE = "xor_model.pth"

    def training(self, learning_rate, epochs):
        criterion = nn.BCELoss()  # Binary Cross Entropy Loss
        optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)  # Adam Optimizer

        # 모델 학습
        for epoch in range(epochs):
            optimizer.zero_grad()
            output_pred = self.model(binary_input_tensor)
            loss = criterion(output_pred, xor_output_tensor)
            loss.backward()
            optimizer.step()

    def operate(self, input):
        with torch.no_grad():
            torch_input = torch.tensor(input, dtype=torch.float32)
            result = self.model(torch_input)
            return (result > 0.5).int().item()
    
    def save(self):
        torch.save(self.model.state_dict(), self.MODEL_FILE)
    
    def load(self):
        if os.path.exists(self.MODEL_FILE):
            self.model.load_state_dict(torch.load(self.MODEL_FILE))
            self.model.eval()
            return True
        else:
            return False
