# 📌 Python Reddit Reel Generator  

## 🚀 Overview  
The **Python Reddit Reel Generator** is a Python-based script that automates the creation of short video reels. It fetches the top posts from user-specified subreddits, converts the content into a voiceover, and synchronizes it with text to produce a shareable MP4 video reel.  

## 🛠 Tech Stack  
- **Python**  
- **PRAW** (Python Reddit API Wrapper) - Fetch Reddit data  
- **Selenium** - Automate browser interactions  
- **MoviePy** - Generate and edit video  
- **AssemblyAI** - Text-to-speech API  

## ✨ Features  
- Fetches top Reddit posts based on user-defined subreddits  
- Converts post content into natural voiceovers  
- Creates synchronized video reels with text and audio  
- Outputs ready-to-share MP4 videos  

## ⚙️ Installation  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/python-reddit-reel-generator.git
   cd python-reddit-reel-generator

2. **Update Reddit API Credentials**  
   Open `main.py` and replace the placeholders with your Reddit API credentials:  
   ```python
   client_id = "bot_clientid"
   client_secret = "bot_clientSecret"
   password = "reddit_pass"
   user_agent = "bot_name"
   username = "reddit_username"

2. **Update AssemblyAI API Key**  
   Open `saveVideofunc.py` and replace the placeholders with your Reddit API credentials:  
   ```python
   aai.settings.api_key = "api key"
