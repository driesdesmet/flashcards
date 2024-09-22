import random

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text


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

    console = Console()

    # Iterate over the shuffled keys
    for key in keys:  # Prompt the user for the value
        # Display the flashcard
        flashcard = Panel(
            Text(key, justify="center", style="bold magenta"),
            title="Flashcard", border_style="blue")
        console.print(flashcard)

        # Prompt the user for the value
        user_answer = Prompt.ask(
            f"[bold cyan]What is the value for '{key}'?[/bold cyan]")

        # Check if the answer is correct
        if user_answer.lower() == quiz_dict[key].lower():
            console.print("[bold green]Correct![/bold green]")
            correct_answers += 1
        else:
            console.print(
                f"[bold red]Wrong! The correct answer is '{quiz_dict[key]}'."
                "[/bold red]")

    # Display the final score
    print(f"\nYour final score is {correct_answers} out of {len(quiz_dict)}.")


if __name__ == "__main__":
    main()
