import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
# url = 'https://www.indeed.com/jobs?q=ai+engineer&l=South+Florida%2C+FL'
url = 'https://www.glassdoor.com/Job/south-florida-ai-engineer-jobs-SRCH_IL.0,13_IC1166206_KO14,25.htm?clickSource=searchBox'

# Get the page contents
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Get the job results
results = soup.find(id='jobResults')
# results = soup.find_all('div', class_ ='jobResults')


job_titles = []
for card in results:
    title_elem = card.find('a', class_='span')
    if title_elem is not None:
        job_titles.append(title_elem.text.strip())
    print()

job_data = {'Title': job_titles}
df = pd.DataFrame.from_dict(job_data) 
df.to_csv('test.csv', index=False, encoding='utf-8')

# titles = soup.find_all('h2', class_='jobTitle')
# job_elems = results.inf_all('div', class_='jobsearch-SerpmMainContent')