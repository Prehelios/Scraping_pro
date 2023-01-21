# Scraping_pro
This is a better version of my scraping initial.

This script uses the requests library to send a GET request to the website and retrieve the HTML content.

It then uses BeautifulSoup to parse the HTML content and locate the elements containing the data you want to scrape.

It uses find_all() method to find all elements with a certain CSS class (here 'data-container') and store these elements in a list.

It also handles pagination by using the find() method to find the link to the next page, it checks if that link exists, and uses the get() method to retrieve the URL of the next page.

It also checks whether the data has been extracted or not before trying to save it to a file. It also handles paging and connection errors more robustly by using a while loop to continue paging until there are no more following pages or an error occurs.

It handles URLs that do not contain a scheme (http or https). This code checks if the URL given by the user does not contain a scheme (http or https). If it doesn't, it prepends 'http://' to the URL before sending it with the request. This allows the user to enter URLs of the form 'www.example.com' without creating errors.

Finally, this code writes the extracted data to a CSV file, using the name of the chosen option as the file name (for example, 'links_output.csv' for the 'Scrape links' option). It also checks if data has been extracted before writing to a file.
