import requests
import string
from bs4 import BeautifulSoup


def find_marked_textV2(text, start_marker, end_marker):
    found_text = []
    more_to_search = True
    while more_to_search:
        start = text.find(start_marker)
        end = text.find(end_marker, start)
        if start == -1 and end == -1:
            more_to_search = False
        else:
            phrase = text[start + len(start_marker):end]
            # print(phrase)
            # print("----------------------------------")
            found_text.append(phrase)
            text = text[end + len(end_marker):]

    return found_text


def main():
    f = open("stop_words.txt")
    stop_words = []
    for word in f.readlines():
        word = word.rstrip('\n')
        stop_words.append(word)

    low_word_dict = dict()
    high_word_dict = dict()

    for i in range(0, 3):
        rev_num = i*20
        url = 'https://www.yelp.com/biz/taco-bell-salt-lake-city-10?osq=taco+bell' + str(rev_num)
        # Get the html text for that page
        page = requests.get(url)
        htmltext = page.text
        # print(htmltext)
        soup = BeautifulSoup(htmltext)
        content = soup.find_all(lang="en")
        reviews = []
        for con in content[1:]:
            cont = find_marked_textV2(str(con), 'lang="en">', "</span>")
            if len(cont)>0:
                # print(cont)
                reviews.extend(cont)
        print(len(reviews))

        content = []
        for sentence in reviews:
            find = True
            while find:
                start = sentence.find("<br/>")
                if start == -1:
                    content.append(sentence)
                    find = False
                else:
                    sentence = sentence[:start]+sentence[start+5:]

        content1 = []
        for sentence in content:
            find = True
            while find:
                start = sentence.find("\xa0")
                if start == -1:
                    content1.append(sentence)
                    find = False
                else:
                    sentence = sentence[:start]+sentence[start+3:]

        text = [str.lower(sentence) for sentence in content1]
        text = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in text]
        for sentence in text:
            words = sentence.split(' ')
            words = [word for word in words if word not in stop_words]
            for word in words:
                if len(word) > 0:
                    if word in low_word_dict.keys():
                        low_word_dict[word] = low_word_dict[word] + 1
                    else:
                        low_word_dict[word] = 1
        # print(low_word_dict)

    for i in range(0, 25):
        rev_num = i*20
        url = 'https://www.yelp.com/biz/hsl-salt-lake-city?osq=HSL' + str(rev_num)
        # Get the html text for that page
        page = requests.get(url)
        htmltext = page.text
        # print(htmltext)
        soup = BeautifulSoup(htmltext)
        content = soup.find_all(lang="en")
        reviews = []
        for con in content[1:]:
            cont = find_marked_textV2(str(con), 'lang="en">', "</span>")
            if len(cont)>0:
                # print(cont)
                reviews.extend(cont)
        print(len(reviews))

        content = []
        for sentence in reviews:
            find = True
            while find:
                start = sentence.find("<br/>")
                if start == -1:
                    content.append(sentence)
                    find = False
                else:
                    sentence = sentence[:start]+sentence[start+5:]

        content1 = []
        for sentence in content:
            find = True
            while find:
                start = sentence.find("\xa0")
                if start == -1:
                    content1.append(sentence)
                    find = False
                else:
                    sentence = sentence[:start]+sentence[start+3:]

        text = [str.lower(sentence) for sentence in content1]
        text = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in text]
        for sentence in text:
            words = sentence.split(' ')
            words = [word for word in words if word not in stop_words]
            for word in words:
                if len(word) > 0:
                    if word in high_word_dict.keys():
                        high_word_dict[word] = high_word_dict[word] + 1
                    else:
                        high_word_dict[word] = 1
        print(high_word_dict)

    low_word_dict = sorted(low_word_dict.items(), key=lambda d:d[1], reverse=True)
    print(low_word_dict)
    with open("low_dict.txt","w") as f:
        for dic in low_word_dict:
            f.write(str(dic[1]))
            f.write(",")
            f.write(dic[0])
            f.write("\n")

    high_word_dict = sorted(high_word_dict.items(), key=lambda d:d[1], reverse=True)
    print(high_word_dict)
    with open("high_dict.txt","w") as f:
        for dic in high_word_dict:
            f.write(str(dic[1]))
            f.write(",")
            f.write(dic[0])
            f.write("\n")


if __name__ == '__main__':
    main()

