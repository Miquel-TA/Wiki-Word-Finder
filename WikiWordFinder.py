from openai import OpenAI
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Configure your OpenAI API key
client = OpenAI(api_key='API-KEY')

def search_wikipedia(page_title):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Search Wikipedia for the page titled '{page_title}' and provide the first link.",
                }
            ],
            model="gpt-3.5-turbo",
        )
        for message in response.choices[0].text.split():
            print(message)
            if "https://en.wikipedia.org/wiki/" in message:
                return message
    except Exception as e:
        print(f"Error during Wikipedia search: {e}")
        return None

def fetch_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_links(soup, base_url):
    links = []
    for link in soup.find_all('a', href=True):
        href = link.get('href', '')
        if href.startswith('/wiki/') and ':' not in href:
            full_url = urljoin(base_url, href)
            links.append(full_url)
    return links

def evaluate_similarity(phrase, target):
    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=f"Rate the similarity between the phrases: '{phrase}' and '{target}'",
            max_tokens=50
        )
        return float(response.choices[0].text)
    except Exception as e:
        print(f"Error during similarity evaluation: {e}")
        return 0.0

def main():
    initial_word = input("Enter the initial word: ")
    target_word = input("Enter the target word: ")
    
    start_url = search_wikipedia(initial_word)
    if not start_url:
        print("Failed to find a Wikipedia page for the initial word.")
        return
    
    current_url = start_url
    visited_urls = set()

    while current_url not in visited_urls:
        visited_urls.add(current_url)
        print(f"Searching in: {current_url}")

        soup = fetch_article(current_url)
        links = extract_links(soup, current_url)
        
        best_score = 0
        best_link = None

        for link in links:
            if link not in visited_urls:
                similarity = evaluate_similarity(link, target_word)
                if similarity > best_score:
                    best_score = similarity
                    best_link = link

        if best_score > 0.8:  # Assume similarity is good enough if score > 0.8
            print(f"High similarity found: {best_link} with score {best_score}")
            break
        elif best_link:
            print(f"Following link: {best_link} with best score {best_score}")
            current_url = best_link
        else:
            print("No relevant links found or all links visited.")
            break

# Run the main function
if __name__ == "__main__":
    main()
