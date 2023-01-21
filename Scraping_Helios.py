# -*- coding: cp1252 -*-

# -*- coding: UTF-8 -*-


##### Modules import #####

import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url, option):
    extracted_data = []
    while url:
        try:
            # Send a request to the website
            if not url.startswith("http"):
                url = "http://" + url
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            break
        except Exception as err:
            print(f'Other error occurred: {err}')
            break
        
        if option == "Links":
            # Scrape all links from the website
            links = soup.find_all('a')
            extracted_data = [link.get('href') for link in links]
        elif option == "Domain Names":
            # Extract domain names from the website's links
            links = soup.find_all('a')
            extracted_data = [link.get('href').split("//")[-1].split("/")[0] for link in links]
        elif option == "HTML":
            # Extract the website's HTML content
            extracted_data = [response.text]
        elif option == "Part":
            # Find the data we want to scrape
            data = soup.find_all('div', class_='data-container')
            extracted_data = [item.text for item in data]
        else:
            break
        
        # Handle pagination
        next_page = soup.find('a', class_='next-page')
        if next_page:
            url = next_page.get('href')
        else:
            url = None
    return extracted_data

# Example usage

print("Welcome to the Web Scraper")

while True:
    print ("###################################################")
    print ("#               Scraping Website                  #")
    print ("#                Scrap & Extract                  #")
    print ("#               -----------------                 #")
    print ("#                DreAmuS/HelioS                   #")
    print ("###################################################")
    print ("")
    print("Please choose an option:")
    print(" [+] 1. Scrape links from a website")
    print(" [+] 2. Extract domain names from a website")
    print(" [+] 3. Extract HTML content of a website")
    print(" [+] 4. Extract a specific part of a website")
    print(" [+] 5. Quit")

    option = input()

    if option == "1":
        option = "Links"
    elif option == "2":
        option = "Domain Names"
    elif option == "3":
        option = "HTML"
    elif option == "4":
        option = "Part"
    elif option == "5":
        break
    else:
        print("Invalid option")
        continue

    url = input("Enter the URL to scrape: ")
    data = scrape_data(url, option)

    if data:
        # Write the data to a CSV file
        filename = f"{option.lower()}_output.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([option])
            for row in data:
                writer.writerow([row])
        print(f"Scraping finished! Data saved to {filename}.")
    else:
        print("No data to save.")
