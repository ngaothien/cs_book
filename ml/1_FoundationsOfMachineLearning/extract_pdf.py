import sys
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Extracted {len(reader.pages)} pages to {output_path}")

if __name__ == "__main__":
    extract_text_from_pdf(sys.argv[1], sys.argv[2])
