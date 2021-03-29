from User import Examiner,Candidate

mohit=Examiner("Mohit Sir",77)
print(mohit)
mohit.addQuestion("python","easy")
mohit.displayAllQuestions()

C=Candidate("Pranit",7)
print(C)
C.viewTopics()
C.run_test()