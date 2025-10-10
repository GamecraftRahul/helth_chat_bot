from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import askstring
import re
from bot import getresponse, get_pridected_value, get_diesese_practions

# ============================
# Colors & Fonts
# ============================
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self.outputs = []
        self.days = 0
        self.user_name = None
        self._get_name()

    def run(self):
        self.window.mainloop()

    # ============================
    # Display messages in chatbox
    # ============================
    def giveanswer(self, speaker, msg):
        self.text_widget.configure(state=NORMAL)
        if speaker.lower() == "bot":
            self.text_widget.insert(END, f"Bot : {msg}\n", "bot")
        else:
            self.text_widget.insert(END, f"{self.user_name} : {msg}\n", "user")
        self.text_widget.tag_config("bot", foreground="yellow")
        self.text_widget.tag_config("user", foreground="cyan")
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

    # ============================
    # Initial name input window
    # ============================
    def _get_name(self):
        self.window.title("Welcome to Health Care Chatbot")
        self.window.geometry("500x300")
        self.window.configure(bg=BG_COLOR)
        self.window.resizable(False, False)

        Label(self.window, text="Enter Your Name:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_BOLD).pack(pady=(50,10))

        self.name_entry = Entry(self.window, bg=BG_GRAY, fg="black", font=FONT_BOLD, width=30)
        self.name_entry.pack(pady=(0,10))
        self.name_entry.focus()
        self.name_entry.bind("<Return>", self.get_name_after_click)

        Button(self.window, text="Submit", bg="red", fg=TEXT_COLOR, font=FONT_BOLD,
               command=lambda: self.get_name_after_click(None)).pack(pady=(0,20))

    # ============================
    # Store name and open chat window
    # ============================
    def get_name_after_click(self, event):
        entered_name = self.name_entry.get().strip()
        if len(entered_name) >= 2:
            self.user_name = entered_name.split()[0]
            self._setup_main_window()
            self.coming_msg()
        else:
            self.msg_warning("Name Error", "Please enter at least two words of a name.")

    # ============================
    # Setup main chat window with search
    # ============================
    def _setup_main_window(self):
        self.window.geometry("1200x640")
        self.window.configure(bg=BG_COLOR)

        # Left side: search similar diseases
        leftside_label = Frame(self.window, bg=BG_COLOR)
        leftside_label.place(relx=0, rely=0, relwidth=0.25, relheight=1)

        Label(leftside_label, text="Search Diseases:", bg="red", fg=TEXT_COLOR, font=FONT_BOLD).pack(pady=(10,5))

        self.help_entry = Entry(leftside_label, bg=BG_GRAY, fg="black", font=FONT_BOLD)
        self.help_entry.pack(padx=10, pady=5, fill=X)
        self.help_entry.bind("<Return>", self._on_enter_help_search)

        Button(leftside_label, text="Search", bg=BG_GRAY, font=FONT_BOLD, command=lambda: self._on_enter_help_search(None)).pack(padx=10, pady=5, fill=X)

        self.search_box = Text(leftside_label, bg="#00003d", fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.search_box.pack(padx=5, pady=10, fill=BOTH, expand=True)
        self.search_box.configure(state=DISABLED)

        scrollbar = Scrollbar(self.search_box)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.configure(command=self.search_box.yview)
        self.search_box.configure(yscrollcommand=scrollbar.set)

        # Right side chat
        rightside_label = Frame(self.window, bg=BG_COLOR)
        rightside_label.place(relx=0.25, rely=0, relwidth=0.75, relheight=1)

        self.text_widget = Text(rightside_label, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.pack(fill=BOTH, expand=True)
        self.text_widget.configure(state=DISABLED)

        bottom_frame = Frame(rightside_label, bg=BG_COLOR)
        bottom_frame.pack(fill=X)

        self.msg_entry = Entry(bottom_frame, bg=BG_GRAY, fg="black", font=FONT)
        self.msg_entry.pack(side=LEFT, fill=X, expand=True, padx=(5,0), pady=5)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        Button(bottom_frame, text="Send", bg=BG_GRAY, font=FONT_BOLD,
               command=lambda: self._on_enter_pressed(None)).pack(side=RIGHT, padx=5, pady=5)

    # ============================
    # Handle search diseases
    # ============================
    def _on_enter_help_search(self, event):
        dis_list = ['itching', 'skin rash', 'joint pain', 'vomiting', 'fatigue', 'headache', 'cough', 'high fever']
        # You can expand the dis_list with all feature_names from bot.py

        inp = self.help_entry.get().strip().lower()
        self.help_entry.delete(0, END)
        pred_list = []

        if inp:
            regexp = re.compile(inp)
            for item in dis_list:
                if regexp.search(item.lower()):
                    pred_list.append(item)

        self.search_box.configure(state=NORMAL)
        self.search_box.delete(1.0, END)

        if pred_list:
            for i, val in enumerate(pred_list, start=1):
                self.search_box.insert(END, f"{i}) {val}\n")
        else:
            self.search_box.insert(END, "No Disease Match Found.")

        self.search_box.configure(state=DISABLED)

    # ============================
    # Send message & get response
    # ============================
    def _on_enter_pressed(self, event):
        user_input = self.msg_entry.get().strip()
        if not user_input:
            self.msg_warning("Input Error", "Please enter some text.")
            return

        self.giveanswer("user", user_input)
        self.msg_entry.delete(0, END)

        if user_input.lower() not in self.outputs:
            self.outputs.append(user_input.lower())

        pr_val = get_pridected_value(user_input, self.outputs)
        if pr_val:
            self.giveanswer("bot", f"Predicted Disease: {pr_val}")
            precautions = get_diesese_practions(pr_val)
            self.giveanswer("bot", f"Disease Precautions: {precautions}")
        else:
            self.giveanswer("bot", "Please tell me your primary symptoms first.")

    # ============================
    # First bot greeting
    # ============================
    def coming_msg(self):
        self.giveanswer("bot", f"Hello {self.user_name}! Please tell me your primary symptoms one by one.")

    # ============================
    # Warning dialogs
    # ============================
    def msg_warning(self, title, msg):
        tkinter.messagebox.showwarning(title, msg)

# ============================
# Run the application
# ============================
if __name__ == "__main__":
    app = ChatApplication()
    app.run()
