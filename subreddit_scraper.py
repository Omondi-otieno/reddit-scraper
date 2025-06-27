import praw
import os
import sys
from dotenv import load_dotenv
import datetime as dt

# --- Load Environment Variables ---
load_dotenv()

# --- Get Credentials from Environment ---
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

# --- Main Application ---

def main():
    """
    Main function to connect to Reddit, search for posts based on user keywords
    within a specific subreddit, filter them by age (last 3 months),
    and save the results to a text file.
    """
    # Set stdout encoding to UTF-8 to handle special characters
    sys.stdout.reconfigure(encoding='utf-8')

    # Check if all credentials are loaded
    if not all([client_id, client_secret, user_agent]):
        print("Error: Missing Reddit API credentials in the .env file.")
        print("Please make sure your .env file has REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT.")
        return

    try:
        # Initialize the Reddit instance
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

        # --- SPECIFY YOUR TARGET SUBREDDIT HERE ---
        # Replace "YOUR_SUBREDDIT_NAME" with the actual name of the subreddit (e.g., "python", "learnprogramming").
        # Do NOT include "r/".
        target_subreddit_name = "HKUniversity"
        
        if target_subreddit_name == "YOUR_SUBREDDIT_NAME" or not target_subreddit_name:
            print("Error: Please specify a target subreddit name in the script (e.g., 'python').")
            return

        subreddit = reddit.subreddit(target_subreddit_name)

        # --- Define Keywords Here ---
        # You can add multiple keywords to this list.
        # The script will search for posts containing ANY of these keywords.
        keywords_list = ["2025"]
        keywords = " ".join(keywords_list) # Join keywords for the search query

        if not keywords_list:
            print("No keywords defined in the script. Exiting.")
            return

        print(f"Searching for posts in r/{target_subreddit_name} with keywords: '{keywords}'")

        # --- Time Filtering Setup ---
        # Calculate the timestamp for 3 months ago (approx 90 days)
        three_months_ago = dt.datetime.now() - dt.timedelta(days=90)
        three_months_ago_timestamp = three_months_ago.timestamp()

        # --- Prepare Output File ---
        # Create a safe filename from the keywords and subreddit name
        safe_keywords = "_".join(c for c in keywords_list if c.isalnum() or c in (' ', '_')).rstrip()
        output_filename = f"reddit_posts_{target_subreddit_name}_{safe_keywords.replace(' ', '_')}.txt"
        
        found_posts = False
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(f"--- Search Results from r/{target_subreddit_name} for '{keywords}' (last 3 months) ---\n\n")
            
            # --- Search and Filter Posts ---
            # PRAW's search time_filter doesn't support custom ranges, so we search and then filter manually.
            # We sort by 'new' to get the most recent posts first.
            for post in subreddit.search(keywords, sort='new', limit=100): # Increased limit to find more recent posts
                if post.created_utc > three_months_ago_timestamp:
                    found_posts = True
                    f.write(f"Title: {post.title}\n")
                    f.write(f"Score: {post.score}\n")
                    f.write(f"URL: {post.url}\n")
                    f.write(f"Date: {dt.datetime.fromtimestamp(post.created_utc)}\n")
                    f.write("---" * 20 + "\n")
                    
                    # Also print to console to show progress
                    print(f"Found post: {post.title}")

        if found_posts:
            print(f"\nSuccess! The results have been saved to '{output_filename}'")
        else:
            print(f"\nNo posts found matching your criteria in the last 3 months.")
            # Clean up the empty file if no posts were found
            os.remove(output_filename)


    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your credentials in the .env file are correct and you have a stable internet connection.")

if __name__ == "__main__":
    main()