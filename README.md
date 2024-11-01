This program is designed to record all product links from a category page on Kaspi into an Excel file. Here’s how it works:

![Screenshot](https://github.com/PoweRFullGG/ProductParserKaspi/blob/main/Screenshot_234.png)

Input a Category Link: You simply enter the URL of a category on Kaspi.

Web Scraping: Using Selenium, the program navigates to the specified category and extracts links to all available products.

Excel File Creation: It saves these links in an Excel file named links.xlsx.

Scrolling and Loading More Links: The program scrolls down the page to load more products automatically until there are no more links to collect.

The program runs in headless mode, which means it operates without opening a visible browser window. This makes it efficient for running in the background.
