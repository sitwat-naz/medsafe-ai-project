from tools.entity_extractor import extract_lab_values_from_pdf
from tools.lab_value_parser import parse_lab_values

def main():
    file_path = input("Enter PDF file path (default: data/blood_report.pdf): ") or "data/blood_report.pdf"
    
    # Extract raw lab values
    lab_values = extract_lab_values_from_pdf(file_path)
    print("\nRaw Lab Values:", lab_values)
    
    # Convert to structured results
    structured_results = parse_lab_values(lab_values)
    print("\nStructured Lab Results:")
    for test, details in structured_results.items():
        print(f"{test}: {details['value']} {details['unit']} (Normal Range: {details['range']}) - {details['status']}")

if __name__ == "__main__":
    main()