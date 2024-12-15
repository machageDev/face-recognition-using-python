import os

folders = [
    "dataset/train/class1",
    "dataset/train/class2",
    "dataset/validation/class1",
    "dataset/validation/class2"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folders created successfully!")
