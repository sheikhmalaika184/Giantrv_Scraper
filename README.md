# Giantrv_Scraper
This Python script scrapes **RV inventory data** from [giantrv.com](https://giantrv.com) using their public API.  
It extracts details like **title, price, VIN, engine, dimensions, features, images, and contact info** and saves them into JSON files.

## Features
- Scrapes multiple RV categories (Class A, Class B, Class C, Fifth Wheel, Toy Hauler, Destination Trailers).
- Collects structured fields (title, VIN, engine, fuel type, etc.).
- Saves clean JSON output with all details & images.
- Modular design (functions for each category).
- Easy to extend for new categories.

## Installation Steps
1. Clone the repo and install dependencies:
2. git clone https://github.com/sheikhmalaika184/Giantrv_Scraper.git
3. cd Giantrv_Scraper
4. pip install -r requirements.txt 

## Output Files
By default, the script saves output into JSON files like:
1. class_a.json
2. class_b.json
3. travel_trailers.json
4. fifth_wheel.json
5. toy_hauler.json
6. destinations.json

## Sample Output
[
  {
    "vehicle_id": "12345",
    "title": "2025 Thor Motor Coach Axis",
    "vin": "1F65F5DY0J0A12345",
    "engine": "V8 Gasoline",
    "price_msrp": 145000,
    "current_price": 129999,
    "images": ["https://...jpg", "..."],
    "address": "123 RV Street Colton CA 92324",
    "phone_no": "800-123-4567"
  }
]
