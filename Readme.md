# Twitter Trends Scraper

A web application that automatically scrapes trending topics from Twitter/X using Selenium and stores them in MongoDB.

## Demo Video



https://github.com/user-attachments/assets/f84bc2c6-110c-4c78-a7fe-2ea188927368



Short demo showcasing the Twitter Trends Scraper in action using Selenium WebDriver

## Features

- Automated login to Twitter
- Scrapes top 5 trending topics
- MongoDB integration for data storage
- Web interface to view results
- Proxy support
- Detailed logging and error handling

## Prerequisites

- Python 3.8+
- Google Chrome browser
- ChromeDriver matching your Chrome version
- MongoDB (local or Atlas)
- Twitter/X account

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd twitter-trends-scraper
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download ChromeDriver:
   - Go to [Chrome for Testing Downloads](https://googlechromelabs.github.io/chrome-for-testing/)
   - Download the version matching your Chrome browser
   - Extract `chromedriver.exe` to the project root directory

5. Create `.env` file in the root directory:
```env
# MongoDB Configuration
MONGO_URI=your_mongodb_uri
DB_NAME=your_database_name

# Twitter Credentials
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password

# ProxyMesh Configuration (Optional)
PROXYMESH_USERNAME=your_proxymesh_username
PROXYMESH_PASSWORD=your_proxymesh_password
PROXYMESH_HOST=your_proxymesh_host
```

## Project Structure

```
twitter-trends-scraper/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── scraper/
│   │   ├── __init__.py
│   │   └── selenium_scraper.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── styles.css
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── chromedriver.exe
```

## Usage

1. Start the application:
```bash
python src/app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Click the "Run Script" button to start scraping

## Features Details

### Web Interface
- Simple and intuitive interface
- Real-time status updates
- Display of trending topics
- MongoDB record preview

### Scraping Engine
- Automated Chrome browser control
- Multiple selector strategies
- Fallback mechanisms
- Robust error handling
- Configurable timeouts

### Data Storage
- MongoDB integration
- Timestamp tracking
- IP address logging
- Unique ID for each scraping session

## Troubleshooting

1. ChromeDriver Issues:
   - Ensure Chrome browser is installed
   - Match ChromeDriver version with Chrome version
   - Place chromedriver.exe in project root

2. MongoDB Connection:
   - Check MongoDB service is running
   - Verify connection string in .env
   - Ensure network connectivity

3. Twitter Login:
   - Verify credentials in .env
   - Check for any Twitter security prompts
   - Ensure account is not locked/restricted

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Security Notes

- Never commit .env file
- Regularly rotate credentials
- Monitor access logs
- Use environment variables in production

## License

MIT License - See LICENSE file for details

## Acknowledgments

- Selenium WebDriver
- Flask Framework
- MongoDB Team
- Twitter/X Platform

## Disclaimer

This tool is for educational purposes only. Use responsibly and in accordance with Twitter's Terms of Service.
