# LegalEase – AI Legal Document Generator
Streamlit frontend + FastAPI backend + Gemini. Exports .txt, .docx, .pdf with logo, terms table and footer.

## Run
```bash
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                  # add GEMINI_API_KEY
uvicorn legalEaseAPI.main:app --reload                # terminal 1  (http://127.0.0.1:8000)
streamlit run frontend/app.py                         # terminal 2  (http://localhost:8501)
```
(`./run.sh` starts both.) Replace `Image/Logo.png` / `Image/inverseLogo.png` with your branding.

## Structure
`ai_core/gemini_generator.py` (Gemini) · `ai_core/generator.py` (sanitize/docx/pdf/html) ·
`legalEaseAPI/main.py, routes.py` (POST /generate) · `frontend/app.py` · `config.py`

_Drafts are not legal advice; have a lawyer review them._
