import re
import sys

def main():
    # Read the HTML input from standard input
    html = sys.stdin.read()
    # Parse the HTML input and get the shorter URL
    url = parse(html)
    # Print the URL or a message if None
    if url:
        print(url)
    else:
        print("No YouTube URL found.")

def parse(html):
    # Define a regular expression pattern to match YouTube URLs in src attributes
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"'
    # Search for the pattern in the HTML input
    match = re.search(pattern, html)
    # If a match is found, extract the video ID and return the shorter URL
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    # If no match is found, return None
    else:
        return None

if __name__ == "__main__":
    main()
