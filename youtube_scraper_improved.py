#!/usr/bin/env python3
"""
Improved YouTube Homepage Scraper using Playwright
This script navigates to the YouTube homepage and extracts information
with improved waiting and interaction.
"""

import asyncio
from playwright.async_api import async_playwright
import json
from datetime import datetime


async def main():
    """Main function to scrape YouTube homepage with improved techniques."""
    async with async_playwright() as p:
        # Launch the browser with slower navigation to allow content to load
        print("Launching browser...")
        browser = await p.chromium.launch(headless=False)  # Set to False to see what's happening
        
        # Create a context with a larger viewport
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )
        
        # Create a new page
        page = await context.new_page()
        
        # Navigate to YouTube with a longer timeout
        print("Navigating to YouTube...")
        await page.goto("https://www.youtube.com/", wait_until="networkidle", timeout=60000)
        
        # Wait for the page to be fully loaded
        print("Waiting for content to load...")
        await page.wait_for_load_state("networkidle")
        
        # Scroll down to trigger lazy loading
        print("Scrolling to load more content...")
        for _ in range(3):
            await page.evaluate("window.scrollBy(0, 1000)")
            await asyncio.sleep(1)
        
        # Wait a bit more for content to load after scrolling
        await asyncio.sleep(3)
        
        # Take a screenshot
        print("Taking screenshot...")
        await page.screenshot(path="youtube_homepage_improved.png")
        
        # Extract information
        print("Extracting page information...")
        
        # Get page title
        title = await page.title()
        
        # Try different selectors for videos
        selectors = [
            'ytd-rich-grid-media',
            'ytd-rich-item-renderer',
            '#content.ytd-rich-item-renderer',
            'ytd-video-renderer',
            '#dismissible.ytd-rich-grid-media'
        ]
        
        video_count = 0
        video_titles = []
        
        for selector in selectors:
            # Check if this selector exists on the page
            has_selector = await page.evaluate(f"""
                () => {{
                    return document.querySelectorAll('{selector}').length > 0;
                }}
            """)
            
            if has_selector:
                print(f"Found videos using selector: {selector}")
                
                # Count videos
                video_count = await page.evaluate(f"""
                    () => {{
                        return document.querySelectorAll('{selector}').length;
                    }}
                """)
                
                # Get video titles
                video_titles = await page.evaluate(f"""
                    () => {{
                        const elements = Array.from(document.querySelectorAll('{selector}'));
                        return elements.slice(0, 10).map(el => {{
                            const titleEl = el.querySelector('#video-title, .title');
                            return titleEl ? titleEl.textContent.trim() : null;
                        }}).filter(title => title !== null);
                    }}
                """)
                
                if video_titles.length > 0:
                    break
        
        # Collect results
        results = {
            "page_title": title,
            "video_count": video_count,
            "sample_titles": video_titles,
            "timestamp": datetime.now().isoformat()
        }
        
        # Save results to a JSON file
        filename = "youtube_improved_data.json"
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
        print(f"Screenshot saved as youtube_homepage_improved.png")
        
        # Close the browser
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
