# pen-approvebot
import time
import praw
import getpass

print("Enter password. Password will not display whilst typing.")
APPROVE_AGE          = 120 # How old a post has to be (in seconds) before being approved. Default: 2 minutes.
CONFIG_CLIENT_ID     = "VpzTL7raRIbgrA" # Client ID from /prefs/apps
CONFIG_CLIENT_SECRET = "XV-orqjA1xpEmsFUvVoMuW16d3U" # Client secret from /prefs/apps
CONFIG_USERNAME      = "bjapprovebot" # Username for the bot account
CONFIG_PASSWORD      = "iapprovepenises"
CONFIG_SUBREDDITS    = ["penis"] # Subreddit(s) the script runs on
CONFIG_SCRIPTHOST    = "bjapprovebot" # Your Reddit username
CONFIG_USER_AGENT    = "Auto approves posts for /r/{} and more. Run by /u/{}".format(CONFIG_SUBREDDITS[0],
                                                                                     CONFIG_SCRIPTHOST)


def connect_to_reddit():
    return praw.Reddit(client_id=CONFIG_CLIENT_ID, client_secret=CONFIG_CLIENT_SECRET,
                       username=CONFIG_USERNAME, password=CONFIG_PASSWORD, user_agent=CONFIG_USER_AGENT)

def scan_submissions():
    for sub in CONFIG_SUBREDDITS:
        REPORTED = [item.id for item in reddit.subreddit(sub).mod.modqueue(only="submissions", limit=None)]
        for submission in reddit.subreddit(sub).mod.unmoderated(limit=None):
            if submission.id not in REPORTED and time.time() - submission.created_utc > APPROVE_AGE:
                submission.mod.approve()
                print("Approved {}.".format(submission.shortlink))

def main():
    while True:
        scan_submissions()
        time.sleep(APPROVE_AGE)


if __name__ == "__main__":
    reddit = connect_to_reddit()
    main()
