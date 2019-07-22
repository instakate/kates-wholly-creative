# This is a quiz program written in Python.
# There are three questions.
# Question 1. How many Os are in the name Oblobloboly Oblogoblogan?
# Answer: There are 8.
# Question 2. Yes or no, do you pick your nose when no one is looking?
# The correct answer is yes. We appreciate your honesty. Do not lie to the quiz. 
# Question 3. Neil Armstrong was the first man on the moon. What is "Neil A" spelled backwards?
# The correct answer is Alien. The FBI has asked me to delete this question.
# Start of pseudocode.
# Set the variable counter to 0. This will count the score.
# Ask the first question, assign the answer to variable question1.
# If the answer is correct, add a point to the counter. 
# Provide feedback on the question. Give the current score. 
# Ask the second question, assign the answer to variable question2.
# If the answer is correct, add a point to the counter.
# Provide feedback on the question. Give the current score.
# Ask the third question, assign the answer to variable question3.
# If the answer is correct, add a point to the counter.
# Provide feedback on the question.
# Give the total score. Congratulate the user for their efforts. No one is perfect. This was a pretty hard quiz.
# End of pseudocode. 

def main():
        # Set the counter to 0 to keep score.
        counter = 0

        # First question
        print('Welcome to Kate\'s wholly creative quiz program! Do your best.')
        print(' ')
        print('Question 1.')
        question1 = int(input('How many Os are in the name Oblobloboly Oblogoblogan? '))
        if question1 == 8:
                counter = counter + 1
                print('That is correct. ')
                print('There are 8 Os in Oblobloboly Oblogoblogan. You\'re pretty smart.')
                print('Your score is ',counter,'/1.',sep='')
        else:
                print('Look again! Good try. There are 8 Os in this common name. ')
                print('Your score is ',counter,'/1.',sep='')
        print(' ')
        
        # Second question
        print('Question 2.')
        question2 = str(input('Answer yes or no: Do you pick your nose when no one else is looking? '))
        if question2 == 'Yes' or question2 == 'yes' or question2 == 'YES' :
                counter = counter + 1
                print ('We enjoy your honesty in this important quiz! Your answer earns a point.')
                print ('Your score is ',counter,'/2.',sep='')
        else:
                print ('Do not lie to the quiz. Your score is ',counter,'/2.',sep='')
        print('')

        # Third question
        print('Question 3.')
        question3 = str(input('Neil Armstrong was the first man on the moon. What is "Neil A" spelled backwards? '))
        if question3 == ('Alien') or question3 ==('a lien') or question3 == ('alien') or question3 == ('A Lien') or \
                        question3 == ('A lien') or question3 == ('ALIEN') or question3 == ('A LIEN') or question3 == ('A lieN'):
                counter = counter + 1
                print ('That is correct. "Neil A" backwards is "Alien".')
                print('The FBI has asked me to delete this question.')
        else:
                print('The correct answer is "alien". If you\'re from the government, I deleted this question.')
        print('')
        
        # Give the final score
        if counter == 3:
                print('Congratulations!! Your score is',counter,'out of a possible score of 3. '
                      'You got a perfect score! You are perfect.')
        else: 
                print('You completed this quiz with a score of',counter,'out of 3. Ouch. No one is perfect. ')
                print('This was a pretty hard quiz. Try again.')

main()
