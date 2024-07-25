import torch
import matplotlib.pyplot as plt
import numpy as np
words=None
with open('names.txt','r') as f:
    words = f.read().splitlines()
print(words[:10])

def infoData(dataset:list)->dict:
    mp={}
    mp["len"]=len(dataset)
    mp["min"]=min(len(word) for word in dataset)
    mp["max"]=max(len(word) for word in dataset)
    return mp

print(infoData(words))

chars=sorted(list(set("".join(words))))
stoi={s:i for i,s in enumerate(chars)}
stoi["<S>"]=26
stoi["<E>"]=27
print(stoi)

N=torch.zeros((28,28),dtype=torch.int32)
for word in words:
    chs=["<S>"] + list(word) +["<E>"]
    for ch1, ch2 in zip(chs,chs[1:]):
        idx1,idx2=stoi[ch1],stoi[ch2]
        N[idx1,idx2]+=1
array=N.numpy()

try:
    plt.imshow(array)
    plt.show()
except Exception as E:
    print(E)