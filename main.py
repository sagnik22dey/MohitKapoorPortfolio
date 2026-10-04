from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

app = FastAPI(
    title="Mohit Kapoor | Author & Global Executive Portfolio",
    description="Showcase portfolio for author and enterprise leader Mohit Kapoor",
    version="1.0.0"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")
templates_dir = os.path.join(BASE_DIR, "templates")

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

class ContactForm(BaseModel):
    name: str
    email: str
    subject: str = ""
    message: str

AUTHOR_DATA = {
    "name": "Mohit Kapoor",
    "role": "Author, Thinker & Global Conference Producer",
    "company": "Innovative Concepts",
    "company_role": "Founder & Director",
    "experience_years": "18+",
    "book": {
        "title": "The Hidden Lens",
        "subtitle": "Understanding Unconscious Bias",
        "isbn": "978-81-989341-7-8",
        "cover_image": "/static/images/the-hidden-lens-cover.png",
        "back_image": "/static/images/the-hidden-lens-back.png",
        "chapters_count": 9,
        "description": "The Hidden Lens explores the covert mechanisms of unconscious bias that steer everyday decisions, strategic judgments, and interpersonal dynamics. Mohit Kapoor dissects cognitive patterns into nine structured, accessible chapters, equipping professionals, corporate boards, and individuals with pragmatic tools to foster psychological safety, objective evaluation, and genuinely inclusive leadership.",
        "key_takeaways": [
            "Deconstructing cognitive blind spots in leadership and executive hiring",
            "The neural architecture of instinctual judgment versus conscious deliberation",
            "Strategic interventions to eliminate bias in high-stakes B2B negotiations",
            "Cultivating inclusive team cultures across global, multicultural organizations"
        ]
    },
    "bio_summary": "Mohit Kapoor is an avid thinker, writer, and global enterprise director. With over 18 years producing premier international B2B energy and maritime conferences across India, the Middle East, Southeast Asia, and North Africa, he bridges deep industrial acumen with human-centric organizational psychology.",
    "company_overview": "Innovative Concepts is a premier conference and exhibition producer with 18+ years of legacy, curating high-impact international forums including the Offshore Jack Up Middle East (OJME), India Drilling & Exploration Conference (IDEC), and Asset Integrity Management Conference (AIMC).",
    "linkedin_profile": "https://www.linkedin.com/in/mohit-kapoor-389301a",
    "company_linkedin": "https://www.linkedin.com/company/innovativeconcepts/",
    "company_website": "https://www.innoconcepts.co.in/",
    "locations": "Mumbai, India | Dubai, UAE | Singapore | Doha, Qatar"
}

@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    """
    Renders the flagship 3D curving ribbon luminary portfolio (Design 1).
    """
    return templates.TemplateResponse(
        "index1.html",
        {"request": request, "author": AUTHOR_DATA, "active_design": 1}
    )

@app.get("/design-1", response_class=HTMLResponse)
async def serve_design_one(request: Request):
    """
    Dedicated route for Design 1 (Curving 3D Ribbon & Glass Luminary).
    """
    return templates.TemplateResponse(
        "index1.html",
        {"request": request, "author": AUTHOR_DATA, "active_design": 1}
    )

@app.get("/design-2", response_class=HTMLResponse)
async def serve_design_two(request: Request):
    """
    Dedicated route for Design 2 (Architectural 3D Curving Studio & Carousel).
    """
    return templates.TemplateResponse(
        "index2.html",
        {"request": request, "author": AUTHOR_DATA, "active_design": 2}
    )

@app.get("/api/author")
async def get_author_profile():
    """
    Returns structured biographical and literary metadata for Mohit Kapoor.
    """
    return JSONResponse(content=AUTHOR_DATA)

@app.post("/api/contact")
async def handle_contact_message(payload: ContactForm):
    """
    Handles speaking invitations, book inquiry, and consulting queries.
    """
    return JSONResponse(
        content={
            "status": "success",
            "message": f"Thank you, {payload.name}. Your inquiry regarding '{payload.subject or 'General Inquiry'}' has been received."
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
