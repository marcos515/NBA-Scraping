# Simple webscraper for fetch NBA data 

The NBA website was written using angular, so to get the data it is necessary to run js. I used selenium to render the html by running js to get the data.

----------------
### How to run

- First of all, clone this project;

- Install the libs:
    ```bash
    $ pip3 install -r requirements.txt
    ```

- Download driver with the same version of your chrome desktop app on: https://sites.google.com/chromium.org/driver/downloads and put it on chrome_driver/ folder.

- Run the code:

    ```bash
    $ python3 scraping.py
    ```

- the result will appear in result folder as data.json.


----------