### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No": 
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "0D0B7C61CB2FC1F81EA49CA221D2CDA4747988802B203E55FEA77228816BAB72"
    
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
        
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = "7"
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = "3"
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "Please verify the question from the list"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    
    debug_question = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    
    debug_question = "Is it possible to decrypt a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    
    debug_question = "Is it possible to decode a message without a key? - Yes/No"
    
    print(welcome_assignment_answers(debug_question))
    
    debug_question = "Is a hashed message supposed to be un-hashed? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    
    debug_question = "What is the SHA256 hashing value of your NYU email and use the answer in your code - "
    print(welcome_assignment_answers(debug_question))
    
    debug_question = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    
    debug_question = "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
    print(welcome_assignment_answers(debug_question))
    
    debug_question = "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    print(welcome_assignment_answers(debug_question))
#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": pcap
#"Are encoding and encryption the same? - Yes/No":NO
#"Is it possible to decrypt a message without a key? - Yes/No": No
#"Is it possible to decode a message without a key? - Yes/No": yes
#"Is a hashed message supposed to be un-hashed? - Yes/No": No
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ": 0D0B7C61CB2FC1F81EA49CA221D2CDA4747988802B203E55FEA77228816BAB72
#"Is MD5 a secured hashing algorithm? - Yes/No": No
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number": 7
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": 3
