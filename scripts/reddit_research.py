"""
reddit_research.py -- Direxter's intelligence tool
Pulls top posts from r/smallstreetbets and r/wallstreetbets,
analyzes format patterns, and writes a report for PR strategy.

SETUP (one time):
  1. Go to https://www.reddit.com/prefs/apps
  2. Click "create another app" at the bottom
  3. Name it anything (e.g. "island-fund-research")
  4. Select "script"
  5. Redirect URI: http://localhost:8080
  6. Click "create app"
  7. Copy: client_id (under the app name), client_secret
  8. Set environment variables or paste below

  pip install praw
"""

import praw
import os
from datetime import datetime
from collections import Counter

# --- CREDENTIALS ---
# Set these as env vars: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET
# Or paste directly (don't commit to git):
CLIENT_ID = os.environ.get("REDDIT_CLIENT_ID", "PASTE_HERE")
CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET", "PASTE_HERE")
USER_AGENT = "island-fund-research/0.1 by padraik"

# --- CONFIG ---
SUBREDDITS = ["smallstreetbets", "wallstreetbets"]
TIME_FILTER = "month"   # hour / day / week / month / year / all
POST_LIMIT = 50
OUTPUT_FILE = "C:/LifeCoach/island-fund-repo/PR/notes/reddit_research_report.md"


def analyze_posts(subreddit_name, reddit):
    sub = reddit.subreddit(subreddit_name)
    posts = []

    for post in sub.top(time_filter=TIME_FILTER, limit=POST_LIMIT):
        text_len = len(post.selftext) if post.selftext else 0
        posts.append({
            "rank": len(posts) + 1,
            "title": post.title,
            "score": post.score,
            "comments": post.num_comments,
            "flair": post.link_flair_text or "none",
            "has_image": post.url.endswith((".jpg", ".jpeg", ".png", ".gif")) or "imgur" in post.url or "i.redd.it" in post.url,
            "is_text": post.is_self,
            "text_length": text_len,
            "upvote_ratio": post.upvote_ratio,
            "url": f"https://reddit.com{post.permalink}",
        })

    return posts


def write_report(all_data):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Reddit Research Report\n")
        f.write(f"*Direxter -- generated {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
        f.write(f"*Time filter: top/{TIME_FILTER} | {POST_LIMIT} posts per subreddit*\n\n")
        f.write("---\n\n")

        for sub_name, posts in all_data.items():
            f.write(f"## r/{sub_name}\n\n")

            # --- AGGREGATE STATS ---
            scores = [p["score"] for p in posts]
            comments = [p["comments"] for p in posts]
            image_count = sum(1 for p in posts if p["has_image"])
            text_count = sum(1 for p in posts if p["is_text"])
            flairs = Counter(p["flair"] for p in posts)
            long_text = [p for p in posts if p["text_length"] > 500]
            short_text = [p for p in posts if p["is_text"] and p["text_length"] <= 500]

            f.write("### Aggregate Stats\n\n")
            f.write(f"| Metric | Value |\n|---|---|\n")
            f.write(f"| Avg score (top {POST_LIMIT}) | {sum(scores)//len(scores):,} |\n")
            f.write(f"| Median score | {sorted(scores)[len(scores)//2]:,} |\n")
            f.write(f"| Avg comments | {sum(comments)//len(comments):,} |\n")
            f.write(f"| Posts with image/screenshot | {image_count} ({image_count*100//len(posts)}%) |\n")
            f.write(f"| Text-only posts | {text_count} ({text_count*100//len(posts)}%) |\n")
            f.write(f"| Long text posts (500+ chars) | {len(long_text)} |\n\n")

            f.write("### Flair Breakdown\n\n")
            f.write("| Flair | Count |\n|---|---|\n")
            for flair, count in flairs.most_common():
                f.write(f"| {flair} | {count} |\n")
            f.write("\n")

            # --- TOP 10 TITLES ---
            f.write("### Top 10 Post Titles\n\n")
            for p in posts[:10]:
                img_flag = " [img]" if p["has_image"] else ""
                f.write(f"{p['rank']}. **{p['title']}**{img_flag}\n")
                f.write(f"   Score: {p['score']:,} | Comments: {p['comments']} | Flair: {p['flair']}\n\n")

            # --- TITLE PATTERN ANALYSIS ---
            f.write("### Title Patterns (top 25)\n\n")
            starts_with_number = sum(1 for p in posts[:25] if p["title"][0].isdigit() or p["title"].startswith("$"))
            has_percent = sum(1 for p in posts[:25] if "%" in p["title"])
            has_dollar = sum(1 for p in posts[:25] if "$" in p["title"])
            is_question = sum(1 for p in posts[:25] if p["title"].endswith("?"))
            all_caps_word = sum(1 for p in posts[:25] if any(w.isupper() and len(w) > 2 for w in p["title"].split()))

            f.write(f"- Starts with number or $: {starts_with_number}/25\n")
            f.write(f"- Contains %: {has_percent}/25\n")
            f.write(f"- Contains $: {has_dollar}/25\n")
            f.write(f"- Ends with ?: {is_question}/25\n")
            f.write(f"- Has ALL-CAPS word: {all_caps_word}/25\n\n")

            # --- HIGH COMMENT-TO-SCORE RATIO (discussion bait) ---
            f.write("### Most Discussion-Heavy Posts (high comment/score ratio)\n\n")
            discussion_posts = sorted(posts, key=lambda p: p["comments"] / max(p["score"], 1), reverse=True)[:5]
            for p in discussion_posts:
                f.write(f"- **{p['title']}** -- {p['comments']} comments, {p['score']} score\n")
            f.write("\n")

            f.write("---\n\n")

        # --- DIREXTER NOTES ---
        f.write("## Direxter Notes\n\n")
        f.write("*Fill in after reviewing the data above.*\n\n")
        f.write("**What title formats dominated:**\n\n")
        f.write("**What flairs got the most traction:**\n\n")
        f.write("**Image vs text breakdown:**\n\n")
        f.write("**Tone observations from top 10 titles:**\n\n")
        f.write("**What this means for our intro post:**\n\n")


def main():
    if CLIENT_ID == "PASTE_HERE":
        print("ERROR: Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET before running.")
        print("See setup instructions at top of this file.")
        return

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
    )

    print(f"Pulling top/{TIME_FILTER} posts from {SUBREDDITS}...")
    all_data = {}
    for sub_name in SUBREDDITS:
        print(f"  Fetching r/{sub_name}...")
        all_data[sub_name] = analyze_posts(sub_name, reddit)
        print(f"  Got {len(all_data[sub_name])} posts.")

    write_report(all_data)
    print(f"\nReport written to: {OUTPUT_FILE}")
    print("Open it and fill in the Direxter Notes section.")


if __name__ == "__main__":
    main()
