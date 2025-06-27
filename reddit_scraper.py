import praw
import os
from dotenv import load_dotenv

# --- Load Environment Variables ---
# This will load the variables from the .env file in the same directory.
load_dotenv()

# --- Get Credentials from Environment ---
# Replace these with the actual variable names from your .env file if you changed them.
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

# --- Main Application ---

def main():
    """
    Main function to connect to Reddit, fetch posts, and print them.
    """
    # Check if all credentials are loaded
    if not all([client_id, client_secret, user_agent]):
        print("Error: Missing Reddit API credentials in the .env file.")
        print("Please make sure your .env file has REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT.")
        return

    try:
        # Initialize the Reddit instance with your credentials
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

        # Specify the subreddit you want to scrape
        subreddit_name = "learnpython"
        subreddit = reddit.subreddit(subreddit_name)

        print(f"--- Top 10 Hot Posts from r/{subreddit_name} ---")

        # Fetch the top 10 "hot" posts from the subreddit
        for post in subreddit.hot(limit=10):
            print(f"Title: {post.title}")
            print(f"Score: {post.score}")
            print(f"URL: {post.url}")
            print("-" * 20)

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your credentials in the .env file are correct and you have a stable internet connection.")

if __name__ == "__main__":
    main()