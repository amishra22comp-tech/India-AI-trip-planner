# India AI Trip Planner

A beginner-friendly Python website made with Streamlit. It estimates a trip budget and creates a day-wise itinerary for selected destinations in India.

## Features
- Indian destinations and sample price estimates
- Group budget and per-person estimate
- Hotel, food, transport, sightseeing, and emergency budget breakdown
- Budget-overrun warning
- Day-wise itinerary and practical tips
- Downloadable trip plan as a text file
- No paid API key required

## Requirements
- Python 3.10 or newer
- VS Code
- Internet connection for installing Streamlit (the app itself uses sample data)

## Run in VS Code

1. Extract the project folder.
2. Open the `india_ai_trip_planner` folder in VS Code.
3. Open **Terminal → New Terminal**.
4. (Recommended) Create a virtual environment:

   Windows:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

   If PowerShell blocks activation, you can skip the virtual environment and use `py -m pip install -r requirements.txt`.

5. Install the dependency:
   ```powershell
   py -m pip install -r requirements.txt
   ```

6. Start the website:
   ```powershell
   py -m streamlit run app.py
   ```

7. Streamlit opens the app in your browser. If it does not, open the local URL shown in the terminal (usually `http://localhost:8501`).

## Project structure

```text
india_ai_trip_planner/
├── app.py
├── requirements.txt
└── README.md
```

## How it works
- Destination data stores sample daily hotel, food, local transport, travel, and sightseeing costs.
- The budget calculator multiplies daily estimates by days and travellers.
- It adds a 10% emergency reserve.
- A simple rule-based itinerary selects sample places and creates morning/afternoon/evening suggestions.

## Important limitations
This starter is a rule-based trip planner, not a connected generative AI service. Prices are illustrative and not live quotes. Confirm current transport fares, accommodation prices, attraction fees, opening hours, and safety advice before travelling.
