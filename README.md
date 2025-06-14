# 📰 News Fetcher using NewsAPI

A simple Python script to fetch the latest news articles on any topic of your interest using the [NewsAPI](https://newsapi.org/). This tool allows users to input a search keyword, fetches the most recent articles, and displays their titles along with direct links.

---

## 📌 Features

- Fetches real-time news articles using **NewsAPI**.
- Accepts user-defined search queries.
- Outputs article titles and clickable URLs.
- Displays articles in reverse chronological order (latest first).

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have the following installed:

- Python 3.x
- `requests` library  
  Install via pip:

```bash
pip install requests
```

## 🔑 Get NewsAPI Key

1. Visit NewsAPI.org.

2. Sign up and generate your free API key.

3. Replace the API key in the code:

```bash
api_key = "YOUR_API_KEY"
```

---

## 🧠 How It Works

1. The user inputs a topic (e.g., "AI", "Space", "Climate").

2. The script sends a GET request to NewsAPI using that query.

3. It parses the JSON response and prints the article titles and URLs.

---

## 💡 Example

```bash
What type of news are you looking for? climate
```

Output:

```arduino
1 Climate change threatens coral reefs - https://example.com/article1

--------------------------------------------------

2 UN Summit highlights urgent climate action - https://example.com/article2

--------------------------------------------------
```

---

## ⚠️ Notes

- The free NewsAPI plan has request limits (usually 100 requests/day).
- Ensure your system has internet access to run this script.

---

## 🙌 Acknowledgements

- NewsAPI.org — for providing a simple and powerful news access API.

---
