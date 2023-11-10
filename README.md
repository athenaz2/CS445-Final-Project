# Relightable NeRF

# Dataset Preparetion
1. Install dataset
Take the website of OpenIllumination as the [overview](https://oppo-us-research.github.io/OpenIllumination/) to select object to download.
```bash
# Change the `--obj_id` with the Object ID. 
python open_illumination.py --light lighting_patterns --obj_id 2 
```

2. Generate weighted map
Given 4 images of same object at same camera pose from 4 different lighting conditions, We need to create a weighted map which is linear interpolation map.

```bash
# Change the absolute path, object_name and gride_size inside the code
python open_illumination.py
```

# Current process
For details read Documentation
- [Google Drive Documentation](https://docs.google.com/document/d/125_pEVwcW1vr8rgyA3AHYGLZWvO4CTy0PwD5N3cTVVk/edit?usp=sharing_)

**Steps:**

~~Download the dataset~~

~~Figure out the orgnize of dataset~~

~~Extract the object with the mask~~

~~Generate weighted map with original dataset~~

Figure out how to change the dataset of Nerfstudio

Integrate the dataset of OI into Nerfstudio

Train the instant-ngp with OI dataset

Get the rerendered image and generate weighted map with rerendered dataset

Train the instant-ngp with weighted map which could control the generated lighting condition with an extra simple parameter

