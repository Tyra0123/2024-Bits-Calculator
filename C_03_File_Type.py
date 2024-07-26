# asks users for file type (integer / image / text / xxx)
def get_filetype():
    response = input("File type: ").lower()

    # check for 'i' or the exit code
    if response == "xxx" or response == "i":
        return response

    # check if it's an integer
    elif response in ['integer', 'int']:
        return "integer"

    # check if it's an image
    elif response in ['image', 'picture', 'img', 'P']:
        return "image"

    # check if it's a text
    elif response in ['text', 'txt', 'T']:
        return "text"

    # if the response is invalid output an error
    else:
        print("Please enter a valid file type")


# Main routine goes here
while True:
    file_type = get_filetype()
    print(f"You chose {file_type}")

    if file_type == "xxx":
        break
