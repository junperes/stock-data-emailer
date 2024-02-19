# About

This repository contains a bot designed to extract data from a stock portfolio listed in Excel using the `pandas_datareader` library. It fetches data from the last n days, where n is the input value of the function. From this data, it calculates today's value and the minimum, average, and maximum values of the adjusted closing prices for the last n days.

Additionally, the bot extracts quotes for the dollar, euro, and cryptocurrencies using an API.

Finally, it includes a function to send all this information via email.

## Installation:

To set up the project, follow these steps:

1. Initialize a virtual environment within the project folder:

    Linux or Mac:
    ```bash
    python3 -m venv .env
    source env/bin/activate
    ```

    Windows:
    ```bash
    py -m venv .env
    .\env\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration:

This repository contains several Python scripts:

- `cotacoes.py`: This script is an independent program with two functions:
    - `carteira(n_days)`: This function takes the number of retroactive days as a parameter and defaults to today's date as the end date. For each stock in the portfolio, the function returns today's calculated adjustment, as well as the minimum, average, and maximum values for the last n days.
    - `moeda()`: This function takes no parameters and returns the values of quotes for the dollar, euro, and cryptocurrency at the moment the program is executed.

- `cotacoesHTML.py`: Similar to `cotacoes.py`, but with HTML adjustments to format the email sending.

- `robotmail.py`: This script contains the `send_mail(message1, message2)` function, which takes two parameters representing the `carteira` and `moeda` functions. It sends the results to the specified email address.

Before using the email functionality, ensure you modify the following fields in the code:
- `sender_email`: Your email address.
- `receiver_email`: The recipient's email address.
- `password`: Your email password. If using Gmail, you may need to generate an app password.

Failure to provide accurate credentials, especially for Gmail accounts, may result in email sending failures due to Google's security settings.
