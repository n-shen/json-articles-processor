import os
import json


def combine_json_files(input_folders, output_file):
    combined_data = []

    # Iterate over all input folders
    for input_folder in input_folders:
        # Iterate over all .json files in the specified folder
        for file_name in os.listdir(input_folder):
            if file_name.endswith(".json"):
                file_path = os.path.join(input_folder, file_name)

                try:
                    # Read the content of the JSON file
                    with open(file_path, 'r') as json_file:
                        data = json.load(json_file)
                        combined_data.append(data)
                except (FileNotFoundError, json.JSONDecodeError) as e:
                    print(f"Error reading {file_path}: {e}")
                    continue

    # Save the combined data to the output file
    with open(output_file, 'w') as output_json_file:
        json.dump(combined_data, output_json_file, indent=4)

    print(f"The combined JSON file has been saved as {output_file}")


def main():
    input_folders = []

    while True:
        input_folder = input(
            ">>> Enter the path to the folder containing the JSON files [e.g. ./input] (or press Enter to finish): ")
        if not input_folder:
            break

        if not os.path.exists(input_folder):
            print(f"[System] Folder {input_folder} not found.")
        else:
            input_folders.append(input_folder)

    if not input_folders:
        print("[System] No valid input folders provided.")
        return

    output_file = input(
        ">>> Enter the path to the output JSON file [e.g. ./combine.json]: ")

    combine_json_files(input_folders, output_file)


if __name__ == "__main__":
    main()
