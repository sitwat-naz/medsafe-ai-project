import re
from tools.pdf_reader import extract_text_from_pdf

def extract_entities(text):
    labs = ['Hemoglobin', 'WBC', 'RBC', 'Platelet', 'PCV', 'MCV', 'MCH']
    entities = {}
    for lab in labs:
        pattern = rf"{lab}.*?(\d+\.?\d*)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            entities[lab] = match.group(1)
    return entities

# ✅ New helper function to call directly with PDF file
def extract_lab_values_from_pdf(file_path):
    text = extract_text_from_pdf(file_path)
    return extract_entities(text)

if __name__ == "__main__":
    file_path = "data/blood_report.pdf"
    entities = extract_lab_values_from_pdf(file_path)
    print("Extracted Lab Values:", entities)