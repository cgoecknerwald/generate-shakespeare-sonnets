from parse import parse
from baum_welch.HMM import unsupervised_HMM

def train():
    Q, C = parse()
    Q_model = unsupervised_HMM(Q, 2, 10)
    C_model = unsupervised_HMM(C, 2, 10)
    print(Q_model.generate_emmission(10))
    print(C_model.generate_emmission(10))

train()
