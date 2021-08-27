
root_path = './First_Sample_of_Dataset/DATASET Bench/'

import os
import torch
import torchvision
from torchvision import transforms

train_path = {
    "ok": os.path.join(root_path, 'train', 'OK'),
    "nok": os.path.join(root_path, 'train', 'KO')
}

n_ok = len(os.listdir(train_path["ok"]))
n_nok = len(os.listdir(train_path["nok"]))
n_total = n_ok + n_nok

print(f"Training set")
print(f"Total number of samples : {n_total}")
print(f"* Correct samples   : {n_ok} ({n_ok / n_total * 100 :3.1f}%)")
print(f"* Incorrect samples : {n_nok} ({n_nok / n_total * 100 :3.1f}%)")
print()

val_path = {
    "ok": os.path.join(root_path, 'val', 'OK'),
    "nok": os.path.join(root_path, 'val', 'KO')
}

n_ok = len(os.listdir(val_path["ok"]))
n_nok = len(os.listdir(val_path["nok"]))
n_total = n_ok + n_nok

print(f"Validation set")
print(f"Total number of samples : {n_total}")
print(f"* Correct samples   : {n_ok} ({n_ok / n_total * 100 :3.1f}%)")
print(f"* Incorrect samples : {n_nok} ({n_nok / n_total * 100 :3.1f}%)")
print()

test_path = os.path.join(root_path, 'test')
n_total = len(os.listdir(test_path))
print('Test set')
print(f"Total number of samples : {n_total}")


from PIL import Image
from matplotlib import pyplot as plt
import random

def show_examples(path, title='', N=4, M=4):
    # N, M = rows, columns
    filenames = random.sample(os.listdir(path), N * M)

    fig = plt.figure(figsize=(16, 10))
    fig.suptitle(title)
    for i in range(N):
        for j in range(M):
            k = i * N + j
            plt.subplot(N, M, k + 1)


            img_path = os.path.join(path, filenames[k])
            image = Image.open(img_path)
            plt.imshow(image)
            plt.axis("off")

    plt.show()

print("################")
print("# Training set #")
print("################")
show_examples(train_path["ok"], 'Examples of OK images (Train)')
#show_examples(train_path["nok"], 'Examples of not OK images (Train)')


print("##################")
print("# Validation set #")
print("##################")
#show_examples(val_path["ok"], 'Examples of OK images (Val)')
#show_examples(val_path["nok"], 'Examples of not OK images (Val)')