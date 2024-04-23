import json
import numpy as np

# Parameters for each level
settings = {
    "easy": {"count": 50, "num_points": 60, "noise_sd": 0.1},
    "medium": {"count": 30, "num_points": 40, "noise_sd": 0.7},
    "hard": {"count": 20, "num_points": 20, "noise_sd": 1}
}

# Randomly generate data for each difficulty level
problems = []
for level, config in settings.items():
    for _ in range(config["count"]):
        m = np.random.uniform(0.5, 5)  # Random slope from 0.5 to 5
        b = np.random.uniform(0, 20)  # Random intercept from 0 to 20
        x_values = np.linspace(0, 100, config["num_points"])
        y_values = m * x_values + b + np.random.normal(0, config["noise_sd"], config["num_points"])
        data_points = [{'x': round(float(x), 4), 'y': round(float(y), 4)} for x, y in zip(x_values, y_values)]
        problems.append({
            "level": level,
            "slope": round(m, 4),
            "intercept": round(b, 4),
            "data": data_points
        })

# Convert to JSON
json_data = json.dumps(problems, indent=4)

# Write JSON data to a file
with open('linear_regression_ICL.json', 'w') as file:
    file.write(json_data)
