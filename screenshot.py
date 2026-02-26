import asyncio
from playwright.async_api import async_playwright

async def take_screenshot():
    # Prompt the user for the WebSocket Endpoint URL
    cdp_url = input("Please enter the CDP WebSocket URL (e.g., ws://127.0.0.1:9222/devtools/browser/...): ").strip()
    
    if not cdp_url:
        print("Error: WebSocket URL cannot be empty.")
        return

    print(f"Connecting to {cdp_url}...")
    
    try:
        async with async_playwright() as p:
            # Connect to the existing browser instance using the CDP URL
            browser = await p.chromium.connect_over_cdp(cdp_url)
            
            # Get the first context and first page
            contexts = browser.contexts
            if not contexts:
                print("No active browser contexts found.")
                await browser.close()
                return
                
            context = contexts[0]
            pages = context.pages
            
            if not pages:
                print("No active pages found in the context. Creating a new page...")
                page = await context.new_page()
            else:
                page = pages[0]
                
            print(f"Taking screenshot of page: {page.url}")
            
            # Take the screenshot
            filename = "screenshot.png"
            await page.screenshot(path=filename)
            
            print(f"Screenshot successfully saved to {filename}")
            
            # Close the connection (this does not close the actual browser)
            await browser.close()
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(take_screenshot())
