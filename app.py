from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os
from classifier import email_classifier, extract_text_pdf
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/classify")
async def classify(
    text: str = Form(None),
    file: UploadFile = File(None)
):
    
    email_content = ""

    if text: 
        email_content = text

    elif file: 
        
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if file.filename.endswith('.pdf'):
            
            email_content = extract_text_pdf(file_path)
        
        elif file.filename.endswith('.txt'):

            with open(file_path, 'r', encoding="utf-8") as f:
                email_content = f.read()
    
    else:
        return JSONResponse(
            status_code=400,
            content={"erro": "Envie um texto ou arquivo"}
        )
    
    os.remove(file_path)
    
    res = email_classifier(email_content)

    if res.get("erro"):
        return JSONResponse(
            status_code=500,
            content=res
        )
    
    return res
