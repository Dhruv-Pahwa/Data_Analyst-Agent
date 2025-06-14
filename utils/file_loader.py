import pandas as pd
import docx
import fitz  # PyMuPDF
from PIL import Image
import pytesseract

def load_file(file_path):
    ext = file_path.split(".")[-1].lower()

    try:
        if ext == "csv":
            return pd.read_csv(file_path)
        elif ext == "xlsx":
            return pd.read_excel(file_path)
        elif ext == "txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        elif ext == "pdf":
            doc = fitz.open(file_path)
            text = ""
            for page in doc:
                text += page.get_text()
            return text
        elif ext == "docx":
            doc = docx.Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs])
        elif ext in ["jpg", "jpeg", "png"]:
            img = Image.open(file_path)
            return pytesseract.image_to_string(img)
        else:
            return None
    except Exception as e:
        return f"❌ Failed to load file: {str(e)}"
