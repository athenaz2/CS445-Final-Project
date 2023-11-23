
# Script to transform transform.json of openillumination to format in nerfstudio
import json

absolute_path = "/home/fr/Documents/project/CS445-Final-Project/lighting_patterns/obj_07_dog/output/"

# Provided filename mapping
filename_mapping = {
    "CA2": "frame_00001.JPG",
    "CA4": "frame_00002.JPG",
    "CA6": "frame_00003.JPG",
    "CA8": "frame_00004.JPG",
    "CB2": "frame_00005.JPG", 
    "CB4": "frame_00006.JPG",
    "CB5": "frame_00007.JPG",
    "CB7": "frame_00008.JPG",  
    "CB8": "frame_00009.JPG",
    "CC4": "frame_00010.JPG",
    "CC5": "frame_00011.JPG",
    "CC7": "frame_00012.JPG",
    "CD1": "frame_00013.JPG",
    "CD3": "frame_00014.JPG",
    "CD7": "frame_00015.JPG",
    "CD8": "frame_00016.JPG",
    "CE2": "frame_00017.JPG",
    "CE3": "frame_00018.JPG",
    "CE4": "frame_00019.JPG",
    "CE8": "frame_00020.JPG",
    "CF1": "frame_00021.JPG",
    "CF3": "frame_00022.JPG",
    "CF5": "frame_00023.JPG",
    "CF8": "frame_00024.JPG",
    "NA1": "frame_00025.JPG",
    "NA3": "frame_00026.JPG",
    "NA5": "frame_00027.JPG",
    "NA7": "frame_00028.JPG",
    "NB1": "frame_00029.JPG",
    "NB3": "frame_00030.JPG",
    "NB6": "frame_00031.JPG",
    "NC1": "frame_00032.JPG",
    "NC2": "frame_00033.JPG",
    "NC3": "frame_00034.JPG",
    "NC6": "frame_00035.JPG",
    "NC8": "frame_00036.JPG",
    "ND2": "frame_00037.JPG",
    "ND4": "frame_00038.JPG",
    "ND5": "frame_00039.JPG",
    "ND6": "frame_00040.JPG",
    "NE1": "frame_00041.JPG",
    "NE5": "frame_00042.JPG",
    "NE6": "frame_00043.JPG",
    "NE7": "frame_00044.JPG",
    "NF2": "frame_00045.JPG",
    "NF4": "frame_00046.JPG",
    "NF6": "frame_00047.JPG",
    "NF7": "frame_00048.JPG"
}

# Modify the load_and_process_json function to map filenames using the provided mapping
def load_and_process_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [
        {
            "file_path": "images/" + filename_mapping[frame["file_path"].split('/')[-1].split('.')[0]],
            "transform_matrix": frame["transform_matrix"]
        }
        for frame in data["frames"].values()
    ]

# Load and process each JSON file
data_train = load_and_process_json(absolute_path + 'transforms_train.json')
data_val = load_and_process_json(absolute_path + 'transforms_val.json')
data_test = load_and_process_json(absolute_path + 'transforms_test.json')

# Combine data from all three files
combined_data = {"frames": data_train + data_val + data_test}

sorted_combined_data = {"frames": sorted(combined_data["frames"], key=lambda x: x["file_path"])}

# Define the path for the new JSON file
output_file_path = absolute_path + 'combined_processed_transforms.json'

# Write the combined data to a new JSON file
with open(output_file_path, 'w') as file:
    json.dump(sorted_combined_data, file, indent=2)



# import json

# absolute_path = "/home/fr/Documents/project/openillumination/lighting_patterns/obj_02_egg/output/"

# # Function to load and process JSON file
# def load_and_process_json(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return [
#         {"file_path": frame["file_path"], "transform_matrix": frame["transform_matrix"]}
#         for frame in data["frames"].values()
#     ]

# # Load and process each JSON file
# data_train = load_and_process_json(absolute_path + 'transforms_train.json')
# data_val = load_and_process_json(absolute_path + 'transforms_val.json')
# data_test = load_and_process_json(absolute_path + 'transforms_test.json')

# # Combine data from all three files
# combined_data = {"frames": data_train + data_val + data_test}

# # Define the path for the new JSON file
# output_file_path = absolute_path + 'combined_processed_transforms.json'

# # Write the combined data to a new JSON file
# with open(output_file_path, 'w') as file:
#     json.dump(combined_data, file, indent=2)


# {"CA2": "frame_00001.JPG",
#  "CA4": "frame_00002.JPG",
#  "CA6": "frame_00003.JPG",
#  "CA8": "frame_00004.JPG",
#  "CB2": "frame_00005.JPG", 
#  "CB4": "frame_00006.JPG",
#  "CB5": "frame_00007.JPG",
#  "CB7": "frame_00008.JPG",  
#  "CB8": "frame_00009.JPG",
#  "CC4": "frame_00010.JPG",
#  "CC5": "frame_00011.JPG",
#  "CC7": "frame_00012.JPG",
#  "CD1": "frame_00013.JPG",
#  "CD3": "frame_00014.JPG",
#  "CD7": "frame_00015.JPG",
#  "CD8": "frame_00016.JPG",
#  "CE2": "frame_00017.JPG",
#  "CE3": "frame_00018.JPG",
#  "CE4": "frame_00019.JPG",
#  "CE8": "frame_00020.JPG",
#  "CF1": "frame_00021.JPG",
#  "CF3": "frame_00022.JPG",
#  "CF5": "frame_00023.JPG",
#  "CF8": "frame_00024.JPG",
#  "NA1": "frame_00025.JPG",
#  "NA3": "frame_00026.JPG",
#  "NA5": "frame_00027.JPG",
#  "NA7": "frame_00028.JPG",
#  "NB1": "frame_00029.JPG",
#  "NB3": "frame_00030.JPG",
#  "NB6": "frame_00031.JPG",
#  "NC1": "frame_00032.JPG",
#  "NC2": "frame_00033.JPG",
#  "NC3": "frame_00034.JPG",
#  "NC6": "frame_00035.JPG",
#  "NC8": "frame_00036.JPG",
#  "ND2": "frame_00037.JPG",
#  "ND4": "frame_00038.JPG",
#  "ND5": "frame_00039.JPG",
#  "ND6": "frame_00040.JPG",
#  "NE1": "frame_00041.JPG",
#  "NE5": "frame_00042.JPG",
#  "NE6": "frame_00043.JPG",
#  "NE7": "frame_00044.JPG",
#  "NF2": "frame_00045.JPG",
#  "NF4": "frame_00046.JPG",
#  "NF6": "frame_00047.JPG",
#  "NF7": "frame_00048.JPG",
#  }

