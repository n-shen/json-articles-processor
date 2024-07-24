import os
import sys
import json


def paragraph_to_json(title, body, true_narrative):
    # Create a dictionary with the required format
    data = {
        "title": title,
        "body": body,
        "true_narrative": true_narrative
    }
    return json.dumps(data, indent=4)


def process_body_content(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    paragraphs = []
    current_paragraph = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            current_paragraph.append(stripped_line)
        else:
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph))
                current_paragraph = []

    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    return "\n\n".join(paragraphs)


def process_args():
    if len(sys.argv) >= 3:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        group_narrative_standpoint_value = sys.argv[3] if len(
            sys.argv) == 4 else None
        return input_folder, output_folder, group_narrative_standpoint_value
    return None, None, None


def main():
    input_folder, output_folder, group_narrative_standpoint_value = process_args()

    if not input_folder:
        input_folder = input(
            ">>> Enter the path to the folder containing .txt files [e.g. ./articles] : ")
    if not os.path.exists(input_folder):
        print(f"[System] Folder {input_folder} not found.")
        return

    if not output_folder:
        output_folder = input(
            ">>> Enter the path to the output folder [e.g. ./output]: ")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not group_narrative_standpoint_value:
        group_narrative_standpoint_value = input(
            ">>> Enter the group narrative_standpoint_value value, press Enter if not applicable: ")

    print("[System] Group narrative_standpoint_value: ",
          group_narrative_standpoint_value if group_narrative_standpoint_value != "" else "Not applicable")

    # Iterate over all .txt files in the specified folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            title = os.path.splitext(file_name)[0]
            file_path = os.path.join(input_folder, file_name)

            try:
                # Process the content of the file
                body = process_body_content(file_path)
            except FileNotFoundError:
                print(f"File {file_path} not found.")
                continue

            # Present the title to the user and ask for the true_narrative value
            print(f"Title: {title}")
            if group_narrative_standpoint_value != "":
                true_narrative = int(group_narrative_standpoint_value)
            else:
                true_narrative = input(
                    ">>> Enter the true_narrative value (e.g., 1 for true, 0 for false): ")

            # Convert the paragraph to a JSON string
            json_string = paragraph_to_json(title, body, int(true_narrative))

            # Save the JSON string to a file in the output folder
            output_file = os.path.join(
                output_folder, f"{title.replace(' ', '_')}.json")
            with open(output_file, 'w') as json_file:
                json_file.write(json_string)

            print(f"The JSON file has been saved as {output_file}\n")


if __name__ == "__main__":
    main()
