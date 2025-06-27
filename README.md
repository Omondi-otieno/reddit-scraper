# Reddit Scraper

This is a Python web scraper that uses the PRAW (Python Reddit API Wrapper) library to extract Reddit posts.

## Features:

- Searches for posts across all of Reddit based on user-defined keywords.
- Filters posts to include only those published within the last 3 months.
- Saves the extracted post titles, scores, URLs, and dates to a text file.
- Keywords are defined directly within the `reddit_scraper.py` file for easy modification.

## Setup:

1.  **Clone this repository** (after it's pushed to GitHub).
2.  **Install dependencies:** `pip install praw python-dotenv`
3.  **Get Reddit API Credentials:** Follow the instructions [here](https://www.reddit.com/prefs/apps) to create a "script" application and obtain your `client_id` and `client_secret`. Set the `redirect uri` to `http://localhost:8080`.
4.  **Create a `.env` file** in the project root with your credentials:
    ```
    REDDIT_CLIENT_ID="YOUR_CLIENT_ID"
    REDDIT_CLIENT_SECRET="YOUR_CLIENT_SECRET"
    REDDIT_USER_AGENT="MyScraper/1.0 by u/YourRedditUsername"
    ```
5.  **Define Keywords:** Open `reddit_scraper.py` and modify the `keywords_list` variable with your desired search terms.

## Usage:

Run the script from your terminal:

```bash
python reddit_scraper.py
```

The results will be saved to a text file named `reddit_posts_[your_keywords].txt` in the same directory.
