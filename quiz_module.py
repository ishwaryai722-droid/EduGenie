import os

from google import genai


def _call_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return (
            "Gemini API key is not configured. Add GEMINI_API_KEY to your .env file "
            "to enable live AI responses."
        )

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return getattr(response, "text", str(response))
    except Exception as exc:
        return f"Gemini request failed: {exc}"


def generate_quiz(topic: str) -> str:
    if not topic or not topic.strip():
        return "Please enter a topic to generate a quiz."

    prompt = (
        f"Create a short quiz on the topic '{topic.strip()}'. Include 5 multiple-choice questions "
        f"with 4 options each, mark the correct answer, and provide a brief answer key."
    )
    return _call_gemini(prompt)
