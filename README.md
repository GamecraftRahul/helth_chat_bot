# 🩺 Health Care Chatbot

A simple **AI-powered Health Care Chatbot** built with **Python**, **Tkinter**, and **spaCy**. This desktop application allows users to describe their symptoms in natural language, identifies possible symptoms using NLP, and provides basic health precautions through an interactive chat interface.

> **Note:** This project is for educational purposes only and is **not a replacement for professional medical advice**.

---

## 📖 Overview

The Health Care Chatbot demonstrates the use of **Natural Language Processing (NLP)** in healthcare applications. Users can interact with the chatbot through a graphical interface, enter symptoms, and receive possible symptom identification along with general precautions.

The application combines:

- 🧠 Natural Language Processing (spaCy)
- 💬 Interactive chatbot interface
- 🖥️ Desktop GUI using Tkinter
- ❤️ Basic healthcare guidance

---

## ✨ Features

- 👤 User name registration before chat
- 💬 Interactive chatbot conversation
- 🧠 Symptom detection using NLP
- 🔍 Disease/Symptom search panel
- 📋 Basic health precautions
- 🎨 Clean and responsive Tkinter interface
- ⚡ Fast local execution
- 🖥️ Lightweight desktop application

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Tkinter | Desktop GUI |
| spaCy | Natural Language Processing |
| Regular Expressions | Input Validation |

---

## 📂 Project Structure

```text
helth_chat_bot-main/
│
├── app.py          # Main GUI Application
├── bot.py          # Chatbot logic & NLP processing
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/helth_chat_bot.git
```

### 2. Navigate to the Project

```bash
cd helth_chat_bot-main
```

### 3. Install Dependencies

```bash
pip install spacy
```

### 4. Download the spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

### 5. Run the Application

```bash
python app.py
```

---

## 🚀 How It Works

1. Launch the application.
2. Enter your name.
3. Start chatting with the chatbot.
4. Describe your symptoms naturally.
5. The chatbot identifies matching symptoms using NLP.
6. General precautions are displayed based on detected symptoms.
7. Use the search panel to look up diseases or symptoms.

---

## 🧠 NLP Workflow

```text
User Input
      │
      ▼
Tokenization & Lemmatization
      │
      ▼
Symptom Matching
      │
      ▼
Detected Symptoms
      │
      ▼
Health Suggestions
      │
      ▼
General Precautions
```

---

## 📸 Application Features

- Welcome screen
- User name registration
- Interactive chatbot
- Chat history
- Symptom detection
- Disease search panel
- Basic health precautions

---

## 💡 Example Conversation

```text
You:
I have headache and cough.

Bot:
Based on your symptoms, you might be experiencing:
Headache

Bot:
Precautions:
1. Take proper rest
2. Drink plenty of water
3. Eat healthy food
4. Avoid stress
5. Consult a doctor if symptoms persist
```

---

## 📦 Dependencies

- Python 3.8+
- Tkinter
- spaCy
- en_core_web_sm

Install everything:

```bash
pip install spacy

python -m spacy download en_core_web_sm
```

---

## ⚠️ Disclaimer

This chatbot:

- Does **not** diagnose diseases.
- Provides only educational guidance.
- Should **not** replace medical professionals.
- Always consult a qualified healthcare provider for medical concerns.

---

## 🔮 Future Improvements

- Machine Learning disease prediction
- Larger medical dataset
- Multiple language support
- Voice input
- Voice output
- Medical history tracking
- Doctor appointment integration
- Cloud database support
- User authentication
- Dark/Light themes

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Rahul Kulkarni**

GitHub: https://github.com/GamecraftRahul

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

## 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project for educational purposes.
