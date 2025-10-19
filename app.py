import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class CrimeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Interrogatório Criminal 🕵️")
        self.master.geometry("500x250")
        self.master.configure(bg="#2E2E2E")
        self.master.resizable(False, False)

        self.perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"
        ]
        self.current_question_index = 0
        self.respostas_positivas = 0

        self.setup_styles()
        self.create_widgets()
        self.display_question()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#2E2E2E')
        style.configure('TLabel', background='#2E2E2E', foreground='white', font=('Segoe UI', 14))
        style.configure('TButton', font=('Segoe UI', 12, 'bold'), padding=10)
        style.map('TButton',
                  foreground=[('active', 'white')],
                  background=[('active', '#555555')])

    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="20 20 20 20")
        main_frame.pack(expand=True, fill='both')

        self.question_label = ttk.Label(main_frame, text="", wraplength=450, justify='center')
        self.question_label.pack(pady=(20, 30))

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)

        sim_button = ttk.Button(button_frame, text="Sim", command=lambda: self.process_answer(True))
        sim_button.pack(side='left', padx=15)

        nao_button = ttk.Button(button_frame, text="Não", command=lambda: self.process_answer(False))
        nao_button.pack(side='left', padx=15)

    def display_question(self):
        if self.current_question_index < len(self.perguntas):
            question_text = self.perguntas[self.current_question_index]
            self.question_label.config(text=question_text)
        else:
            self.show_result()

    def process_answer(self, answer_is_yes):
        if answer_is_yes:
            self.respostas_positivas += 1
        self.current_question_index += 1
        self.display_question()

    def show_result(self):
        count = self.respostas_positivas
        if count == 2:
            classificacao = "Suspeita"
        elif 3 <= count <= 4:
            classificacao = "Cúmplice"
        elif count == 5:
            classificacao = "Assassino"
        else:
            classificacao = "Inocente"

        messagebox.showinfo("Resultado da Análise", f"A pessoa foi classificada como: {classificacao}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CrimeApp(root)
    root.mainloop()
