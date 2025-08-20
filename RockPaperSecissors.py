import random
import emoji
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(seconds=0.6):
    time.sleep(seconds)

# Messages
win_msg     = emoji.emojize("You Win! :trophy: :smiling_face_with_sunglasses: :clap:")
lose_msg    = emoji.emojize("You lose! :crying_face: :broken_heart: :cross_mark:")
draw_msg    = emoji.emojize("It's a draw! :handshake: :neutral_face:")
invalid_msg = emoji.emojize("Invalid input! :warning: :thinking_face:")

# Move emojis
stone   = emoji.emojize(":oncoming_fist:")
paper   = emoji.emojize(":raised_hand:")
scissor = emoji.emojize(":victory_hand:")

moves = {
    0: ("Stone", stone),
    1: ("Paper", paper),
    2: ("Scissors", scissor),
}

# (user, comp) pairs that are wins for user
rules = {(0, 2), (2, 1), (1, 0)}

def get_user_choice():
    prompt = (
        f"Choose your move:\n"
        f"  0: Stone {stone}\n"
        f"  1: Paper {paper}\n"
        f"  2: Scissors {scissor}\n"
        f"Enter 0/1/2: "
    )
    while True:
        raw = input(prompt).strip()
        if raw in {"0", "1", "2"}:
            return int(raw)
        print(invalid_msg)

def play_round():
    user = get_user_choice()
    comp = random.randint(0, 2)

    clear()
    u_name, u_emoji = moves[user]
    c_name, c_emoji = moves[comp]

    print("You throw...", end="", flush=True); pause(0.4); print(f" {u_name} {u_emoji}")
    pause(0.4)
    print("Computer throws...", end="", flush=True); pause(0.4); print(f" {c_name} {c_emoji}\n")
    pause(0.3)

    if user == comp:
        print(draw_msg)
        outcome = "draw"
    elif (user, comp) in rules:
        print(win_msg)
        outcome = "win"
    else:
        print(lose_msg)
        outcome = "lose"
    return outcome

def best_of(n=5):
    target = n // 2 + 1
    user_wins = comp_wins = draws = 0
    streak = 0
    round_no = 1

    while user_wins < target and comp_wins < target:
        print(f"\n— Round {round_no} of best-of-{n} —")
        outcome = play_round()

        if outcome == "win":
            user_wins += 1
            streak = streak + 1 if streak >= 0 else 1
        elif outcome == "lose":
            comp_wins += 1
            streak = streak - 1 if streak <= 0 else -1
        else:
            draws += 1
            streak = 0

        # Scoreboard
        bar_user = "█" * user_wins + "·" * (target - user_wins)
        bar_comp = "█" * comp_wins + "·" * (target - comp_wins)
        print("\nScoreboard:")
        print(f"  You [{bar_user}]  {user_wins}/{target}")
        print(f"  CPU [{bar_comp}]  {comp_wins}/{target}")
        if draws:
            print(f"  Draws: {draws}")
        if streak >= 2:
            print(emoji.emojize("🔥 You're on a streak! :fire:"))
        elif streak <= -2:
            print(emoji.emojize("🥶 CPU streak! :cold_face:"))

        round_no += 1
        pause(1.0); clear()

    print("\nFinal result:")
    if user_wins > comp_wins:
        print(emoji.emojize("🏆 You won the match! :party_popper:"))
    else:
        print(emoji.emojize("💀 CPU won the match. :skull:  Try again!"))

    print(f"\nSummary — You {user_wins} · CPU {comp_wins} · Draws {draws}")

def ask_yes_no(msg="Play again? [Y/N]: "):
    while True:
        ans = input(msg).strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print(invalid_msg)

def main():
    clear()
    print(emoji.emojize("🪨 ✋ ✂️  Stone–Paper–Scissors  :collision:\n"))
    while True:
        try:
            raw = input("Best‑of how many rounds? (3/5/7) [default 5]: ").strip()
            n = int(raw) if raw else 5
            if n not in {3, 5, 7}:
                print("Choose 3, 5 or 7."); continue
        except ValueError:
            print("Please enter a number like 3, 5 or 7."); continue

        clear()
        best_of(n)
        print()
        if not ask_yes_no():
            print(emoji.emojize("\nThanks for playing! :waving_hand:"))
            break
        clear()

if __name__ == "__main__":
    main()
