# YouTube Homepage Scraper

A Python project using Playwright to scrape the YouTube homepage for video information.

## Overview

This project demonstrates how to use Playwright with Python to automate browser interactions and extract data from the YouTube homepage. It includes several scripts with different approaches to web scraping.

## Features

- Browser automation with Playwright
- Screenshot capture of web pages
- Data extraction from dynamic web content
- JSON data storage
- Multiple scraping approaches with varying complexity

## Scripts

1. **simple_scraper.py**: A basic script that navigates to YouTube and takes a screenshot.
2. **youtube_scraper.py**: A more comprehensive script that attempts to extract video information.
3. **youtube_scraper_improved.py**: An enhanced version with better waiting, scrolling, and multiple selector attempts.
4. **phone.py**: The original script with detailed video extraction capabilities.

## Requirements

- Python 3.7+
- Playwright
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd youtube-scraper
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```
   python -m playwright install
   ```

## Usage

Run any of the scripts to scrape the YouTube homepage:

```
python simple_scraper.py
```

or

```
python youtube_scraper_improved.py
```

## Output

The scripts generate:

- Screenshots of the YouTube homepage (saved as PNG files)
- JSON files containing extracted data
- Console output with scraping results

## Challenges and Limitations

Web scraping YouTube can be challenging due to:

1. Dynamic content loading
2. Anti-scraping measures
3. Frequent changes to the website's structure
4. JavaScript-heavy implementation

The scripts may need periodic updates to adapt to changes in YouTube's interface.

## Legal Considerations

Before scraping any website, be sure to:

1. Review the website's Terms of Service
2. Respect robots.txt directives
3. Implement rate limiting to avoid overloading servers
4. Only use the data in accordance with applicable laws and regulations

## Future Improvements

- Implement more robust error handling
- Add proxy support for distributed scraping
- Create a configurable scraping pipeline
- Add support for scraping video details pages
- Implement data storage in a database

## License

[MIT License](LICENSE)

## Disclaimer

This project is for educational purposes only. Use responsibly and in accordance with YouTube's Terms of Service.
