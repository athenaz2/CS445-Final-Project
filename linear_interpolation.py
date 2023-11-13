import os
import cv2  
import numpy as np
from matplotlib import pyplot as plt
import imageio.v2 as imageio

#----------------------------------------------------------------------------------
# Change Parameters Here
# Define your folder paths
absolute_path = "/home/fr/Documents/project/openillumination/lighting_patterns/"
# Object name, the folder name of the objects under folder lighting_patterns
object_name = "obj_07_dog/"
# Size of weighted map
grid_size = 4
# Output masked images
ouput_masked_object = False
# Output weighted maps
weighted_sample = False
#----------------------------------------------------------------------------------

lighting_condition1 = absolute_path + object_name + 'Lights/001/raw_undistorted'
lighting_condition4 = absolute_path + object_name + 'Lights/004/raw_undistorted'
lighting_condition8 = absolute_path + object_name + 'Lights/008/raw_undistorted'
lighting_condition13 = absolute_path + object_name + 'Lights/013/raw_undistorted'
mask_folder_path = absolute_path + object_name + "output/obj_masks"


output_lighting_condition1 = absolute_path + object_name + 'object/001/output'
output_lighting_condition4 = absolute_path + object_name + 'object/004/output'
output_lighting_condition8 = absolute_path + object_name + 'object/008/output'
output_lighting_condition13 = absolute_path + object_name + 'object/013/output'

def generate_weighted_sample(image_list, image_name, grid_size):
    destination_folder_path = absolute_path + object_name + 'weighted_map/' + str(grid_size) + "/"
    os.makedirs(destination_folder_path, exist_ok=True)
    destination = destination_folder_path  + image_name
    H, W, _ = image_list[0].shape
    image1 = image_list[0]
    image2 = image_list[1]
    image3 = image_list[2]
    image4 = image_list[3]
    # Create a function to interpolate between two images
    def interpolate(imageA, imageB, weight):
        return cv2.addWeighted(imageA, 1 - weight, imageB, weight, 0)
    # Initialize an empty list to hold the interpolated images
    interpolated_images = np.zeros((grid_size, grid_size, H, W, 3), dtype=np.uint8)
    # Perform the interpolation
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate weights for interpolation
            w1 = (grid_size - j) / grid_size
            w2 = j / grid_size
            w3 = (grid_size - i) / grid_size
            w4 = i / grid_size
            # Interpolate horizontally along the top and bottom
            top_interpolated = interpolate(image1, image2, w2)
            bottom_interpolated = interpolate(image3, image4, w2)
            # Interpolate vertically between top and bottom interpolations
            final_interpolated = interpolate(top_interpolated, bottom_interpolated, w4)
            interpolated_images[i, j] = final_interpolated
            # Save weighted image alone
            # cv2.imwrite(destination, interpolated_images[0,0])
            
    # Flatten interpolated_images into a huge weighted map image and save
    rows = []
    for i in range(grid_size):
        row = np.concatenate(interpolated_images[i, :], axis=1)   
        rows.append(row)
    large_image = np.concatenate(rows, axis=0)  
    cv2.imwrite(destination, large_image)

# Map the object with mask
def extract_object(image_list, mask):
    object_list = []
    for image in image_list:
        # White background
        mask_3d = np.expand_dims(mask, axis=-1)
        white_image = np.full(image.shape, [255, 255, 255], dtype=np.uint8)
        masked_image = np.where(mask_3d, image, white_image)
        # Black background
        # mask_3d = mask[:, :, np.newaxis]
        # masked_image = image * mask_3d
        object_list.append(masked_image)
    return object_list

# Write masked images
def output(image_list, output_folders, image_name):
    # Save each image in the image_list to the corresponding folder
    for img, folder in zip(image_list, output_folders):
        # Ensure the output folder exists
        if not os.path.exists(folder):
            os.makedirs(folder)
        output_path = os.path.join(folder, image_name)
        cv2.imwrite(output_path, img)

def main(grid_size, ouput_masked_object = False, weighted_sample = False):
    source_folder_paths = [lighting_condition1, lighting_condition4, lighting_condition8, lighting_condition13]
    output_folder_paths = [output_lighting_condition1, output_lighting_condition4, output_lighting_condition8, output_lighting_condition13]
    # Assuming all folders have the same number of images with the same names
    image_names = os.listdir(source_folder_paths[0])  
    for image_name in image_names:
        image_list = []
        # Read images under 4 lighting conditions
        for folder_path in source_folder_paths:
            image_path = os.path.join(folder_path, image_name)
            mask_name = image_name.replace(".JPG", ".png")
            mask_path = os.path.join(mask_folder_path, mask_name)
            # Check if the file exists
            if os.path.isfile(image_path):
                image = cv2.imread(image_path)
            else:
                print(image_path)
                print("Not exist.")
            if os.path.isfile(image_path):
                mask = imageio.imread(mask_path)>0
            else:
                print(mask_path)
                print("Not exist.")
            
            image_list.append(image)
        # Generate weighted_map with different size
        image_list = extract_object(image_list, mask)
        if ouput_masked_object == True:
            output(image_list, output_folder_paths, image_name)
        if weighted_sample == True:
            generate_weighted_sample(image_list, image_name, grid_size) 
    
if __name__ == "__main__":
    main(grid_size, ouput_masked_object, weighted_sample)

