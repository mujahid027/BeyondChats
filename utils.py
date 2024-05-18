"""
Utility functions for fetching data and identifying citations.
"""

import requests
import spacy

# Load the English language model for SpaCy
nlp = spacy.load("en_core_web_sm")


def fetch_data_from_api(api_url):
  """
  Fetches data from the provided API URL in a loop, handling errors.

  Args:
      api_url (str): The URL of the API endpoint.

  Returns:
      list: A list containing data from all fetched pages (potentially).
  """

  next_page_url = api_url
  data = []

  while next_page_url:
    response = requests.get(next_page_url)
    if response.status_code == 200:
      try:
        json_response = response.json()
      except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        break

      # Ensure the response is a dictionary
      if isinstance(json_response, dict):
        data.extend(json_response.get("data", []))
        next_page_url = json_response.get("next_page_url")
      else:
        print("Invalid JSON response. Expected a dictionary.")
        break
    else:
      print("Error fetching data. Status code:", response.status_code)
      break

  return data


def identify_citations(response_text, source_contexts):
  """
  Identifies citations in response text based on similarity to source contexts.

  Args:
      response_text (str): The text of the response message.
      source_contexts (List[Dict[str, str]]): A list of dictionaries containing source contexts (e.g., {"context": "source text", "id": 1}).

  Returns:
      List[int]: A list of IDs of the cited sources.
  """

  citations = []
  response_doc = nlp(response_text)

  for source in source_contexts:
    source_doc = nlp(source["context"])
    similarity = response_doc.similarity(source_doc)
    if similarity > 0.5:  # Adjust threshold as needed
      citations.append(source["id"])

  return citations
