"""
Welcome to the world of e-commerce, where customer feedback is a goldmine of
insights! In this project, you'll dive into the Women's Clothing E-Commerce
Reviews dataset, focusing on the 'Review Text' column filled with direct
customer opinions.

Your mission is to use text embeddings and Python to analyze these reviews,
uncover underlying themes, and understand customer sentiments. This analysis
will help improve customer service and product offerings.

## The Data

You will be working with a dataset specifically focusing on customer reviews.
Below is the data dictionary for the relevant field:

## womens_clothing_e-commerce_reviews.csv

| Column          | Description                                        |
|-----------------|----------------------------------------------------|
| `'Review Text'` | Textual feedback provided by customers about their
|                 | shopping experience and product quality.           |

Armed with access to powerful embedding API services, you will process the
reviews, extract meaningful insights, and present your findings.
"""

# Import the necessary libraries
import pandas as pd
from openai import OpenAI

# Run this cell to install ChromaDB if desired
try:
    assert version('chromadb') == '0.4.17'
except:
    !pip install chromadb==0.4.17
try:
    assert version('pysqlite3') == '0.5.2'
except:
    !pip install pysqlite3-binary==0.5.2
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb