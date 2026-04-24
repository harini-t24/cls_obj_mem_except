class InvalidoptionError(Exception): pass


class Quiz:
    def __init__(self):
        self.questions = [
            "1.which language is the mother of all programming languages?\nA.C\nB.Java\nC.Assembly\nD.Python",
            "2.What is the brain of the computer?\na.RAm\nB.Hard disk\nC.CPU\nD.Monitor",
            "3.Which data structure uses LIFO(Last In First Out)?\nA.Queue\nB.Stack\nC.Tree\nD.Graph",
            "4.Which of the following is not a programming paradigm?\nA.Object-Oriented\nB.Functional\nC.Procedural\nD.Mechanical",
            "5.which sorting is fastest in average case?\nA.Bubble\nB.Selection\nC.Quick\nD.Insertion sort",
            "6.Which protocol is used to transfer web pages?\na.FTP\nB.HTTP\nC.SMTP\nD.TCP",
            "7.Which of the following is a non linear data structure?\nA.Array\nB.Linked list\nC.stack\nD.Tree",
            "8.What is the default port number for HTTP?\nA.21\nB.25\nC.80\nD.443",
            "9.Which keyword is used to define a function in python?\nA.func\nB.define\nC.def\nD.function",
            "10.Which layer of OSI model is responsible for routing?\nA.Data link\nB.Transport\nC.Network\nD.Physical",
        ]
        self.answers = ['A', 'C', 'B', 'D', 'C', 'B', 'D', 'C', 'C', 'C']
        self.score = 0

    def startquiz(self):
        for i in range(len(self.questions)):
            while True:
                try:
                    print(self.questions[i])
                    userans = input("Enter option(A/B/C/D):").upper()

                    if userans not in ['A', 'B', 'C', 'D']:
                        raise InvalidoptionError
                    break

                except InvalidoptionError:
                    print("Invalid option! Please enter A/B/C/D\n")
            if userans == self.answers[i]:
                print("Correct\n")
                self.score += 1
            else:
                print("Wrong!")
                print("Correct answer is:", self.answers[i], "\n")

    def display(self):
        print("Final score:", self.score, "/", len(self.questions))
        if self.score <= 3:
            print("Grade:Needs Improvement")
        elif self.score <= 6:
            print("Grade:Good")
        else:
            print("Grade:Excellent")


q = Quiz()
q.startquiz()
q.display()
