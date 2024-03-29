# Your name: Emmy Tran
# Your student id: 71422721
# Your email: emmytran@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code


# Create the class CootieCatcher
class CootieCatcher():

    # Create the constructor (__init__) method
    # Arguments: self (the curent object)
    #            A set of possible answers (a list), 
    #            A set of four numbers in the range from 0-7 inclusive (a list),
    #            A set of the remaining four numbers in the range from 0-7 inclusive that were not in the first list (a list) 
    # Return: None
    #
    # This method 
    # (1) sets this object's attribute answers_list to the passed list of possible answers (the argument of the method),
    # (2) set the attribute num1_list to the passed list num1s with four numbers in the range from 0-7 inclusive.  For example, (0, 3, 5, 6).
    # (3) set the attribute num2_list to the passed num2s with the remaining four numbers in the range from 0-7 inclusive that are not in num1s. 
    # (4) sets this object's attribute questions_history_list to an empty list,
    # (5) and sets this object's attribute answers_history_list to an empty list.
    def __init__(self, answers, num1s, num2s):
        self.answers_list = answers
        self.num1_list = num1s
        self.num2_list = num2s
        self.questions_history_list = []
        self.answers_history_list = []

    # Create the __str__ method
    # Argument: self (the curent object)
    # Return: a string with all of the answers in the answers_list separated by commas
    #
    # For example: 
    # for answer list ["Definitely", "Most likely", "It is certain", "Maybe", "Cannot predict now", "Very doubtful", "Don't count on it", "Absolutely not"], 
    # it should return a string, "["Definitely", "Most likely", "It is certain", "Maybe", "Cannot predict now", "Very doubtful", "Don't count on it", "Absolutely not"]"
    def __str__(self):
        return ','.join(self.answers_list)

    # Create the get_fortune method
    # Argument: self (the curent object)
    #           nums (the number list that pick should be in)
    #           pick (the number the user entered)
    # Return: an answer (string) 
    #
    # This method checks if pick is in nums and if not prints, “That number is not one you can choose! Please try again”.
    # and asks for another number.
    # if pick is in nums, it adds pick to the answers_history_list and returns the answer at that index from answers_list.
    def get_fortune(self, nums, pick):
        if pick not in nums:
            print("That number is not one you can choose! Please try again")
        else:
            self.answers_history_list.append(self.answers_list[pick])
            return self.answers_list[pick]

    # Create the ask method 
    # Arguments: self (the curent object)
    #            A question (string)
    # Return: An answer (string)
    #
    # The method takes a question and first checks if the question is already in the questions_history_list.
    # If so, it returns a string, "I've already answered that question”
    # Otherwise: 
    #   It adds the question to the questions_history_list
    #	Asks for the favorite color and if the length of the respose is even, use num1_list in the next step, else use num2_list. 
    #   Prompts the user to “Pick a number - <numbers from appropriate list here>: “ 
    #   Returns the answer from the get_fortune method.
    def ask(self, question):
        if question in self.questions_history_list:
            print("I've already answered that question")
        else:
            self.questions_history_list.append(question)
            favorite_color = input("What is your favorite color?")
            if len(favorite_color) % 2 == 0:
                num_list = self.num1_list
            else:
                num_list = self.num2_list
            while True:
                try:
                    pick = int(input(f"Pick a number - {num_list}: "))
                    fortune = self.get_fortune(num_list, pick)
                    return fortune
                except:
                    print("That number is not one you can choose! Please try again")


    # Create the print_question_history method
    # Argument: self (the curent object)
    # Return: None
    #
    # If there are no items in the questions_history_list, it prints "None yet"
    # Otherwise, 
    # the method prints "<number> <question> - <answer>" for each of the values in the questions_history_list, each on a separate line.
    def print_question_history(self):
        if not self.answers_history_list:
            print("None yet")
        else:
            for i in range(len(self.questions_history_list)):
                question = self.questions_history_list[i]
                answer = self.answers_history_list[i]
                print(f"{i+1} {question} - {answer}")
                    
def main():
    answers = ['Definitely', 'Most likely', 'it is certain', 'Maybe', 'Cannot predict now', 'Very doubtful', "Don't count on it", 'Absolutely now']
    nums1 = [1, 3, 5, 6]
    nums2 = [0, 2, 4, 7]
    cootie_catcher = CootieCatcher(answers, nums1, nums2)

    while True:
        question = input('Ask a question or type quit:')
        if question.lower == 'quit':
            break
        else:
            response = cootie_catcher.ask(question)
            print(f"{question} = {response}")
    # define the list of 8 possible answers

    # define the first list of numbers from 0 - 7 inclusive 
    # define the second list of numbers from 0 - 7 inclusive that were not in the first list

    # create the CootieCatcher object

    # Get the first question or "quit"

    # Loop while question is not "quit"

    # show the output of print_question_history 

    # remove pass when you write code above
    


# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    # test() #TODO: Uncomment if you do the extra credit
  


