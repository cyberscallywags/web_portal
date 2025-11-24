import pytest
from playwright.async_api import Page, expect
import os

BASE_URL = os.getenv("TEST_BASE_URL", "http://localhost:8000")

class TestSetupVerification:
    """Verify that the test setup is working correctly."""
    
    async def test_playwright_setup(self, page: Page):
        """Test that Playwright is working."""
        await page.goto("data:text/html,<h1>Test Page</h1>")
        await expect(page.locator("h1")).to_have_text("Test Page")
        
    async def test_server_accessible(self, page: Page):
        """Test that the server is accessible."""
        try:
            response = await page.request.get(BASE_URL)
            assert response.status == 200, f"Server returned {response.status}"
            print(f"✅ Server accessible at {BASE_URL}")
        except Exception as e:
            pytest.fail(f"❌ Server not accessible at {BASE_URL}: {e}")