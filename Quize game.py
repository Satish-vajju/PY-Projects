print("---------------------------Quize game-----------------------------------")

# Define the quiz questions
questions=("1.Who is known as the God of Cricket ?",                
           "2.What is the maximum number of players allowed on the field for a team during a cricket? ",
           "3.What is the term used when a batsman scores 100 runs in a single inning?",
           "4.Which country won the first-ever Cricket World Cup in 1975? ",
           "5.How many runs are awarded for hitting the ball over the boundary without touching the ground?")

# Define the options for each and every question
options=(("A. Ricky Ponting", "B.Sachin Tendulkar", "C Virat Kohlid","D.M.S. Dhoni"),
         ("A.10 ","B.9","C.11","D.12"),
         ("A.Half-century","B Century","C.Double-century", "D.Triple-century"),
         ("A.Australia", "B.England", "C.India", "D.West Indies"),
         ("A.4","B.5","C.6","D.7"))
# Define the correct answers
answers=["B","C","B","D","C"] 
# Initialize an empty list to store user guesses
guesses=[]
#Initialize the score counter
score=0  
# Initialize the question number index
question_num=0 

# Iterate over each question
for question in questions: 
    print("----------------------")
    print(question) #display the current questions
     # Display the options for the current question
    for option in options[question_num]: 
        print(option)  

    # Prompt the user for their answer and convert to uppercase
    guess=input("Enter the options(A,B,C,D): ").upper() 
    guesses.append(guess)     # Store the user's guess
       # Check if the user's guess is correct
    if guess==answers[question_num]: 
        score+=1  # Increment the score for a correct answer
        print("correct answer!") # Inform the user they are correct
    else:        
        print("Incorrect answer!") # Inform the user they are incorrect
           # Display the correct answer for the current question
        print(f"The correct answer is {answers[question_num]}")
    question_num+=1   # Move to the next question
# Display the final results
print("------------------------")
print("        result          ")
print("------------------------")
# Print the correct answers
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print()  # Line break for readability

# Print the user's guesses
print("guess: ", end=" ")
for guess in guesses:
    print(guess, end=" ")

print()  # Line break for readability
 #Calculate the score as a percentage
score=int(score/len(questions)*100)
print(f"Your score is: {score}%") # Display the user's score as a percentage
