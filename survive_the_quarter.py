
# Name: Jai Ajay Keni
# Group: C

# QUESTION 1: What goes in?
# The game reads scenarios from scenarios_C.csv.
# The file uses commas as separators and contains 14 columns:
# Event, Day, Decision 1, Decision 2, Decision 3,
# Reputation 1, Reputation 2, Reputation 3,
# Budget 1, Budget 2, Budget 3, Outcome 1, Outcome 2 and Outcome 3.
# Events contain the daily situations, decisions contain the choices,
# reputation and budget columns contain signed changes,
# and outcome columns contain feedback.
# Numbers are written as signed values such as +15 pts or -800 EUR.

# QUESTION 2: What happens?
# 1. The player enters their name and chooses a difficulty.
# 2. The game loads and shuffles the scenarios.
# 3. The player makes a choice (A, B or C).
# 4. The budget and reputation are updated.
# 5. A streak bonus may be awarded.
# 6. The game checks if the player is fired.
# 7. After 10 days, the final score and title are displayed.

# QUESTION 3: What comes out?
# The player sees their final budget, reputation, score and title.
# The best and worst moves are displayed.
# Results are saved in results.csv with name, budget,
# reputation, title and date.

# QUESTION 4: What could go wrong?
# 1. Invalid choices cause the game to ask again.
# 2. A missing CSV file displays an error message.
# 3. A budget or reputation at zero or below causes game over.
# 4. Invalid difficulty input causes the game to ask again.

# FEATURE CHOICE: Streak Bonus
# I chose the streak bonus because it rewards consecutive
# reputation gains. Three gains in a row award 500 EUR.

import csv
import random
from datetime import date


# Three custom scenarios added to the original CSV file
CUSTOM_SCENARIOS = [
    {
        "Event": "A drone delivery video goes viral after a croissant lands in a fountain.",
        "Day": "31",
        "Decision 1": "Turn it into a funny campaign",
        "Decision 2": "Apologize and refund the customer",
        "Decision 3": "Blame the drone manufacturer",
        "Reputation 1": "+15 pts",
        "Reputation 2": "+5 pts",
        "Reputation 3": "-15 pts",
        "Budget 1": "-500 EUR",
        "Budget 2": "-300 EUR",
        "Budget 3": "+0 EUR",
        "Outcome 1": "The campaign goes viral. People love your humor.",
        "Outcome 2": "The customer is happy, but the story fades.",
        "Outcome 3": "The manufacturer responds publicly. Not a good look."
    },
    {
        "Event": "A luxury fashion brand wants a limited-edition croissant collaboration.",
        "Day": "32",
        "Decision 1": "Accept the expensive collaboration",
        "Decision 2": "Suggest a smaller affordable partnership",
        "Decision 3": "Reject the offer",
        "Reputation 1": "+20 pts",
        "Reputation 2": "+10 pts",
        "Reputation 3": "-5 pts",
        "Budget 1": "-2500 EUR",
        "Budget 2": "-800 EUR",
        "Budget 3": "+0 EUR",
        "Outcome 1": "Your croissants become a luxury accessory.",
        "Outcome 2": "A smart partnership with a manageable budget.",
        "Outcome 3": "The fashion world moves on without you."
    },
    {
        "Event": "Customers complain that your new packaging is difficult to recycle.",
        "Day": "33",
        "Decision 1": "Switch to eco-friendly packaging",
        "Decision 2": "Explain your current packaging choices",
        "Decision 3": "Ignore the complaints",
        "Reputation 1": "+15 pts",
        "Reputation 2": "+5 pts",
        "Reputation 3": "-20 pts",
        "Budget 1": "-1800 EUR",
        "Budget 2": "-200 EUR",
        "Budget 3": "+0 EUR",
        "Outcome 1": "Customers appreciate the sustainable change.",
        "Outcome 2": "Some customers understand. Others remain skeptical.",
        "Outcome 3": "The complaints grow louder on social media."
    }
]


def add_custom_scenarios(filename):
    """Adds scenarios 31, 32 and 33 to the CSV file only once."""

    try:
        with open(filename, mode="r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            existing_rows = list(reader)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit(1)

    existing_days = {row["Day"] for row in existing_rows}

    new_scenarios = [
        scenario for scenario in CUSTOM_SCENARIOS
        if scenario["Day"] not in existing_days
    ]

    if new_scenarios:
        with open(filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(new_scenarios)

        print("Custom scenarios 31, 32 and 33 added to the CSV file.")

    else:
        print("Custom scenarios already exist in the CSV file.")


def load_scenarios(filename):
    """Reads scenarios from the CSV file and returns a list of dictionaries."""

    scenarios = []

    try:
        with open(filename, mode="r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                scenarios.append(row)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please place it in the same directory.")
        exit(1)

    return scenarios


def parse_int(value_str):
    """Converts strings like '+15 pts' or '-800 EUR' into integers."""

    cleaned = (
        value_str.replace(" pts", "")
        .replace(" EUR", "")
        .replace("+", "")
        .strip()
    )

    return int(cleaned)


def apply_choice(budget, reputation, choice_data):
    """Applies budget and reputation changes."""

    b_change, r_change = choice_data

    new_budget = budget + b_change
    new_reputation = reputation + r_change

    if new_reputation > 100:
        new_reputation = 100

    return new_budget, new_reputation


def calculate_score(budget, reputation):
    """Calculates the final score."""

    return reputation + budget // 200


def get_title(score):
    """Returns the title corresponding to the final score."""

    if score < 95:
        return "Eternal Intern"
    elif score <= 119:
        return "Growth Hacker"
    elif score <= 139:
        return "CMO Material"
    else:
        return "Viral Legend"


def save_result(name, budget, reputation, title):
    """Appends one line of game results to results.csv."""

    today_str = date.today().strftime("%Y-%m-%d")

    row = [
        name,
        f"{budget} EUR",
        f"{reputation}/100",
        title,
        today_str
    ]

    with open("results.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(row)


def main():

    print("========================================")
    print("       SURVIVE THE QUARTER: DRONE EDITION")
    print("========================================")

    # Ask for the player's name
    player_name = input("Enter your name, Lil Jedi: ").strip()

    if not player_name:
        player_name = "Anonymous"

    # Difficulty selection
    print("\nChoose your difficulty level:")
    print("1. Easy")
    print("2. Hard")

    while True:
        level = input("Enter 1 or 2: ").strip()

        if level == "1":
            budget = 15000
            print("\nEasy mode selected!")
            print("Starting budget: 15000 EUR")
            break

        elif level == "2":
            budget = 6000
            print("\nHard mode selected!")
            print("Starting budget: 6000 EUR")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

    reputation = 50

    # Add custom scenarios before loading the file
    add_custom_scenarios("scenarios_C.csv")

    # Load scenarios from group C file
    all_scenarios = load_scenarios("scenarios_C.csv")

    # Shuffle scenarios and select 10 days
    random.shuffle(all_scenarios)
    game_days = all_scenarios[:10]

    history = []
    streak_count = 0
    survived = True

    # Play the 10-day game
    for day_num, scen in enumerate(game_days, start=1):

        print("\n----------------------------------------")
        print(f"Day {day_num}")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(scen["Event"])

        print(f"A: {scen['Decision 1']}")
        print(f"B: {scen['Decision 2']}")
        print(f"C: {scen['Decision 3']}")

        # Validate player input
        while True:
            choice = input("Your choice (A, B or C): ").strip().lower()

            if choice in ["a", "b", "c"]:
                break

            print("Please type A, B or C.")

        # Map choice to decision index
        if choice == "a":
            idx = "1"
        elif choice == "b":
            idx = "2"
        else:
            idx = "3"

        # Retrieve selected decision information
        desc = scen[f"Decision {idx}"]
        b_change = parse_int(scen[f"Budget {idx}"])
        r_change = parse_int(scen[f"Reputation {idx}"])
        feedback = scen[f"Outcome {idx}"]

        # Apply decision impact
        budget, reputation = apply_choice(
            budget,
            reputation,
            (b_change, r_change)
        )

        print(f"\n{feedback}")

        b_str = f"+{b_change}" if b_change >= 0 else str(b_change)
        r_str = f"+{r_change}" if r_change >= 0 else str(r_change)

        print(f"Budget {b_str} EUR, Reputation {r_str}")

        # Check game-over conditions before bonus
        if budget <= 0 or reputation <= 0:
            survived = False
            history.append((r_change, desc, b_change))
            break

        # Streak bonus feature
        if r_change > 0:
            streak_count += 1

            if streak_count == 3:
                print(
                    "\nSTREAK BONUS! Three reputation gains in a row!"
                    " +500 EUR added!"
                )

                budget += 500
                streak_count = 0

        else:
            streak_count = 0

        # Store history as a tuple
        history.append((r_change, desc, b_change))

    # Display final results
    print("\n========================================")

    if not survived:
        print("Quarter failed! You are FIRED.")

        if budget <= 0:
            print(f"Reason: Budget hit {budget} EUR.")
        else:
            print(f"Reason: Reputation hit {reputation}/100.")

        title = "Fired"

    else:
        print("Quarter survived!")

        score = calculate_score(budget, reputation)
        title = get_title(score)

        print(f"Budget left: {budget} EUR")
        print(f"Reputation: {reputation}/100")
        print(f"Final score: {score}")
        print(f"{player_name}, your title: {title}")

    # Find best and worst reputation moves
    if history:
        best_move = max(history, key=lambda x: x[0])
        worst_move = min(history, key=lambda x: x[0])

        b_sign = "+" if best_move[0] >= 0 else ""
        w_sign = "+" if worst_move[0] >= 0 else ""

        print(
            f'Best move: "{best_move[1]}" '
            f"({b_sign}{best_move[0]} pts)"
        )

        print(
            f'Worst move: "{worst_move[1]}" '
            f"({w_sign}{worst_move[0]} pts)"
        )

    # Save results for every game
    save_result(player_name, budget, reputation, title)

    print("Saved in results.csv")


# Main program entry point
if __name__ == "__main__":
    main()
