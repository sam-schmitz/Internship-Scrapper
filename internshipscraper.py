#internshipscraper.py
#By: Sam Schmitz
#scrapes ziprecruiter for the first 10 results from the search "fall 2024 software intern"

#I am using chromedriver-py version 126.0.6478.62
#and selenium version 4.6.0

from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path

HEADER = {'Connection': 'keep-alive',
            'Expires': '-1',
            'Upgrade_Insecure-Requests' : '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }

def get_internships():
    #gets the internships from zip recruiter    

    #open a connection to ziprecruiter
    driver = webdriver.Chrome(executable_path=binary_path)
    driver.get("https://www.ziprecruiter.com/jobs-search?search=fall+2024+software+intern&location=Remote+%28USA%29&days=&refine_by_employment=employment_type%3Aall&refine_by_salary=&refine_by_salary_ceil=&lvk=CZjcN9Y6oZJQA340DsUHXQ.--NQTbebbrF")
    
    #get the 1st ten results
    results = []
    
    #the first result is selected already so it has a different class name
    results.append(driver.find_element(By.XPATH, f"//div[@class='job_result_wrapper job_result_selected']/div/div/article/div/div/div/div/h2/a").text)
    
    #the others share a name so they can be grabbed in a loop
    wrappers = driver.find_elements(By.XPATH, f"//div[contains(@class, 'job_result_wrapper')]")
    for i in range(1, 10):
        results.append(wrappers[i].text.split('\n')[0])
    
    return results
    
if __name__ == "__main__":
    print(get_internships())