import random


def main():
    # Define the dictionary
    quiz_dict = {
        "Al": "aluminium",
        "As": "arseen",
        "Ba": "barium",
        "Be": "beryllium",
        "Cd": "cadmium",
        "Ca": "calcium",
        "Cr": "chroom",
        "Au": "goud",
        "Fe": "ijzer",
        "K": "kalium",
        "Co": "kobalt",
        "Cu": "koper",
        "Hg": "kwik",
        "Li": "lithium",
        "Pb": "lood",
        "Pb": "lood",
        "Pb": "lood",
        "Mg": "magnesium",
        "Mn": "mangaan",
        "Na": "natrium",
        "Ni": "nikkel",
        "Pt": "platina",
        "Sn": "tin",
        "U": "uraan",
        "Ag": "zilver",
        "Zn": "zink",
        "Fr": "francium",
        "Br": "broom",
        "Cl": "chloor",
        "F": "fluor",
        "P": "fosfor",
        "I": "jood",
        "C": "koolstof",
        "Si": "silicium",
        "N": "stikstof",
        "H": "waterstof",
        "O": "zuurstof",
        "S": "zwavel",
        "He": "helium",
        "Ne": "neon",
        "Ar": "argon",

    }

    correct_answers = 0

    # Get the keys and shuffle them
    keys = list(quiz_dict.keys())
    random.shuffle(keys)

    # Iterate over the shuffled keys
    for key in keys:  # Prompt the user for the value
        user_answer = input(f"What is the value for '{key}'? ")

        # Check if the answer is correct
        if user_answer.lower() == quiz_dict[key].lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is '{quiz_dict[key]}'.")

    # Display the final score
    print(f"\nYour final score is {correct_answers} out of {len(quiz_dict)}.")


if __name__ == "__main__":
    main()
