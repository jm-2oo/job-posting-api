## Job Posting API Python Script

### Objective

- I wanted to solve a problem where it would be easier for me to search through job postings
- It had to be stored in an Excel file so I could review the postings more easily

### Solution

- I created a script to connect to Reed's API that returned a list of job postings with my requirements
- The script calls Reed's API and transforms the API JSON data into a Pandas dataframe before exporting it as a CSV
- [Link to script](/api_scripts/reed_api_script.py)
- I've included a redacted screenshot of the output file below:

![sample_data](/misc_code/reed_api_screenshot.png)

### Next Steps

- Apply this script with other job posting APIs
- Refine the output data to filter for more relevant results

==========================================================================

## Google Maps API Python Script

### Objective

- I wanted a solution where I could get a list of companies in an area that I could then contact / check for job vacancies on their website

### Solution

- I created a script connecting to Google's Places API that returned a list of companies based on my search query
- The list returned the company's name, website URL and address
- I used Python's googlemaps library
- I could export the list as a CSV so I could review it further
- [Link to script](api_scripts/maps_api_script.py)
- As an example, below is a list of art galleries Central London

![sample_data](/misc_code/gallery_maps_api_screenshot.png)


