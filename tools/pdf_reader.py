from pypdf import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        
    return text


if __name__ == "__main__":
    
    file_path = "data/blood_report.pdf"
    
    extracted_text = extract_text_from_pdf(file_path)
    
    print("\nExtracted Medical Report Text:\n")
    print(extracted_text)