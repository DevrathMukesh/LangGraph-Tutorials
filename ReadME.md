<!-- 📁 Step 1: Create .env File -->
GEMINI_API_KEY=your_actual_api_key_here

<!-- 🐍 Step 2: Create a New Conda Environment -->
conda create --name LangGraph-Tutorials python=3.13
conda activate LangGraph-Tutorials

<!-- 📦 Step 3: Install Required Libraries -->
pip install langgraph langchain langchain_openai python-dotenv streamlit

<!-- If you're using Gemini (Google Generative AI), also install: -->
pip install google-generativeai

<!-- 💬 Step 4: Run the Streamlit Chatbot App -->
cd Workflows/06_AdvancedChatbot/app
streamlit run streamlit_frontend.py



<!-- 🌴: File Tree Overview -->
.
├── ReadME.md
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
    │   │   ├── __pycache__
    │   │   │   └── langgraph_backend.cpython-313.pyc
    │   │   ├── langgraph_backend.py
    │   │   └── streamlit_frontend.py
    │   ├── X_Post_Generator_Gemini.ipynb
    │   └── X_Post_Generator_OpenAI.ipynb
    └── 07_Persistance
        ├── Persistence_Gemini.ipynb
        └── Persistence_OpenAI.ipynb

15 directories, 19 files