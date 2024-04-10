import json

# Load the original JSON data
with open('Data/present_simple_past_simple.json', 'r') as file:
    data = json.load(file)

# Convert all past tense verbs to uppercase
modified_data = {key: value.upper() for key, value in data.items()}

# Save the modified data to a new JSON file
with open('Data/present_past_Uppercase.json', 'w') as file:
    json.dump(modified_data, file, indent=4)

print("The past tense verbs have been converted to uppercase and saved in 'verbs_modified.json'.")
