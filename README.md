# BUXC433-BostonGlobe
Code for BUXC433 Justice Media Boston Globe Team

## Getting Started
### Google Cloud Vision API
The code for this project relies on the Google Cloud Vision Api. To install and get started with it, please follow steps 1-6 in this [codelab for the API](https://codelabs.developers.google.com/codelabs/cloud-vision-api-python#0).
Use this link to set up the API Authentication Key and save it to your computer (and be sure to set the path as an environment variable using a .env file): https://cloud.google.com/vision/docs/libraries 
Once done, upload your pdfs to Google Cloud Storage and ensure the paths in the code match the paths in GCS.  

### To Run
Run in the following order:
  1. scrape_from_pdfs.py: Extracts text from pdfs and stores output JSON files in a separate folder.
  2. parse_data.py: Merges all JSON into a single file for each grievance, then extracts the desired fields and uploads the extracted data to GCS under parsed_data/ folder.
  3. export_to_csv.py: Exports all data from parsed_data/ folder on GCS to a CSV file.
  4. flag_text.py: Checks grievance text for certain keywords and adds flags to CSV file.

# DEPRECIATED
## This section pertains to the original forked version of this repo, however MySQL and other tools below are no longer being used for this project
### MySQL database
The project also uses a MySQL database to store the grievances data. To use it, MySQL needs to be installed. Here is the [installation page](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/) for MySql and just install the one that is appropriate for the system you are using. I also highly recommend installing [mySQL Workbench](https://www.mysql.com/products/workbench/) which allows for database management using a GUI. Make sure you create a database called "grievancesDB" before running the script.
### Installing the packages
Once you have installed the the Google Cloud Vision API and mySQL, clone the repository, copy into Google Cloud and download the rest of the requirements by running the following commands:
```
pip3 install -r requirements.txt
```
You may have to run this command as well:
```
pip3 install mysql-connector-python 
```
### Running the code
To run the code, go into the code/ocr_scan directory. Then create an environment variable called `SQLPWD`to your mySQL password and `GRIEVANCES_DIRECTORY` to the directory of where the images of your grievances are in Google Cloud. Also, make sure the filetype specified in the code is set to ".pdf". Once that is done, run the code with the following command
```
python3 vision.py
```
