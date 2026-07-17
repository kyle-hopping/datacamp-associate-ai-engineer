# datacamp-associate-ai-engineer

This repository contains my project work for DataCamp's **Associate AI Engineer for Developers** certification track.
 
## About the Track
 
The Associate AI Engineer for Developers track focuses on integrating AI into software applications using industry-standard tools and best practices. It covers:
 
- Using the **OpenAI API** to build AI-powered applications and leverage large language models (LLMs)
- Prompt engineering principles and best practices for working with LLMs
- Navigating and using pre-trained models and datasets from the **Hugging Face Hub**
- Building advanced AI applications such as semantic search and recommendation engines using embeddings
- Working with the **Pinecone** vector database for efficient similarity search
- Building LLM-powered applications using prompts, chains, and agents with **LangChain**
- Software engineering best practices for AI applications, including modularity, documentation, and automated testing

## Tools & Technologies
 
- Python
- OpenAI API
- Hugging Face
- LangChain
- Pinecone

## Status
 
✅ Complete — all projects for the track have been finished.

## Projects

### 1. [Paris Trip Planner](01-paris-trip-planner/paris_trip_planner.py)
An AI-powered travel guide chatbot for a fictional tourism company, Peterman Reality Tours. Uses the OpenAI Chat Completions API with a system prompt to answer common traveler questions about Paris landmarks in a running multi-turn conversation.

**Concepts:** system prompts, multi-turn conversation state, `gpt-4o-mini`

### 2. [Organize Medical Transcriptions](02-organize-med-transcriptions/organize_med_transcriptions.py)
Extracts structured patient data (age, recommended treatment) from unstructured medical transcription text using OpenAI function calling, then looks up matching ICD-10 codes for each treatment and compiles the results into a structured DataFrame.

**Concepts:** function calling / tool schemas, structured data extraction, `pandas`

### 3. [Topic Analysis on E-Commerce Reviews](03-topic-analysis/topic_analysis.py)
Analyzes women's clothing e-commerce reviews using OpenAI text embeddings. Reviews are embedded, visualized in 2D with t-SNE, categorized against predefined topics (Quality, Fit, Style, Comfort) by cosine similarity, and stored in a ChromaDB vector database for similarity search.

**Concepts:** text embeddings, dimensionality reduction (t-SNE), vector databases (ChromaDB), semantic similarity search
 
## Setup
 
1. Clone this repository
2. Install dependencies:
```
   pip install -r requirements.txt
```
3. Create a `.env` file in the root directory with your OpenAI API key:
```
   OPENAI_API_KEY=your_key_here
```

