import time
import requests
import os
import string
from bs4 import BeautifulSoup


def download_names():
    url = "https://www.behindthename.com/random/random.php?number=2&gender=u&surname=&all=yes"
    for i in range(500):
        with open(os.path.abspath("resources/raw_names.txt"), 'a', encoding='utf-8') as f:
            req_name = requests.get(url)
            soup = BeautifulSoup(req_name.text, "html.parser")
            last_name = soup.find_all("a", class_="plain")[1]
            invalid_letter = False
            for letter in last_name.string:
                if letter not in string.ascii_letters:
                    invalid_letter = True
                    break
            if not invalid_letter:
                print(i, last_name.string)
                f.write(last_name.string + "\n")
                time.sleep(0.01)
            else:
                print("SKIPPING", i, last_name.string)


def remove_dupe_names():
    name_set = set()
    with open(os.path.abspath("resources/raw_names.txt"), encoding='utf-8') as f:
        for name in f.readlines():
            name_set.add(name.strip())
    print(name_set)
    print(len(name_set))
    with open(os.path.abspath("resources/names.txt"), 'a', encoding='utf-8') as f:
        for name in name_set:
            f.write(name + '\n')
    print("DONE")


if __name__ == '__main__':
    remove_dupe_names()
