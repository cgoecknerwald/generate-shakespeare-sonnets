from parse import get_shakespeare
from baum_welch.HMM import unsupervised_HMM

def train():
    q, c, d = get_shakespeare()
    v = 0
    for i in c:
        print(len(i))

    q_model = unsupervised_HMM(q, 5, 10)
    c_model = unsupervised_HMM(c, 5, 10)
    print(q_model.generate_emmission(10))
    print(c_model.generate_emmission(10))

train()
