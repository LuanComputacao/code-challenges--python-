import re


def clear_text(text: str):
    return re.sub(r"([^a-zA-Z])+", " ", text.lower()).strip().split(" ")


def process_words(text):
    top_t = [("", 0), ("", 0), ("", 0)]
    words = {}
    for word in text:
        words[word] = words.setdefault(word, 0) + 1
        current_count = words[word]

        l_top = len(top_t)
        for x in range(l_top):
            if top_t[x][0] == word:
                if current_count > top_t[x][1]:
                    top_t[x] = (word, current_count)
                break
            else:
                if current_count > top_t[x][1]:
                    next = x + 1
                    if next < l_top:
                        top_t[next] = top_t[x]
                        top_t[x] = (word, current_count)
                    elif next == l_top:
                        top_t[x] = (word, current_count)
                    break
    return words, top_t


if __name__ == "__main__":
    from pprint import pprint

    text = "Hello world! Hello Python. Python is great, and the world is big."
    text = clear_text(text)
    data, hank = process_words(text)
    pprint(data)
    pprint(hank)
