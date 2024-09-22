 # Flashcards Quiz

This is a simple Python script that quizzes the user on the names of chemical elements based on their symbols. The script randomly shuffles the elements and prompts the user to input the name of the element corresponding to each symbol.

## How to Run

1. **Clone the repository** (if applicable):
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Ensure you have Python installed**. You can check your Python version by running:
    ```sh
    python --version
    ```

3. **Run the script**:
    ```sh
    python flashcards.py
    ```

## How It Works

- The script contains a dictionary of chemical element symbols and their corresponding names.
- It shuffles the keys (symbols) randomly.
- It then iterates over the shuffled keys, prompting the user to input the name of the element for each symbol.
- The user's input is checked against the correct answer, and the script keeps track of the number of correct answers.
- At the end, the script displays the user's final score.

## Example

```sh
$ python flashcards.py
What is the value for 'Zn'? zink
Correct!
What is the value for 'Fr'? francium
Correct!
What is the value for 'Br'? bromine
Wrong! The correct answer is 'broom'.
...
Your final score is 2 out of 3.
