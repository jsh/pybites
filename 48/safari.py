"""Bite 48. Make a bar chart of new Safari books."""
import os
import re
import urllib.request
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def create_chart():
    """Print a simple bar chart from the data."""
    books = defaultdict(list)
    with open(SAFARI_LOGS, encoding="utf-8") as fd_in:
        buf = ""
        date = r"\d\d-\d\d"
        time = r"\d\d:\d\d"
        user = r"\S+"
        other = r"\S+"
        id = r"\w+"
        title = r".*"
        # 02-13 01:59 root         DEBUG    9781788838542 - WinOps - DevOps on the Microsoft Azure Stack: VSTS and TFS 2018
        pat = re.compile(fr"{date}\s{time}\s+{user}\s+{other}\s+{id}\s+-\s+({title})$")
        for line in fd_in:
            if "sending to slack channel" in line:
                date = line[:5]
                match = pat.match(buf)
                if match:
                    book = match.group(1)
                    books[date].append(book)
            buf = line
        for date, books in books.items():
            line = [PY_BOOK if "Python" in book else OTHER_BOOK for book in books]
            print(date, "".join(line))
