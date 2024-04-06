# README

**This folder is the DAM's source code and dataset of the paper titled ''Dual Attention Mechanism for Multi-scale
Low-altitude UAV Detection''**

![1712399791179](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\1712399791179.png)

## BFAIRD Dataset：

You can get our dataset by this link: https://pan.baidu.com/s/1rYN0pNg8xV3U1zes2Z7WPw?pwd=63so

## Environment requirements：

**Jinja2 == 3.1.3**

**matplotlib == 3.7.4**

**networkx == 3.1**

**numpy == 1.24.4**

**pandas == 2.0.3**

**pillow == 10.2.0**

**python == 3.8.18**

**scipy == 1.10.1**

**seaborn == 0.13.1**

**torch == 2.1.2**

**torchvision == 0.16.2**

**tqdm == 4.66.1** 

**ultralytics == 8.1.3**

## Setup:

1. Prepare the environment and download our datasets.
2. Place the images and corresponding txt files in the dataset into the **'dataset/bvn/images'** and **'labels'** folders respectively. Put the pictures into the **'images'** folder, and the **txt** files into the **'labels'** folder. Create **'train'** and **'val'** folders in their respective folders and put the corresponding number of pictures according to your own preferences, and ensure that the pictures Corresponds to **txt** file.
3. Adjust those parameters in the main.py file.
4. Run **python main.py** to start it.

