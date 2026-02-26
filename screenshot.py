import asyncio
import urllib.request
import json
from playwright.async_api import async_playwright


async def take_screenshot():
    # 1. Fetch available pages from localhost:9223
    try:
        print("Fetching available pages from http://localhost:9223/json...")
        with urllib.request.urlopen("http://localhost:9223/json") as response:
            pages_data = json.loads(response.read().decode())
    except Exception as e:
        print(f"Failed to fetch pages from localhost:9223: {e}")
        print("Make sure your browser is running with remote-debugging-port=9223")
        return

    # 2. Look for the "Manager" page
    target_ws_url = None
    target_title = None

    for page_info in pages_data:
        # Check if "Manager" is in the title, and it is a connectable page
        title = page_info.get("title", "")
        if "Manager" in title and "webSocketDebuggerUrl" in page_info:
            target_ws_url = page_info["webSocketDebuggerUrl"]
            target_title = title
            break

    if not target_ws_url:
        print(
            "Could not find any page with 'Manager' in the title that has a WebSocket URL."
        )
        print("Available pages were:")
        for p in pages_data:
            print(f" - {p.get('title', 'Unknown')} ({p.get('url', 'Unknown')})")
        return

    print(f"Found target page: '{target_title}'")
    print(f"Connecting to {target_ws_url}...")

    # 3. Connect and take screenshot
    try:
        async with async_playwright() as p:
            # We connect over CDP
            browser = await p.chromium.connect_over_cdp(target_ws_url)

            # Find the active page context (connecting usually attaches to the first one)
            contexts = browser.contexts
            if not contexts:
                print("No active browser contexts found after connecting.")
                await browser.close()
                return

            context = contexts[0]
            pages = context.pages

            if not pages:
                print("No active pages found in the context.")
                await browser.close()
                return

            # Since we connected directly to a specific page's websocket URL (target_ws_url),
            # it should be the first page in the list.
            page = pages[0]

            print(f"Taking screenshot of page: {page.url}")

            # Extract and print available elements on the page
            print("\n--- Available Elements on Page ---")
            elements = await page.evaluate("""() => {
                const els = Array.from(document.querySelectorAll('button, a, input, [role="button"], h1, h2, h3'));
                return els.map(el => {
                    const text = (el.innerText || el.value || '').trim().replace(/\\n/g, ' ');
                    const tag = el.tagName.toLowerCase();
                    return text ? `${tag}: ${text}` : null;
                }).filter(Boolean);
            }""")

            if elements:
                for el in elements:
                    print(f" - {el}")
            else:
                print(" - No meaningful interactive elements found.")
            print("----------------------------------\n")

            # Take the screenshot
            filename = "manager_screenshot.png"
            await page.screenshot(path=filename)

            print(f"Screenshot successfully saved to {filename}")

            # Close the connection (this does not close the actual browser)
            await browser.close()

    except Exception as e:
        print(f"An error occurred while taking the screenshot: {e}")


if __name__ == "__main__":
    asyncio.run(take_screenshot())
