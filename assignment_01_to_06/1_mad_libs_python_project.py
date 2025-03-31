# Mad libs Python Project
# In this Kylie Ying tutorial, you will learn how to get input from the user, work with f-strings, and see your results printed to the console.

# This is a great starter project to get comfortable doing string concatenation in Python.


def fun_story():
    # Taking inputs for the story
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    action = input("What was the animal doing? ")
    object_thrown = input("Enter an object: ")
    reaction = input("How did the person react? ")

    # Story Template
    story = f"""
     One fine day, {name} went to {place}. Everything seemed normal until they spotted a {animal}.
    To their surprise, the {animal} was {action} in the middle of the street! 

    Panicked, {name} grabbed a {object_thrown} and threw it towards the {animal}.
    The {animal} froze for a moment, then dashed away in confusion! 

    {name} couldn't stop laughing and just {reaction}.
    What an unforgettable adventure at {place}! 
    """

    # Printing the final story
    print("\n📜 Here is your Mad Lib story:\n")
    print(story)

# Running the function
if __name__ == "__main__":
    fun_story()
