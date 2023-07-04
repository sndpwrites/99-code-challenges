import requests


def thread_downloader(reddit_url, file_location):
    reddit_url = reddit_url + ".json"
    print(reddit_url)
    try:
        res = requests.get(reddit_url)
        if res.status_code == 200:
            print(res.status_code)
            with open(file_location, "w", encoding="utf-8") as file:
                file.write(res.text)
            print("Thread has been downloaded to", file_location)
        else:
            print(res.text)
    except requests.exceptions.RequestException as e:
        print("Request exception", e)


thread_downloader(
    "https://www.reddit.com/r/i3wm/comments/pleu32/psa_were_moving_to_github_discussions",
    "response.json",
)
