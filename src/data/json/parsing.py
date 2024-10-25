import json
import os
import re

input_file_path = 'sparkingZeroScrapes2.txt'
output_file_path = 'formattedSparkingZeroCharacters.json'

def parse_character_data(data):
    """
    Parses the character data from the given input data.

    Args:
        data (str): The input data containing character information.

    Returns:
        list: A list of dictionaries, where each dictionary represents a character.

    """
    lines = data.split('\n')
    characters = []

    character = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('All Characters'):
            if character:
                characters.append(character)  # Append the current character to the list if it exists
            character = {}  # Initialize a new character dictionary
            parts = line.split('  ')  # Split the line into parts using double spaces as the delimiter
            if len(parts) > 2:
                character['series'] = parts[1].strip()  # Extract and assign the series name to the character
        elif line.startswith('DP Cost:'):
            character['dpCost'] = int(line.replace('DP Cost:', '').strip())
        elif line.startswith('Transformations:'):
            transformations = line.replace('Transformations:', '').strip()
            character['transformations'] = [trans.strip() for trans in transformations.split(',')]
        elif line.startswith('Giant Character'):
            character['specialType'] = 'Giant'
        elif not line.startswith('Image:'):
            # Clean up the name by removing trailing numbers
            cleaned_name = re.sub(r'\s+\d+$', '', line.strip())
            character['name'] = cleaned_name
    
    if character:
        characters.append(character)
    
    return characters

def main():
    """
    Main function that reads the input file, parses the character data, and saves the formatted characters to an output file.
    """
    print(f"Current working directory: {os.getcwd()}")
    if not os.path.exists(input_file_path):
        print(f"Error: {input_file_path} does not exist.")
        return

    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    characters = parse_character_data(data)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(characters, file, indent=2)

    print(f"Formatted characters saved to {output_file_path}")

if __name__ == '__main__':
    main()
