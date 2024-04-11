import json

def reverse_values(data):
  """Reverses the values of each key-value pair in a dictionary.

  Args:
      data: A dictionary containing the data to be reversed.

  Returns:
      A new dictionary with the values reversed.
  """
  reversed_data = {}
  for key, value in data.items():
    reversed_data[key] = value[::-1] if isinstance(value, str) else value
  return reversed_data

# Assuming your JSON file is named "data.json"
with open("antonyms.json", "r") as f:
  data = json.load(f)

# Reverse the values in the dictionary
reversed_data = reverse_values(data)

# Save the reversed data to a new file named "reversed_data.json"
with open("antonym_reversed.json", "w") as f:
  json.dump(reversed_data, f, indent=2)

print("Values reversed and saved to reversed_data.json")