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

~~Figure out the organize of dataset~~

~~Extract the object with the mask~~

~~Generate weighted map with original dataset~~

Figure out how to change the dataset of Nerfstudio

Integrate the dataset of OI into Nerfstudio

Train the instant-ngp with OI dataset

Get the rerendered image and generate weighted map with rerendered dataset

Train the instant-ngp with weighted map which could control the generated lighting condition with an extra simple parameter


# Statement of device
 Currently Feiran's labtop could run instant-ngp, but not sure what will happen when retraining model at the final step.

 Athena and Shourya are suggested to test code on the computer in ECE building. That computer could run demo of the nerfstudio which could used be test ideas. When it works, Feiran could train it on his laptop.

 Under worset situation, we might need to use cloud computing. 
