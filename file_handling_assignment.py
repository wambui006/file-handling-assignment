try:
    # Create or open the file in write mode
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("12345 is a number written on the second line.\n")
        file.write("This is the third line of text.\n")
    print("File created and text written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while creating or writing to the file: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nContents of the file after initial write:")
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is an appended fourth line.\n")
        file.write("67890 is another number appended as a fifth line.\n")
        file.write("This is the final sixth line added to the file.\n")
    print("\nText appended successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while appending to the file: {e}")

# File Reading After Appending
try:
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("\nContents of the file after appending:")
        print(updated_content)
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while reading the file after appending: {e}")

finally:
    print("\nFile handling operation completed.")
