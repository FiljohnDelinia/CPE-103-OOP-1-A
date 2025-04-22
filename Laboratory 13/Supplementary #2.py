full_name = input("Enter your first name: ")

name_parts = full_name.split()

if len(name_parts) >= 3:
    middle_words = name_parts[1:-1]
    print("The 3 middle words are:", ' '.join(middle_words))
else:
    print("Your name doesn't have enough words to extract 3 middle words.")
