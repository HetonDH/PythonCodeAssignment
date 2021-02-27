from random import randrange
import string



def random_choice_from_list(phrases):
    return phrases[randrange(0, len(phrases))]

def make_list_from_lines_in_file(filename):
    sentences = []
    with open(filename) as file:
        for line in file:
            sentences.append(line)
    return sentences

def convert_response_lines_into_dict(resp_list):
    dictionary = dict()
    for line in resp_list:
        entry_word = line.split(",")
        key = entry_word[0]
        phrase = entry_word[1]
        dictionary[key] = phrase
    return dictionary



class Chatter:
    def __init__(self, greetings, keyword_and_response, default_response):
        self.greetings = greetings
        self.keyword_and_response = keyword_and_response
        self.default_response = default_response
        self.keyword_and_response = convert_response_lines_into_dict(self.keyword_and_response)

    def greet(self):
        self.random_choice_from_list(self.greetings)

    def respond(self, human_text):
        human_text = human_text.lower()
        human_text = human_text.translate(str.maketrans('', '', string.punctuation))
        wordslist = human_text.split()
        potential_response = []
        for word in wordslist:
            if word in self.keyword_and_response:
                potential_response.append(self.keyword_and_response[word])
        if len(potential_response) == 0:
            potential_response = self.default_response
        print(random_choice_from_list(potential_response))


def main():
    greetings = make_list_from_lines_in_file("greetings.txt")
    responses = make_list_from_lines_in_file("responses.txt")
    default_responses = make_list_from_lines_in_file("default_responses.txt")
    robot = Chatter(greetings, responses, default_responses)
    print(random_choice_from_list(robot.greetings))
    while True:
        user_input = input("Enter message: ")
        robot.responses(user_input)
        if user_input == "stop":
            print("Bye Bye :)")
            break

if __name__ == '__main__':
   main()