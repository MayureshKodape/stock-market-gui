# Stock Market GUI Tracker (India) — Python + Tkinter + yfinance

## 1. Introduction
The **Stock Market GUI Tracker** is a desktop application built using **Tkinter** (a Python GUI library) to track real-time stock prices of Indian companies. The application retrieves stock data from the **yfinance** API, displaying the price of stocks in **Indian Rupees (₹)**. Users can track live stock prices by entering the stock symbol and receiving real-time updates.

This application is designed for Indian stock markets (**BSE, NSE**) and displays data in **₹ (Indian Rupees)**.

---

## 2. Features
- **Real-time Updates:** The application fetches live stock prices every **2 seconds**.
- **User-Friendly Interface:** A simple and intuitive GUI for users to input stock symbols and get real-time price data.
- **Indian Stocks Only:** Displays stock prices for Indian companies, formatted in **₹**.
- **Error Handling:** The app gracefully handles invalid stock symbols and displays a relevant message.

---

## 3. Tech Stack
- **Python:** The core programming language used for the application.
- **Tkinter:** The GUI library used to create the graphical interface.
- **yfinance:** A library that pulls real-time stock data from Yahoo Finance. It supports Indian stocks with the `.NS` suffix (e.g., `TCS.NS`, `RELIANCE.NS`).

---

## 4. Installation Guide

### Prerequisites
To run this application, you need to have Python installed on your machine. If not, you can download Python from the official website.

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/stock-market-gui.git
cd stock-market-gui
Step 2: Install Dependencies
You will need the following libraries: Tkinter and yfinance.

Option A: Using requirements.txt (Recommended)
Create a file named requirements.txt in the project folder and add the following lines:

yfinance

tk

Then install the required libraries:

bash
Copy code
pip install -r requirements.txt
Option B: Install the Libraries Individually
bash
Copy code
pip install yfinance
pip install tk
Step 3: Run the Application
Once the dependencies are installed, you can run the application with the following command:

bash
Copy code
python main.py
This will open the GUI for stock tracking.

5. Usage Instructions
Enter Stock Symbol
In the input box, type the stock symbol for an Indian company. For example:

TCS.NS for Tata Consultancy Services

RELIANCE.NS for Reliance Industries

INFY.NS for Infosys

Note: The .NS suffix is required for Indian stocks on Yahoo Finance.

Press Track
After entering the stock symbol, press the Track button to get real-time stock data.

View Stock Price
The application will display the stock price in ₹ (Indian Rupees).

Error Handling
If an invalid stock symbol is entered (e.g., TCS without .NS), the application will display "Invalid Symbol."

6. Example Usage
After running the application, you will be presented with a simple window. Here’s what you need to do:

In the input field, type TCS.NS and press Track.

The current stock price of Tata Consultancy Services will be displayed in ₹, like this:

makefile
Copy code
TCS.NS: ₹3,542.67
You can also enter other Indian stock symbols like:

RELIANCE.NS for Reliance Industries

INFY.NS for Infosys

HDFC.NS for HDFC Bank

7. Troubleshooting
Problem: "Invalid Symbol" is displayed
Solution: Make sure you enter the correct stock symbol with the .NS suffix for Indian stocks. For example, enter TCS.NS for Tata Consultancy Services, not just TCS.

Problem: No stock data is displayed
Solution: Ensure you have an active internet connection, as the application fetches real-time stock data from the web.

Problem: Tkinter not installed
Solution: If Tkinter is not already installed, you can install it by running:

bash
Copy code
pip install tk
perl
Copy code

If you want, tell me the **actual filename** in your repo (`main.py` or something else) and I’ll replace `python main.py` with the exact correct run command.
::contentReference[oaicite:0]{index=0}
