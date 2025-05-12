#!/usr/bin/env python3
"""
Simple YouTube Homepage Scraper using Playwright
"""

import asyncio
from playwright.async_api import async_playwright


async def main():
    """Simple script to take a screenshot of YouTube homepage."""
    async with async_playwright() as p:
        print("Launching browser...")
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("Navigating to YouTube...")
        await page.goto("https://www.youtube.com/")
        
        print("Taking screenshot...")
        await page.screenshot(path="youtube_homepage.png")
        
        print("Getting page title...")
        title = await page.title()
        print(f"Page title: {title}")
        
        print("Closing browser...")
        await browser.close()
        
        print("Done! Screenshot saved as youtube_homepage.png")


if __name__ == "__main__":
    asyncio.run(main())
