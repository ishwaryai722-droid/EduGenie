\# EduGenie AI – Smart Learning Assistant



EduGenie AI is an AI-powered learning assistant built using Python, FastAPI, and Google Gemini. It helps students understand topics, ask questions, generate quizzes, summarize study materials, and receive personalized learning path recommendations.



\## Features



\- \*\*Topic Explanation:\*\* Understand complex topics through AI-generated explanations.

\- \*\*Question \& Answer:\*\* Get answers to educational questions.

\- \*\*Quiz Generation:\*\* Generate quizzes to practice and test knowledge.

\- \*\*Text Summarization:\*\* Convert lengthy study materials into concise summaries.

\- \*\*Learning Path Recommendation:\*\* Get learning recommendations based on your interests and goals.



\## Technologies Used



\- Python

\- FastAPI

\- HTML

\- CSS

\- Jinja2

\- Google Gemini API

\- Uvicorn



\## Project Structure



```text

EduGenie/

│

├── main.py

├── qna.py

├── quiz\_module.py

├── summary\_module.py

├── explanation\_module.py

├── learning\_path.py

├── requirements.txt

├── .gitignore

│

├── static/

│   └── style.css

│

└── templates/

&#x20;   └── index.html

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/ishwaryai722-droid/EduGenie.git

cd EduGenie

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the virtual environment



Windows:



```bash

venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Configure Gemini API Key



Create a `.env` file in the project root folder.



Add:



```env

GEMINI\_API\_KEY=your\_gemini\_api\_key

```



Replace the placeholder with your own API key. Never upload your `.env` file to GitHub.



\### 6. Run the application



```bash

uvicorn main:app --reload

```



Open your browser and visit:



```text

http://127.0.0.1:8000

```



\## Health Check



Visit:



```text

http://127.0.0.1:8000/health

```



\## Future Enhancements



\- Student login and registration

\- Learning progress tracking

\- More interactive learning activities

\- Improved user experience



\## Author



\*\*Ishwarya\*\*



GitHub: https://github.com/ishwaryai722-droid



\---



\*EduGenie AI – Making Learning Smarter with Artificial Intelligence.\*

