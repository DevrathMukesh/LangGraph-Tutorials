# LangGraph-Tutorials 🚀

This repository contains LangGraph workflow examples using both **OpenAI** and **Google Gemini (Generative AI)**. It includes everything from basic prompt chaining to an advanced chatbot with a Streamlit interface.

---

## 📁 Step 1: Create `.env` File

```env
OPENAI_API_KEY=your-openai-api-key
GEMINI_API_KEY=your-google-gemini-api-key
```

```python
from dotenv import load_dotenv
load_dotenv()
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
pip install langgraph langchain langchain_openai python-dotenv streamlit langchain-google-genai
```

If you're using **Google Gemini**:

```bash
pip install google-generativeai
```

☁️ **(Optional) Install Google Cloud SDK (for ADC)**  
Only required if you're using Gemini via Google Cloud Console instead of API Key:

```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud auth application-default login
```

---

## 🧠 Step 4: Sample Code for OpenAI & Gemini (LangChain + SDK)

### 🟦 OpenAI Example (LangChain)

```python
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))
print(llm.invoke("Tell me a joke.").content)
```

### 🟨 Google Gemini Example (LangChain)

```python
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
print(llm.invoke("Define AI in one line.").content)
```

### 🟨 Google Gemini Example (Native SDK)

```python
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Define AI in one line.")
print(response.text)
```

---

## 💬 Step 5: Run the Streamlit Chatbot App

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
- Easily switch between OpenAI and Gemini in your code
- Follow LangGraph docs to build custom multi-step workflows

---

Happy Building! ⚙️✨
