**Twitter Airflow Project**
![twitter](https://user-images.githubusercontent.com/51711008/201462230-7d767c6a-6367-40f7-8b82-cd23a14998ab.jpeg)

## Project Overview
The **Twitter-Airflow-Project** is an ETL pipeline designed to extract data from Twitter using the Twitter API, transform and clean it, and load it into a specified storage medium (e.g., database, CSV file). The pipeline is built using Apache Airflow for automation, ensuring periodic data extraction and processing with minimal manual intervention.

## Project Structure

* twitter_etl.py: A Python script that implements the ETL process for extracting tweets from the Twitter API, transforming the data (e.g., cleaning, processing), and loading it into a database or file.
* ismail_twitter.csv: A sample CSV file containing Twitter data.
( ismail_twets.pem: A private key file for securely accessing the Twitter API (ensure that this file is kept secure and not pushed to public repositories).
* Untitled-1.ipynb: A Jupyter Notebook used for exploratory data analysis on the Twitter data.

## Technologies Used

- **Apache Airflow**: Used to automate the ETL pipeline.
- **Python**: For scripting the ETL process.
- **Twitter API**: To fetch real-time Twitter data.
- **Pandas**: Data manipulation and cleaning.
- **GitHub Actions**: For continuous integration/continuous deployment (CI/CD).
- **Jupyter Notebook**: For data exploration and analysis.

## Setup Instructions

### Prerequisites
1. **Twitter Developer Account**: You need Twitter API keys. Create a Twitter Developer account and generate API keys.
2. **Python**: Ensure you have Python 3.7+ installed.
3. **Apache Airflow**: Install Airflow to schedule and manage the ETL pipeline.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iamismaill/Twitter-Airflow--Project.git
   cd Twitter-Airflow--Project
```
