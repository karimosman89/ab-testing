# A/B Testing Project

## Overview
This project analyzes A/B test results to determine if there is a statistically significant difference between two groups (control and treatment).

## Project Structure

             ab-testing /
                        │ 
                        ├── data/ # Data files 
                                │ 
                                └── ab_test_results.csv # Example A/B test results 
                        ├── src/ 
                               │ 
                               ├── ab_test.py # A/B testing analysis script 
                               │ 
                               └── utils.py # Utility functions 
                        ├── tests/ # Test scripts 
                                 │ 
                                 └── test_ab_test.py # Unit tests for A/B testing 
                        ├── requirements.txt # Dependencies 
                        └── README.md # Project documentation

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/karimosman89/ab-testing.git
   cd ab-testing

2. Install the required packages:
     pip install -r requirements.txt


## Usage

1. Prepare your A/B test results in the **/data** directory and name it **ab_test_results.csv**.
   
2. **Analyze the A/B test results:**
            python src/ab_test.py

   
 ## Testing    

Run the unit tests to ensure the utility functions work as expected:

     python -m unittest discover -s tests


## License
 This project is licensed under the MIT License.
 
