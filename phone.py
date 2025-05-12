#!/usr/bin/env python3
"""
YouTube Homepage Scraper using Playwright
This script navigates to the YouTube homepage and extracts video information.
"""

import asyncio
from playwright.async_api import async_playwright
import json
from datetime import datetime


async def scrape_youtube_homepage():
    """
    Scrape the YouTube homepage for video information.
    Returns a list of dictionaries containing video data.
    """
    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=False)  # Set to True for headless mode
        page = await browser.new_page()

        # Navigate to YouTube
        print("Navigating to YouTube homepage...")
        await page.goto("https://www.youtube.com/")

        # Wait for the content to load
        print("Waiting for content to load...")
        await page.wait_for_selector("#contents")

        # Extract video information
        print("Extracting video information...")
        videos = await page.evaluate("""
            () => {
                const videoElements = document.querySelectorAll('ytd-rich-grid-media');
                return Array.from(videoElements).slice(0, 10).map(video => {
                    // Get title
                    const titleElement = video.querySelector('#video-title');
                    const title = titleElement ? titleElement.textContent.trim() : 'Unknown Title';

                    // Get channel name
                    const channelElement = video.querySelector('#channel-name a');
                    const channel = channelElement ? channelElement.textContent.trim() : 'Unknown Channel';

                    // Get video metadata (views, time)
                    const metadataElement = video.querySelector('#metadata-line');
                    let views = 'Unknown';
                    let publishTime = 'Unknown';

                    if (metadataElement) {
                        const metaSpans = metadataElement.querySelectorAll('span');
                        if (metaSpans.length >= 1) views = metaSpans[0].textContent.trim();
                        if (metaSpans.length >= 2) publishTime = metaSpans[1].textContent.trim();
                    }

                    // Get video URL
                    const linkElement = video.querySelector('a#thumbnail');
                    const url = linkElement ? 'https://www.youtube.com' + linkElement.getAttribute('href') : 'Unknown URL';

                    return {
                        title,
                        channel,
                        views,
                        publishTime,
                        url
                    };
                });
            }
        """)

        # Close the browser
        await browser.close()

        return videos


async def main():
    """Main function to run the scraper and save results."""
    try:
        # Scrape YouTube homepage
        videos = await scrape_youtube_homepage()

        # Print results
        print(f"\nFound {len(videos)} videos on the YouTube homepage:")
        for i, video in enumerate(videos, 1):
            print(f"\n{i}. {video['title']}")
            print(f"   Channel: {video['channel']}")
            print(f"   Views: {video['views']}")
            print(f"   Published: {video['publishTime']}")
            print(f"   URL: {video['url']}")

        # Save results to a JSON file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"youtube_data_{timestamp}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(videos, f, indent=2, ensure_ascii=False)

        print(f"\nData saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())