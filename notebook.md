# Experiment Record

# Quick test on the nerfstudio locally

Download the following [dataset](https://drive.google.com/file/d/1O14XntmZHt2wy7WbfHIdJLdBa6ROV0Ut/view?usp=sharing) into the folder "./data",

```bash
# Train instant-ngp with new dataset
ns-train instant-ngp --data data/nerfstudio/egg_out
```

# Full Process 
## 1. Installation of [nerfstudio](https://docs.nerf.studio/quickstart/installation.html)


## 2. Preparetion of data
(1) Install dataset
   
Take the website of OpenIllumination as the [overview](https://oppo-us-research.github.io/OpenIllumination/) to select object to download.
```bash
# Change the `--obj_id` with the Object ID. 
python open_illumination.py --light lighting_patterns --obj_id 2 
```

(2) Generate weighted map
   
Given 4 images of same object at same camera pose from 4 different lighting conditions, We need to create a weighted map which is linear interpolation map.

```bash
# Change the 'absolute path', 'object_name' and 'gride_size' inside the code
python open_illumination.py
```

(3) Transform data to Nerfstudio format
To train on self captured data you will need to process the data into the nerfstudio format, [instruction](https://docs.nerf.studio/quickstart/custom_dataset.html).

```bash
ns-process-data images --data {DATA_PATH} --output-dir {PROCESSED_DATA_DIR}

# Example
ns-process-data images --data /home/fr/Documents/project/openillumination/lighting_patterns/obj_02_egg/object/004/output --output-dir /home/fr/Documents/project/nerfstudio/data/nerfstudio/egg_4
```
**Note: output-dir should be folder under "nerfstudio/data/nerfstudio/"**

4. Change the format of the transform_matrix to nerfstudio version
Replace the "transforms.json" in the output folder with the one in the outest 


## 3. Others: Generate weighted map

Given 4 images of same object at same camera pose from 4 different lighting conditions, We need to create a weighted map which is linear interpolation map.

```bash
# Change the absolute path, object_name and gride_size inside the code
python open_illumination.py
```

## 3. Train the model
```bash
# Run instant-ngp
ns-train instant-ngp --data data/nerfstudio/{PROCESSED_DATA_DIR}
```


# Quick Sheet

```bash
# Run instant-ngp with demo data
ns-train instant-ngp --data data/nerfstudio/poster
```

```bash
#Show the memory usage of GPU at real time
nvidia-smi -l
```


# Warning Solution
1. No nvcc

If shows no "No such file or directory: ':/usr/local/cuda-11.3/bin/nvcc'", change the path of CUDA-HOME(According to [ZhiHu](https://zhuanlan.zhihu.com/p/519732843)): 
```bash
export CUDA_HOME=/usr/local/cuda
```

2. No colmap

```bash
sudo apt-get install colmap
```


# Installation

1. Colmap

(1) Install Ceres1.14.0

```bash
sudo apt-get install liblapack-dev libsuitesparse-dev libgflags-dev 
sudo apt-get install libgoogle-glog-dev libgtest-dev
sudo apt-get install libcxsparse3
wget ceres-solver.org/ceres-solver-1.14.0.tar.gz
tar -zxvf ceres-solver-1.14.0.tar.gz
cd ceres-solver-1.14.0
sudo mkdir build
cd build
sudo cmake ..
sudo make
sudo make install
```
(2) Install colmap
```bash
sudo apt-get install \
    git \
    cmake \
    build-essential \
    libboost-program-options-dev \
    libboost-filesystem-dev \
    libboost-graph-dev \
    libboost-regex-dev \
    libboost-system-dev \
    libboost-test-dev \
    libeigen3-dev \
    libsuitesparse-dev \
    libfreeimage-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev \
    libcgal-qt5-dev

git clone https://github.com/colmap/colmap
cd colmap
mkdir build
cd build
cmake .. -DCMAKE_CUDA_ARCHITECTURES=70
make
sudo make install
```

Reference: 
1. [Ceres](https://zhuanlan.zhihu.com/p/460693184)
1. [Colmap](https://zhuanlan.zhihu.com/p/460685629)