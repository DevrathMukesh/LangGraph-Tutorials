# LangGraph-Tutorials 🚀

This repository contains LangGraph workflow examples using both OpenAI and Google Gemini (Generative AI). It includes everything from basic prompt chaining to an advanced chatbot with a Streamlit interface.

---

## 📁 Step 1: Create `.env` File

Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

---

## 🐍 Step 2: Set Up Conda Environment

```bash
conda create --name LangGraph-Tutorials python=3.13
conda activate LangGraph-Tutorials
```

---

## 📦 Step 3: Install Dependencies

```bash
pip install langgraph langchain langchain_openai python-dotenv streamlit
```

If you're using **Google Gemini**:

```bash
pip install google-generativeai
```

---

## 💬 Step 4: Run the Streamlit Chatbot App

```bash
cd Workflows/06_AdvancedChatbot/app
streamlit run streamlit_frontend.py
```

---

## 🌴 Folder Structure

```
.
├── README.md
└── Workflows
    ├── 01_PromptChaining
    │   └── main.ipynb
    ├── 02_Sequential_Workflows
    │   ├── BMICalculator
    │   │   └── main.ipynb
    │   └── SimpleLLM
    │       └── main.ipynb
    ├── 03_Parallel_Workflow
    │   ├── BatsmanPerformance
    │   │   └── main.ipynb
    │   └── UPSCEssay
    │       ├── gemini.ipynb
    │       └── openai.ipynb
    ├── 04_Conditional_Workflows
    │   ├── LLM_Based_Gemini.ipynb
    │   ├── LLM_Based_OpenAI.ipynb
    │   └── Quadratic_Equation.ipynb
    ├── 05_Iteratice_Workflows
    │   ├── X_Post_Generator_Gemini.ipynb
    │   └── X_Post_Generator_OpenAI.ipynb
    ├── 06_AdvancedChatbot
    │   ├── app
    │   │   ├── langgraph_backend.py
    │   │   └── streamlit_frontend.py
    │   ├── X_Post_Generator_Gemini.ipynb
    │   └── X_Post_Generator_OpenAI.ipynb
    └── 07_Persistance
        ├── Persistence_Gemini.ipynb
        └── Persistence_OpenAI.ipynb
```

---

## 🧠 Tips

- Use `.env` to securely manage API keys
- Follow LangGraph documentation to create custom workflows
- Easily switch between OpenAI and Gemini models in your code

---

Happy Building! ⚙️
