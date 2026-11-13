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


def summarize_text(text: str) -> str:
    if not text or not text.strip():
        return "Please enter text to summarize."

    prompt = (
        f"Summarize the following text concisely while preserving the key points and main ideas. "
        f"Use bullet points if helpful.\n\n{text.strip()}"
    )
    return _call_gemini(prompt)
