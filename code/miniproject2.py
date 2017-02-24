from parse import get_shakespeare
from baum_welch.HMM import unsupervised_HMM

def train():
    q, c, dq, dc = get_shakespeare()
    c_model = unsupervised_HMM(c, 6, 10)
    q_model = unsupervised_HMM(q, 6, 10)

    for i in range(0,12):
        print(' '.join(map(dq.get, q_model.generate_emission(6))))
    for _ in range(0,2):
        print(' '.join(map(dc.get, c_model.generate_emission(6))))

train()
