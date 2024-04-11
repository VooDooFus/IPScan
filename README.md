IPScan
IPScan is a Python script designed to scan text files for non-local IP addresses, count their occurrences, and query their ownership information. This tool provides insights into the distribution of IP addresses within a given text document.

Features
IP Extraction: IPScan utilizes regular expressions to extract IP addresses from text files efficiently.
Occurrence Counting: The script aggregates the extracted IP addresses and counts their occurrences.
Ownership Query: IPScan queries ownership information for non-local IP addresses using the ipinfo.io API, providing insights into the organizations associated with these addresses.
Output to CSV: IPScan outputs the results to a CSV file (ipscan.csv) for further analysis or processing.

Usage
Ensure you have Python installed on your system.
Copy the IPScan script to your desired location.
Prepare your text file containing the data you wish to scan for IP addresses. By default, the script is linked to sample.txt, but you can easily change the file path within the script.
Open a terminal or command prompt and navigate to the directory containing IPScan.

Run IPScan using the following command:
python ipscan.py

IPScan will read the contents of the specified text file and extract non-local IP addresses.
It will then count the occurrences of each IP address and query ownership information.
The results will be saved to ipscan.csv, containing columns for IP Address, Times Seen, and Ownership.
You can further analyze the CSV file using spreadsheet software or any other data analysis tool.

Disclaimer
IPScan relies on external services (ipinfo.io API) to fetch ownership information for IP addresses. Please ensure compliance with the terms of service of the utilized API and respect the privacy and usage policies of the queried organizations.

Note: IPScan may generate false positives or fail to identify certain IP addresses, depending on the formatting and context of the text file.

/VooDooFus/
