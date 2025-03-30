# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
# We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.
# (user input is in bold italics):

def mad_lib():
   
    adjective : str = input("Type an adjective and press enter: ")
    verb :str = input("Type an verb and press enter: ")
    noun :str = input("Type an noun and press enter: ")

    print(f"The {adjective} code {verb} smoothly on the {noun}.")
          
if __name__ == "__main__":
    mad_lib()