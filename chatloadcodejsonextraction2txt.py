def copy_lines_to_file(lines, filename):
    with open(filename, 'w') as file:
        file.writelines(lines)
        print(f"Lines copied to {filename}")

def copy_lines_from_file(text_file, chunk_size=50):
    with open(text_file, 'r') as file:
        data = file.readlines()
        total_lines = len(data)
        copied_lines = 0

        while copied_lines < total_lines:
            chunk = data[copied_lines:copied_lines + chunk_size]
            copy_lines_to_file(chunk, f"output_{copied_lines + 1}-{copied_lines + chunk_size}.txt")
            copied_lines += chunk_size

        print("Copying completed.")

# Usage
text_file = "QA_Cell_Phones_and_Accessories.txt"
copy_lines_from_file(text_file, chunk_size=50)

