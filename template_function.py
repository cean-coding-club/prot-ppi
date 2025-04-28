#!/usr/bin/env python

## Author: 
## Date: 

## Run this function as:
## python template_function.py

def analyze_protein_sequence(protein_name: str = "Unknown", seq: str) -> Dict[str, float]:
    """
    Add here your description of the function

    Args:
        seq (str): Protein sequence (amino acid string).

    Returns:
        Dict[str, float]: Dictionary with basic features.
    """
    # ADD HERE YOUR CODE
    # code for length - code here
    return {
        "Protein Name": protein_name,
        "Length": length
    }

def main():
    """
    Main function for testing the protein sequence analysis.
    """
    # Example sequence
    test_seq = "MKWVTFISLLFLFSSAYSRGVFRRDTHKSEIAHRFKDLGE"
    test_name = "Serum_Albumin_Human"
    
    # Run the analysis
    results = analyze_protein_sequence(test_name, test_seq)
    
    # Print results nicely
    print("Protein Sequence Analysis Results:")
    for key in ["Protein Name", "Length"]:
        print(f"{key}: {results[key]}")
        
if __name__ == "__main__":
    main()
