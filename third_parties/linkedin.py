import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from a linkedin profile"""
    headers = {'Authorization': 'Bearer ' + os.environ.get('PROXYCURL_API_KEY')}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    linkedin_profile_url = 'https://www.linkedin.com/in/williamhgates'

    response = requests.get(api_endpoint,
                            params={'url': linkedin_profile_url},
                            headers=headers)
