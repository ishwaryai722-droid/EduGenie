from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path

load_dotenv()

app = FastAPI(
    title="EduGenie AI",
    description="AI Learning Assistant powered by Google Gemini"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "result": None,
            "selected_feature": None,
            "user_input": ""
        }
    )


@app.post("/process", response_class=HTMLResponse)
async def process(
    request: Request,
    feature: str = Form(...),
    user_input: str = Form(...)
):
    result = ""

    try:
        if feature == "explain":
            result = explain_topic(user_input)
        elif feature == "qa":
            result = answer_question(user_input)
        elif feature == "quiz":
            result = generate_quiz(user_input)
        elif feature == "summary":
            result = summarize_text(user_input)
        elif feature == "recommend":
            result = recommend_learning_path(user_input)
        else:
            result = "Please select a valid feature."
    except Exception as exc:
        result = f"Error: {str(exc)}"

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "result": result,
            "selected_feature": feature,
            "user_input": user_input
        }
    )


@app.get("/health")
async def health_check():
    return {
        "status": "running",
        "application": "EduGenie AI"
    }
