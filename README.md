# Wiki Word Finder (BETA)

The Wiki Word Finder is a Python project that navigates through Wikipedia to find a connection between two words. It starts by fetching the Wikipedia page of an initial word and scans for links related to a target word, traversing from page to page until the target word is found.

## Disclaimer

This project is currently in BETA and requires further improvements and bug fixes. It is intended for educational purposes and demonstrates the capabilities of web scraping and interaction with the ChatGPT API.

## Features

- **Dynamic Wiki Navigation:** Starts with a user-provided word and dynamically navigates through Wikipedia to find a connection to another user-provided target word.
- **Link Analysis:** Analyzes links on each Wikipedia page to determine their relevance to the target word, using language processing through the ChatGPT API.
- **Iterative Search:** Continues to traverse through the most relevant links until the target word is reached or no further relevant links are found.

## Requirements

- Python 3.x
- Libraries: `requests`, `bs4`, `openai`
- OpenAI API key

## Installation

1. **Install Python:**
   - Ensure Python 3.x is installed on your system. Download from [python.org](https://www.python.org/).

2. **Install Dependencies:**
   - Install the required libraries using pip:
     ```bash
     pip install requests beautifulsoup4 openai
     ```

3. **Set Up OpenAI API Key:**
   - Configure your OpenAI API key in the script by replacing `'API-KEY'` with your actual API key.

## Usage Instructions

1. **Start the Script:**
   - Run the script via command line:
     ```bash
     python wiki_word_finder.py
     ```

2. **Input Words:**
   - When prompted, enter the initial and target words to start the search process.

3. **Observe Output:**
   - The script will output the navigation process, showing each step taken from one Wikipedia link to another until the target word is found or the search ends.
