
import json

absolute_path = "/home/fr/Documents/project/openillumination/lighting_patterns/obj_02_egg/output/"

# Provided filename mapping
filename_mapping = {
    "CA2": "frame_00001.png",
    "CA4": "frame_00002.png",
    "CA6": "frame_00003.png",
    "CA8": "frame_00004.png",
    "CB2": "frame_00005.png", 
    "CB4": "frame_00006.png",
    "CB5": "frame_00007.png",
    "CB7": "frame_00008.png",  
    "CB8": "frame_00009.png",
    "CC4": "frame_00010.png",
    "CC5": "frame_00011.png",
    "CC7": "frame_00012.png",
    "CD1": "frame_00013.png",
    "CD3": "frame_00014.png",
    "CD7": "frame_00015.png",
    "CD8": "frame_00016.png",
    "CE2": "frame_00017.png",
    "CE3": "frame_00018.png",
    "CE4": "frame_00019.png",
    "CE8": "frame_00020.png",
    "CF1": "frame_00021.png",
    "CF3": "frame_00022.png",
    "CF5": "frame_00023.png",
    "CF8": "frame_00024.png",
    "NA1": "frame_00025.png",
    "NA3": "frame_00026.png",
    "NA5": "frame_00027.png",
    "NA7": "frame_00028.png",
    "NB1": "frame_00029.png",
    "NB3": "frame_00030.png",
    "NB6": "frame_00031.png",
    "NC1": "frame_00032.png",
    "NC2": "frame_00033.png",
    "NC3": "frame_00034.png",
    "NC6": "frame_00035.png",
    "NC8": "frame_00036.png",
    "ND2": "frame_00037.png",
    "ND4": "frame_00038.png",
    "ND5": "frame_00039.png",
    "ND6": "frame_00040.png",
    "NE1": "frame_00041.png",
    "NE5": "frame_00042.png",
    "NE6": "frame_00043.png",
    "NE7": "frame_00044.png",
    "NF2": "frame_00045.png",
    "NF4": "frame_00046.png",
    "NF6": "frame_00047.png",
    "NF7": "frame_00048.png"
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


# {"CA2": "frame_00001.png",
#  "CA4": "frame_00002.png",
#  "CA6": "frame_00003.png",
#  "CA8": "frame_00004.png",
#  "CB2": "frame_00005.png", 
#  "CB4": "frame_00006.png",
#  "CB5": "frame_00007.png",
#  "CB7": "frame_00008.png",  
#  "CB8": "frame_00009.png",
#  "CC4": "frame_00010.png",
#  "CC5": "frame_00011.png",
#  "CC7": "frame_00012.png",
#  "CD1": "frame_00013.png",
#  "CD3": "frame_00014.png",
#  "CD7": "frame_00015.png",
#  "CD8": "frame_00016.png",
#  "CE2": "frame_00017.png",
#  "CE3": "frame_00018.png",
#  "CE4": "frame_00019.png",
#  "CE8": "frame_00020.png",
#  "CF1": "frame_00021.png",
#  "CF3": "frame_00022.png",
#  "CF5": "frame_00023.png",
#  "CF8": "frame_00024.png",
#  "NA1": "frame_00025.png",
#  "NA3": "frame_00026.png",
#  "NA5": "frame_00027.png",
#  "NA7": "frame_00028.png",
#  "NB1": "frame_00029.png",
#  "NB3": "frame_00030.png",
#  "NB6": "frame_00031.png",
#  "NC1": "frame_00032.png",
#  "NC2": "frame_00033.png",
#  "NC3": "frame_00034.png",
#  "NC6": "frame_00035.png",
#  "NC8": "frame_00036.png",
#  "ND2": "frame_00037.png",
#  "ND4": "frame_00038.png",
#  "ND5": "frame_00039.png",
#  "ND6": "frame_00040.png",
#  "NE1": "frame_00041.png",
#  "NE5": "frame_00042.png",
#  "NE6": "frame_00043.png",
#  "NE7": "frame_00044.png",
#  "NF2": "frame_00045.png",
#  "NF4": "frame_00046.png",
#  "NF6": "frame_00047.png",
#  "NF7": "frame_00048.png",
#  }

