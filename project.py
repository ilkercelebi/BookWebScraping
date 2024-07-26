from selenium import webdriver
from selenium.webdriver.common.by import By
from pand import convert_to_df
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://books.toscrape.com/")

element_xpath = '//a[contains(text(),"Travel") or contains(text(),"Nonfiction")]'
element_links = driver.find_elements(By.XPATH, element_xpath)
category_urls = [element.get_attribute("href") for element in element_links]

def find_category_urls(driver, category_url, is_nonfiction):
    urls = []
    driver.get(category_url)
    while True:
        book_elements = driver.find_elements(By.XPATH, '//h3/a')
        for book in book_elements:
            book_url = book.get_attribute('href')
            urls.append(book_url)
        if is_nonfiction:
            try:
                next_button = driver.find_element(By.XPATH, '//li[@class="next"]/a')
                next_page_url = next_button.get_attribute('href')
                driver.get(next_page_url)
            except:
                break
        else:
            break
    return urls

def product_details(link):
    driver.get(link)
    
    price_path = '//p[@class="price_color"]'
    book_name_path = '//h1'
    book_star_path = '//p[contains(@class, "star-rating")]'
    book_description_path = '//*[@id="content_inner"]/article/p'

    try:
        price_element = driver.find_element(By.XPATH, price_path)
        price = price_element.text
    except:
        price = "Price not found"
    
    try:
        name_element = driver.find_element(By.XPATH, book_name_path)
        name = name_element.text
    except:
        name = "Name not found"
    
    try:
        star_element = driver.find_element(By.XPATH, book_star_path)
        star_class = star_element.get_attribute('class')
        
        star_rating = star_class.split()[-1]
    except:
        star_rating = "Rating not found"
    
    try:
        description_element = driver.find_element(By.XPATH, book_description_path)
        description = description_element.text
    except:
        description = "Description not found"

    return {
        'name': name,
        'price': price,
        'star_rating': star_rating,
        'description': description
    }

all_urls = []
for category_url in category_urls:
    is_nonfiction = "nonfiction" in category_url
    print(f"Processing category: {category_url}")
    category_urls = find_category_urls(driver, category_url, is_nonfiction)
    all_urls.extend(category_urls)

books_details = []
for url in all_urls:
    details = product_details(url)
    books_details.append(details)

df = convert_to_df(books_details)
print(df.head())
# print(books_details)

driver.quit()
