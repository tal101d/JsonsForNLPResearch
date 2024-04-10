import numpy as np
import json

# Setting seed for reproducibility
np.random.seed(42)

# Generate at least 100 examples with a sum of zero
zero_sum_pairs = [(x, -x) for x in np.random.normal(0, 10000, 100)]

# Initialize dataset with zero sum pairs and their classification
dataset = {str(pair): 'null' for pair in zero_sum_pairs}

# Continue generating pairs until we have at least 1k examples
while len(dataset) < 1000:
    # Generate a pair of numbers
    pair = np.random.normal(0, 10000, 2)
    pair_tuple = (pair[0], pair[1])
    
    # Determine the classification of their sum
    sum_class = 'null' if np.isclose(pair.sum(), 0, atol=1e-10) else 'positive' if pair.sum() > 0 else 'negative'
    
    # Add to dataset if not already present
    dataset[str(pair_tuple)] = sum_class

# Save the dataset to a JSON file
with open('/mnt/data/dataset.json', 'w') as file:
    json.dump(dataset, file, indent=4)

len(dataset)
