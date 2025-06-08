import tkinter as tk #adds tkinter for the gui
from tkinter import messagebox #adds messageboxs in tkinter
import tkinter.font as tkFont

questions = [ #nested list of q & a
    {"question": "Kia ora is a Māori greeting.", "answer": True},
    {"question": "The Māori are the indigenous people of New Zealand.", "answer": True},
    {"question": "Whānau means food.", "answer": False},
    {"question": "Whānau means family.", "answer": True},
    {"question": "Aroha means love or compassion.", "answer": True},
    {"question": "The Māori arrived in New Zealand in the 1900s.", "answer": False},
    {"question": "The Māori arrived in New Zealand over 700 years ago.", "answer": True},
    {"question": "The haka is a traditional Māori dance.", "answer": True},
    {"question": "Kai means car.", "answer": False},
    {"question": "Kai means food.", "answer": True},
    {"question": "Wai means water.", "answer": True},
    {"question": "All Māori people live in Australia.", "answer": False},
    {"question": "Māori primarily live in New Zealand.", "answer": True},
    {"question": "Māori is one of New Zealand’s official languages.", "answer": True},
    {"question": "The Treaty of Waitangi was signed in 1990.", "answer": False},
    {"question": "The Treaty of Waitangi was signed in 1840.", "answer": True},
    {"question": "Marae is a traditional meeting place.", "answer": True},
    {"question": "Tamariki means grandparents.", "answer": False},
    {"question": "Tamariki means children.", "answer": True},
    {"question": "Koro means grandfather.", "answer": True},
    {"question": "The Māori alphabet includes the letter ‘s’.", "answer": False},
    {"question": "The Māori alphabet does not include the letter ‘s’.", "answer": True},
    {"question": "Māori myths often include taniwha (guardian creatures).", "answer": True},
    {"question": "Māori culture does not include carving or weaving.", "answer": False},
    {"question": "Māori culture includes carving and weaving as key art forms.", "answer": True},
    {"question": "A wharenui is a meeting house.", "answer": True},
    {"question": "Waka means flower.", "answer": False},
    {"question": "Waka means canoe.", "answer": True},
    {"question": "Mana refers to prestige and authority.", "answer": True},
    {"question": "Māori tattoos are called ta moko.", "answer": True},
    {"question": "The Māori language is only spoken by children.", "answer": False},
    {"question": "The Māori language is spoken by people of all ages.", "answer": True},
    {"question": "Puku means stomach or belly.", "answer": True},
    {"question": "Haka is only performed during war.", "answer": False},
    {"question": "Haka can be performed to welcome guests or celebrate events.", "answer": True},
    {"question": "Māori art often features spirals and natural patterns.", "answer": True},
    {"question": "Moana means ocean or sea.", "answer": True},
    {"question": "The word Aotearoa means Australia.", "answer": False},
    {"question": "Aotearoa is the Māori name for New Zealand.", "answer": True},
    {"question": "Māori is taught in some New Zealand schools.", "answer": True},
    {"question": "All Māori words come from English.", "answer": False},
    {"question": "Te Reo Māori is a Polynesian language, not based on English.", "answer": True},
    {"question": "Te Reo Māori means the Māori language.", "answer": True}
]

class TeReoQuiz: #makes the class for the quiz
    def __init__(self, root):
        self.root = root 
        self.root.title("Te Reo Māori Quiz") #makes window title
        self.root.geometry("500x400") #makes window size
        self.root.config(bg ="#2c610f") #makes background color

        self.current_q = 0 #sets the question
        self.score = 0 #sets the score

        self.title_label = tk.Label(root, text="Te Reo Māori Quiz", font=custom_font, bg="#e0f7d4", fg="#1a5d1a")
        self.title_label.pack(pady=20) #adds title wiht colour and font

        self.question_label = tk.Label(root, text="", font=custom_font, bg="#2c610f", wraplength=450)
        self.question_label.pack(pady=20) #adds question font

        self.true_button = tk.Button(root, text="True", font=custom_font, bg="#a5d6a7", width=10, command=lambda: self.check_answer(True))
        self.true_button.pack(pady=10) #adds true button and font

        self.false_button = tk.Button(root, text="False", font=custom_font, bg="#ef9a9a", width=10, command=lambda: self.check_answer(False))
        self.false_button.pack(pady=10) #adds false button with colour and font
        self.score_label = tk.Label(root, text="Score: 0", font=custom_font)
        self.score_label.pack(pady=20) #adds score text

        self.load_question() #loads the first question

    def load_question(self): #loads the question
        if self.current_q < len(questions): #checks if there are more questions
            q_text = questions[self.current_q]["question"] #gets the question text
            self.question_label.config(text=f"Q{self.current_q + 1}: {q_text}") #updates the question text
        else:
            messagebox.showinfo("Quiz Complete", f"Ka pai! Your final score: {self.score}/{len(questions)}") #goodbye message with score
            self.root.destroy() #closes the window

    def check_answer(self, user_answer): #checks the answer
        correct_answer = questions[self.current_q]["answer"] #gets the correct answer
        if user_answer == correct_answer:
            self.score += 1 #adds to the score
        self.current_q += 1 #shows question number
        self.score_label.config(text=f"Score: {self.score}") #updates the score text
        self.load_question() #loads the next question

root = tk.Tk() #creates the main window
custom_font = tkFont.Font(family="OpenDyslexicAlta", size=14) #adds my custom font
quiz_app = TeReoQuiz(root) #starts the quiz
root.mainloop() #loops until closed
