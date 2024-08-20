# Weather API project

This repository is dedicated to learning to use an `API` from [Open Meteo API](https://open-meteo.com) website.
The project involves fetching API data, saving it to a CSV file and using various techniques to **plot** and **prepare** them for analysis.

## Table of Contents

- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Structure

```bash
├── weather_api.py                # Python scripts for the API request and plotting the data
├── weather_data.csv              # Saved API data
└── README.md
```
`weather_api.py`: Contain the python script for the API request, CSV file writing and plotting the fetched data.
`weather_data.csv`: Contains the processed data in a CSV format.

## Technologies Used

- **Python**
- **Requests**
- **Datetime**
- **CSV**
- **Pandas**
- **Matplotlib** *(for visualisation)*

## Setup

**Clone the repository:**
```bash
git clone https://github.com/pitukepe/API_Plot.git
```
**Install the required packages:**
```bash
pip install -r requirements.txt
```

## Usage

Python Scripts: Run the scripts in the scripts/ directory to automate the cleaning process of the messy database.
Example:
```bash
python3 weather_api.py
```

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or have a suggestion.
