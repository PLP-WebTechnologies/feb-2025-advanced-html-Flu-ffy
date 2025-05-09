import os

def read_and_modify_file(input_filename, output_filename):
    if not os.path.isfile(input_filename):  # Check if the file exists
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    
    try:
        # Open the input file in read mode and the output file in write mode using context managers
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Check if content is empty
        if not content:
            print(f"Warning: The file '{input_filename}' is empty.")
            return
        
        # Modify the content (example: reversing the text)
        modified_content = content[::-1]  # Reverse the content for demonstration
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{input_filename}' has been read, modified, and written to '{output_filename}'.")

    except PermissionError:
        print(f"Error: Permission denied to read/write the file '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the new file to write the modified content to: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)
