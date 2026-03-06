# tools/lab_value_parser.py

def parse_lab_values(extracted_values):
    """
    Converts extracted lab values into structured dictionary with units, ranges, and status.
    
    Parameters:
        extracted_values (dict): Lab values extracted from PDF as strings.
        
    Returns:
        dict: Structured lab results with value, unit, range, and status.
    """
    # Define reference ranges and units for your lab tests
    reference_data = {
        "Hemoglobin": {"unit": "g/dL", "range": (13.0, 17.0)},
        "WBC": {"unit": "cumm", "range": (4000, 11000)},
        "RBC": {"unit": "mill/cumm", "range": (4.5, 5.5)},
        "Platelet": {"unit": "cumm", "range": (150000, 410000)},
        "PCV": {"unit": "%", "range": (40, 50)},
        "MCV": {"unit": "fL", "range": (83, 101)},
        "MCH": {"unit": "pg", "range": (27, 32)},
    }
    
    structured_results = {}
    
    for test, value in extracted_values.items():
        try:
            val = float(value)
            ref = reference_data.get(test)
            if ref:
                low, high = ref["range"]
                status = "Normal"
                if val < low:
                    status = "Low"
                elif val > high:
                    status = "High"
                structured_results[test] = {
                    "value": val,
                    "unit": ref["unit"],
                    "range": f"{low}-{high}",
                    "status": status
                }
        except ValueError:
            # skip if conversion fails
            continue
    
    return structured_results

# Example usage
if __name__ == "__main__":
    sample_values = {'Hemoglobin': '12.5', 'WBC': '9000', 'RBC': '5.2', 
                     'Platelet': '150000', 'PCV': '57.5', 'MCV': '87.75', 'MCH': '27.2'}
    
    structured = parse_lab_values(sample_values)
    print("Structured Lab Results:")
    print(structured)