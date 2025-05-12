#!/usr/bin/env python3
"""
YouTube Homepage Scraper using Playwright
This script navigates to the YouTube homepage and extracts basic information.
"""

import asyncio
from playwright.async_api import async_playwright
import json
from datetime import datetime


async def main():
    """Main function to scrape YouTube homepage."""
    async with async_playwright() as p:
        # Launch the browser (headless=True for no UI, False to see the browser)
        print("Launching browser...")
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Navigate to YouTube
        print("Navigating to YouTube...")
        await page.goto("https://www.youtube.com/")
        
        # Wait for content to load
        print("Waiting for content to load...")
        await page.wait_for_selector("#contents", timeout=30000)
        
        # Take a screenshot
        print("Taking screenshot...")
        await page.screenshot(path="youtube_homepage_full.png")
        
        # Extract basic page information
        print("Extracting page information...")
        
        # Get page title
        title = await page.title()
        
        # Count video elements (this selector might need adjustment)
        video_count = await page.evaluate("""
            () => {
                const videos = document.querySelectorAll('ytd-rich-grid-media');
                return videos.length;
            }
        """)
        
        # Get a few video titles as a sample
        video_titles = await page.evaluate("""
            () => {
                const titleElements = document.querySelectorAll('#video-title');
                return Array.from(titleElements)
                    .slice(0, 5)
                    .map(el => el.textContent.trim());
            }
        """)
        
        # Collect results
        results = {
            "page_title": title,
            "video_count": video_count,
            "sample_titles": video_titles,
            "timestamp": datetime.now().isoformat()
        }
        
        # Save results to a JSON file
        filename = "youtube_basic_data.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Print results
        print(f"\nResults:")
        print(f"Page title: {title}")
        print(f"Video count: {video_count}")
        print(f"Sample video titles:")
        for i, title in enumerate(video_titles, 1):
            print(f"  {i}. {title}")
        
        print(f"\nData saved to {filename}")
        print(f"Screenshot saved as youtube_homepage_full.png")
        
        # Close the browser
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
