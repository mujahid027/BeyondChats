"""
Citation Identification Tool using SpaCy

This script fetches data from an API, identifies citations within response texts
based on similarity to source contexts using SpaCy, and returns a list of cited source IDs.

Requires:
- SpaCy (en_core_web_sm model)
- requests
"""

from utils import fetch_data_from_api, identify_citations

# Replace with your actual API URL
api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"

def main():
  """
  Fetches data, identifies citations, and prints the results.
  """
  citations = get_citations(api_url)

  if citations:
    print("Citations found:")
    for item in citations:
      print(f"- Message ID: {item[0]}")
      print(f"  Citation Source IDs: {item[1:]}")
  else:
    print("No citations found.")

if __name__ == "__main__":
  main()
