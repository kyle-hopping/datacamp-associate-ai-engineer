"""
Medical professionals often summarize patient encounters in transcripts written
in natural language, which include details about symptoms, diagnosis, and
treatments. These transcripts can be used for other medical documentation, such
as for insurance purposes, but as they are densely packed with medical
information, extracting the key data accurately can be challenging.  

You and your team at Lakeside Healthcare Network have decided to leverage the
OpenAI API to automatically extract medical information from these transcripts
and automate the matching with the appropriate ICD-10 codes. ICD-10 codes are a
standardized system used worldwide for diagnosing and billing purposes, such as
insurance claims processing.

## The Data
The dataset contains anonymized medical transcriptions categorized by specialty.

## transcriptions.csv
| Column                | Description                                        |
|-----------------------|----------------------------------------------------|
| `"medical_specialty"` | The medical specialty associated with each         |
|                       | transcription.                                     |
| `"transcription"`     | Detailed medical transcription texts, with         |
|                       | insights into the medical case.                    |
"""

# Import the necessary libraries
import pandas as pd
from openai import OpenAI
import json

# Load the data
df = pd.read_csv("data/transcriptions.csv")
df.head()

# Initialize the OpenAI client
client = OpenAI()

def extract_info_with_openai(transcription):
    messages = [
        {
            "role": "system",
            "content": """Act as a healthcare professional extracting patient
                       data. Always return both the age and recommended treatment,
                       and if the information is missing, still create the field
                       and specify 'Unknown'.""",
            "role": "user",
            "content": f"""Eextract and return both the patient's age and
                       recommended treatment from the following transcription.
                       Transcription: {transcription}."""
        }]

    function_definition = [
        {
            'type': 'function',
            'function': {
                'name': 'extract_medical_data',
                'description': '''Get the age and recommended treatment from the
                               input text. Return both age and recommended treatment.''',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'Age': {
                            'type': 'integer',
                            'description': 'Age of the patient'
                        },
                        'Recommended Treatment/Procedure': {
                            'type': 'string',
                            'description': '''Recommended the treatment or
                                           procedure for the patient'''
                        }
                    }
                }
            }
        }]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=function_definition
    )
    return json.loads(response.choices[0].message.tool_calls[0].function.arguments)

def get_icd_codes(treatment):
    if treatment != 'Unknown':
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""Provide the ICD codes for the following treatment
                           or procedure: {treatment}. Return the answer as a
                           list of codes. Only include the codes and no
                           other information."""
            }],
            temperature=0.5
        )
        output = response.choices[0].message.content
    else:
        output = 'Unknown'
    return output

# Processed data storage
processed_data = []

# Process each row
for index, row in df.iterrows():
    medical_specialty = row['medical_specialty']
    extracted_data = extract_info_with_openai(row['transcription'])
    
    if 'Recommended Treatment/Procedure' in extracted_data.keys():
        icd_code = get_icd_codes(extracted_data["Recommended Treatment/Procedure"])
    else:
        icd_code = 'Unknown'

    extracted_data["Medical Specialty"] = medical_specialty
    extracted_data["ICD Code"] = icd_code
    processed_data.append(extracted_data)

# Convert the list to a DataFrame
df_structured = pd.DataFrame(processed_data)