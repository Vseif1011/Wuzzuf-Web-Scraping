# Wuzzuf Job Scraper

This project is a web scraping tool designed to extract job listings from [Wuzzuf](https://wuzzuf.net/) for selected data-related fields. It collects job data for multiple queries and saves the combined results into a single CSV file.

## 📌 Description

The tool scrapes job data from Wuzzuf using Python and the BeautifulSoup library. It targets four specific job queries:

- Machine Learning
- Data Science
- Data Analysis
- Business Intelligence

For each query, it extracts:

- Job Title
- Occupation
- Description
- Company
- Location
- Link

The final combined dataset is exported as a CSV file named `Final_DATA_ALL.csv`.

## 📁 Project Structure

### `WWS.py`

Contains all core logic:
- `find_no_pages(search)` – Determines how many result pages exist for a search term.
- `scrap(query)` – Scrapes job listings for a given search query and returns both a dictionary and a pandas DataFrame.
- `combine_data_frames(dfs)` – Combines multiple DataFrames into one.
- `combine_dicts(dicts)` – Combines multiple dictionaries with the same keys into one dictionary.

### `Combined.py`

Main script that:
- Scrapes data for each of the four job categories.
- Combines the resulting DataFrames.
- Exports the final data to `Final_DATA_ALL.csv`.

## ✅ How to Use

1. Make sure the required libraries are installed:
   ```bash
   pip install requests beautifulsoup4 pandas lxml
