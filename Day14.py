# Higher or Lower Project
import random 

vs = """            
__  ________
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/ 
           """
data = [
    {
        'name': 'Ram Charan',
        'follower_count': 29,
        'description': 'Tollywood Actor',
        'country': 'India',
    },
    {
        'name': 'Allu Arjun',
        'follower_count': 28,
        'description': 'Tollywood Actor',
        'country': 'India',
    },
    {
        'name': 'NTR',
        'follower_count': 10,
        'description': 'Tollywood Actor',
        'country': 'India',
    },
    {
        'name': 'Prabhas',
        'follower_count': 15,
        'description': 'Tollywood Actor',
        'country': 'India',
    },
    {
        'name': 'Pawan Kalyan',
        'follower_count': 27,
        'description': 'Tollywood Actor',
        'country': 'India',
    },
    {
        'name': 'Mahesh Babu',
        'follower_count': 20,
        'description': 'Tollywood Actor',
        'country': 'India',
    },
    {
        'name': 'Vijay Talapathy',
        'follower_count': 11,
        'description': 'Kollywood Actor',
        'country': 'India',
    },
    {
        'name': 'Suriya',
        'follower_count': 18,
        'description': 'Kollywood Actor',
        'country': 'India',
    },
    {
        'name': 'Yash',
        'follower_count': 23,
        'description': 'Sandalwood Actor',
        'country': 'India',
    },
    {
        'name': 'Dhanush',
        'follower_count': 8,
        'description': 'Kollywood Actor',
        'country': 'India',
    },
    {
        'name': 'Ronaldo',
        'follower_count': 291,
        'description': 'Football Player',
        'country': 'Portugal',
    },
    {
        'name': 'Messi',
        'follower_count': 270,
        'description': 'Football Player',
        'country': 'Argentina',
    },
    {
        'name': 'Neymar',
        'follower_count': 100,
        'description': 'Football Player',
        'country': 'Brazil',
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 200,
        'description': 'Indian Cricketer',
        'country': 'India',
    },
    {
        'name': 'M S Dhoni',
        'follower_count': 277,
        'description': 'Indian Cricketer',
        'country': 'India',
    },
    {
        'name': 'Suresh Raina',
        'follower_count': 244,
        'description': 'Indian Cricketer',
        'country': 'India',
    },
    {
        'name': 'Robert Downwey Jr',
        'follower_count': 70,
        'description': 'Tollywood Actor',
        'country': 'India',
    },
]

# Format the account data into printable format
def format_data(account):
    """Takes the account data returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    """Take's a user guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
# Generate a random account from the game data
score = 0

game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")



    # Ask user to guess
    guess = input("Who has more Followers? Type 'A' or 'B': ").lower()


    # Check if user is correct
    # --Get folower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # --Use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're Right! Current score {score}")
    else:
        print(f"Sorry, That's Wrong. Final score {score}")
        game_should_continue = False


    # Score Keeping


    # Make the game repeatable


    # Making account at position B become the next account at position A