from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from typing import List, Tuple
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

class TwitterScraper:
    def setup_driver(self) -> webdriver.Chrome:
        """Set up Chrome WebDriver with proxy settings."""
        try:
            options = Options()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument("--window-size=1920,1080")
            options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
            
            driver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chromedriver.exe')
            driver = webdriver.Chrome(executable_path=driver_path, options=options)
            return driver
            
        except Exception as e:
            print(f"Chrome driver initialization error: {str(e)}")
            raise Exception("Failed to initialize Chrome driver")

    def login_to_twitter(self, driver: webdriver.Chrome) -> bool:
        """Log in to Twitter account."""
        try:
            driver.get('https://twitter.com/i/flow/login')
            print("Navigated to login page")
            time.sleep(5)  
            
            print("Looking for username field")
            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]'))
            )
            username_input.clear()
            username_input.send_keys(Config.TWITTER_USERNAME)
            username_input.send_keys(Keys.RETURN)
            print("Username entered")
            time.sleep(3)
            
            print("Looking for password field")
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.clear()
            password_input.send_keys(Config.TWITTER_PASSWORD)
            password_input.send_keys(Keys.RETURN)
            print("Password entered")
            
            time.sleep(10)
            
            try:
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="primaryColumn"]'))
                )
                print("Successfully logged in")
                return True
            except Exception as e:
                print(f"Login verification failed: {str(e)}")
                return False
            
        except Exception as e:
            print(f"Login error: {str(e)}")
            return False

    def get_trending_topics(self) -> Tuple[List[str], str]:
        """Scrape trending topics from Twitter."""
        driver = None
        try:
            driver = self.setup_driver()
            print("Driver initialized")
            
            if not self.login_to_twitter(driver):
                raise Exception("Failed to login to Twitter")
            
            print("Navigating to explore page")
            driver.get('https://twitter.com/explore/tabs/trending')
            time.sleep(8)  
            
            print("Scrolling page to load content")
            driver.execute_script("window.scrollBy(0, 300)")
            time.sleep(3)
            
            print("Looking for trends...")
            selectors = [
                '[data-testid="trend"]',
                '[data-testid="tweetText"]',
                'div[dir="ltr"] > span'
            ]
            
            trends = []
            for selector in selectors:
                try:
                    trend_elements = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
                    )
                    if trend_elements:
                        for element in trend_elements[:10]:
                            text = element.text.strip()
                            if (text and 
                                not text.startswith(('Trending', 'View', 'Show')) and 
                                len(text) > 1):
                                trends.append(text)
                                print(f"Found trend: {text}")
                            if len(trends) >= 5:
                                break
                        if len(trends) >= 5:
                            break
                except Exception as e:
                    print(f"Selector {selector} failed: {str(e)}")
                    continue

            if not trends:
                try:
                    all_text_elements = driver.find_elements(By.XPATH, "//span[string-length(text()) > 2]")
                    for element in all_text_elements[:20]:
                        text = element.text.strip()
                        if text and len(text) > 2 and not text.startswith(('Trending', 'View', 'Show')):
                            trends.append(text)
                            if len(trends) >= 5:
                                break
                except Exception as e:
                    print(f"Fallback method failed: {str(e)}")
            
            if not trends:
                print("No trends found, returning placeholder data")
                trends = ["No trends found"]
            
            trends = trends[:5]
            print(f"Successfully scraped {len(trends)} trends")
            return trends, "127.0.0.1"
            
        except Exception as e:
            print(f"Error in get_trending_topics: {str(e)}")
            raise Exception(f"Failed to scrape trending topics: {str(e)}")
        finally:
            if driver:
                try:
                    driver.quit()
                    print("Browser closed successfully")
                except Exception as e:
                    print(f"Error closing browser: {str(e)}")