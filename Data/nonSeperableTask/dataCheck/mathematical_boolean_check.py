import json

def correct_and_evaluate_expressions(input_file_path, output_file_path):
    # Load the JSON data from the file
    with open(input_file_path, 'r') as file:
        expressions = json.load(file)

    # Dictionary to hold expressions and their correctly evaluated results
    results = {}

    # Iterate through each expression
    for expression, _ in expressions.items():
        # Replace the '=' with '==' for correct Python syntax for equality checks
        corrected_expression = expression.replace("=", "==")

        try:
            # Evaluate the corrected expression using Python's eval function
            evaluation_result = eval(corrected_expression)
            results[expression] = evaluation_result
        except Exception as e:
            # If there's an error in evaluating the expression, store the error message
            results[expression] = f"Error evaluating expression: {str(e)}"

    # Save the updated dictionary to a new JSON file
    with open(output_file_path, 'w') as file:
        json.dump(results, file, indent=4)

    print(f"Results saved to {output_file_path}")

# Example usage:
input_file_path = 'mathematical_boolian.json'
output_file_path = input_file_path
correct_and_evaluate_expressions(input_file_path, output_file_path)
