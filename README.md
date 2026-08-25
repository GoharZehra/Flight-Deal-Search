# Flight Price Tracker & Alert System

A lightweight program written with Python to check for the cheapest available flight. It checks for flight deals using **SerpAPI (Google Flights)**, tracks baseline prices in **Google Sheets** via **Sheety**, and then dispatches deal alerts to registered users through **Twilio (SMS/WhatsApp)** and **SMTP Email**.

## Features

1) **Price Checks:** The program queries live Google Flights data via SerpAPI.
2) **Google Sheets as a Database:** Uses Sheety API to easily view, manage, and update baseline prices.
3) **User Signup:** Syncs with a Google Form to maintain a real-time list of email/SMS subscribers.
4) **Multi-Channel Alerts:** Sends instant notifications with flight details and price comparisons via Email (`smtplib`) or Twilio (`SMS` / `WhatsApp`).
5) **Environment Isolation:** Credentials are kept safe using an `.env` file.

## Tech Stack & Requirements

- **APIs & Services:**
  - [SerpAPI](https://serpapi.com/) — To get Flight Data.
  - [Sheety](https://sheety.co/) — Google Sheets REST API.
  - [Twilio](https://www.twilio.com/) — SMS / WhatsApp alert messaging.
  - Gmail SMTP (via `smtplib`) — Email alerts
- **Libraries:** `requests`, `requests-cache`, `python-dotenv`

## Setup & Configuration

**1. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**2. Google Sheets Setup:**
- Create a first google sheet named 'prices' with columns named City, IATA Code, Lowest Price and add some example data.
    - City: Paris, Frankfurt, Tokyo
    - IATA Code: CDG, FRA, HND
    - Lowest Price: 200, 200, 200
- Add another sheet named 'users' and link it with your google form which takes the user's first name, last name and email.
- Link the sheets with sheety.co and enable GET, POST and PUT permissions.

**3. Environment Variables:**
- Create a .env file based on .env.example and populate your API credentials.

**4. Run:**
- python main.py


To run it periodically, set up a cron job, Windows Task Scheduler, or deploy via GitHub Actions.
