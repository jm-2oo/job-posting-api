## Job Posting API Python Script

### Objective

- I wanted to solve a problem where it would be easier for me to search through job postings
- It had to be stored in an Excel file so I could review the postings more easily

### Solution

- I created a script to connect to Reed's API that returned a list of job postings with my requirements
- The script calls Reed's API and transforms the API JSON data into a Pandas dataframe before exporting it as a CSV
- [Link to script](/reed_api/reed_api_script.py)
- I've included a redacted screenshot of the output file below:

![sample_data](/misc_code/reed_api_screenshot.png)

### Next Steps

- Apply this script with other job posting APIs
- Refine the output data to filter for more relevant results


