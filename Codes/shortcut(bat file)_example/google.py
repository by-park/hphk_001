import webbrowser
import sys

url = "https://www.google.com/search?q="
keyword = sys.argv[1]
webbrowser.open(url + keyword)