import requests
import json

def extract_data(url,detail_url, outputfile, type="a"):
    page_no = 1
    payload = {}
    headers = {
    'Cookie': 'DO-LB="Cg4xMC4xMTYuMTYuNTo4MBD1qwM="'
    }
    ids = []
    scraped_data = []
    while(True):
        ids_url = url.replace("page=2",f"page={page_no}")
        response = requests.request("GET", ids_url, headers=headers, data=payload)
        data = response.json()
        if(len(data["ids"]) == 0):
            break
        ids.extend(data["ids"])
        page_no = page_no + 1
    for id in ids[:]:
        temp_data = {}
        vehicle_url = f"https://inventory.coasttechnology.org/api/v3/inventory/{id}"
        detaild_url = detail_url.replace("-id",f"-{id}")
        response = requests.request("GET", vehicle_url, headers=headers, data=payload)
        vehicle_data = response.json()
        title = vehicle_data["data"]["title"]
        stock_number = vehicle_data["data"]["stock_number"]
        vin = vehicle_data["data"]["vin"]
        miles = vehicle_data["data"]["odometer"]
        length = vehicle_data["data"]["vehicle_body_length"]
        width = vehicle_data["data"]["vehicle_body_width"]
        height = vehicle_data["data"]["vehicle_body_height"]
        engine = vehicle_data["data"]["engine"]
        fuel_type = vehicle_data["data"]["fuel_type"]
        horsepower = vehicle_data["data"]["horsepower"]
        torque = vehicle_data["data"]["torque"]
        sleeps = vehicle_data["data"]["max_sleeping_count"]
        slideouts = vehicle_data["data"]["number_of_slideouts"]
        fresh = vehicle_data["data"]["total_fresh_water_tank_capacity"]
        grey = vehicle_data["data"]["total_gray_water_tank_capacity"]
        black = vehicle_data["data"]["total_black_water_tank_capacity"]
        furnance_btu = vehicle_data["data"]["heater_btu"]
        chassis_brand = vehicle_data["data"]["chassis_brand"]
        water_heater = vehicle_data["data"]["water_heater_tank_capacity"]
        driveline_type = vehicle_data["data"]["driveline_type"]
        fuel_capacity = vehicle_data["data"]["fuel_tank_capacity"]
        two_capacity = vehicle_data["data"]["towing_capacity"]
        air_conditioning_btu = vehicle_data["data"]["air_conditioning_btu"]
        floorplan_style = vehicle_data["data"]["floorplan_style"]
        price_msrp = vehicle_data["data"]["price_msrp"]
        current_price = vehicle_data["data"]["price_current"]
        created_at = vehicle_data["data"]["created_at"]
        if(type == "b"):
            gvwr = vehicle_data["data"]["gvwr"]
            hitch_weight = vehicle_data["data"]["hitch_weight"]
            dry_weight = vehicle_data["data"]["dry_weight"]
        try:
            address = vehicle_data["data"]["company_location"]["address"] + " " + vehicle_data["data"]["company_location"]["city"] + " " + vehicle_data["data"]["company_location"]["state"] + " " + vehicle_data["data"]["company_location"]["zip"]
        except:
            address = ""
        phone_no = vehicle_data["data"]["company_location"]["phone"]
        email = vehicle_data["data"]["company_location"]["email"]
        try:
            feature_list = vehicle_data["data"]["feature_list"]
        except:
            feature_list = []
        try:
            description = vehicle_data["data"]["inventory_unit_descriptions"][0]["description"]
        except:
            description = ""
        images = []
        images_list = vehicle_data["data"]["images"]
        try:
            display_image = vehicle_data["data"]["display_image"]
            images.append(display_image)
        except:
            pass
        images_list.extend(vehicle_data["data"]["vehicle"]["images"])
        for img in images_list:
            images.append(img["url"])
        images = list(set(images))
        temp_data["vehicle_id"] = id
        temp_data["vehicle_url"] = detaild_url
        temp_data["title"] = title
        temp_data["price_msrp"] = price_msrp
        temp_data["current_price"] = current_price
        temp_data["address"] = address
        temp_data["phone_no"] = phone_no
        temp_data["created_at"] = created_at
        temp_data["email"] = email
        temp_data["stock_number"] = stock_number
        temp_data["vin"] = vin
        temp_data["miles"] = miles
        temp_data["length"] = length
        temp_data["height"] = height
        temp_data["width"] = width
        temp_data["engine"] = engine
        if(type == "b"):
            temp_data["gvwr"] = gvwr
            temp_data["hitch_weight"] = hitch_weight
            temp_data["dry_weight"] = dry_weight
        temp_data["fuel_type"] = fuel_type
        temp_data["horsepower"] = horsepower
        temp_data["torque"] = torque
        temp_data["sleeps"] = sleeps
        temp_data["slideouts"] = slideouts
        temp_data["fresh"] = fresh
        temp_data["grey"] = grey
        temp_data["black"] = black
        temp_data["furnance_btu"] = furnance_btu
        temp_data["chassis_brand"] = chassis_brand
        temp_data["water_heater"] = water_heater
        temp_data["driveline_type"] = driveline_type
        temp_data["two_capacity"] = two_capacity
        temp_data["air_conditioning_btu"] = air_conditioning_btu
        temp_data["fuel_capacity"] = fuel_capacity
        temp_data["floorplan_style"] = floorplan_style
        temp_data["description"] = description
        temp_data["feature_list"] = feature_list
        temp_data["images"] = images
        scraped_data.append(temp_data)
    with open(outputfile, 'w') as f:
        json.dump(scraped_data, f, indent=4, ensure_ascii=False)
    pass

def class_a_diesel():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=class%20a&filters[$and][2][fuel_type][$eq]=regular%20diesel&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="https://giantrv.com/inventory/2018-tiffin-breeze-31br-id", outputfile='class_a_diesel.json')
    
def class_a_data():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=class%20a&filters[$and][2][fuel_type][$eq]=Regular%20Gasoline&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="https://giantrv.com/inventory/2023-thor-motor-coach-axis-25.7-tax115-colton-ca-id", outputfile='class_a.json')

def class_b():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=class%20b&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="https://giantrv.com/inventory/2025-midwest-passage-rv-144-mwp002-murrieta-ca-id", outputfile='class_b.json')

def class_c():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=class%20c&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="https://giantrv.com/inventory/2025-coachmen-prism-elite-24fse-fpr017-colton-ca-id", outputfile='class_c.json')

def super_class_c():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=class%20super%20c&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="https://giantrv.com/inventory/2026-thor-motor-coach-omni-trail-s29-tom104-montclair-ca-id", outputfile='super_class_c.json')

# second type of data

def travel_trailers():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=Travel%20Trailer&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="https://giantrv.com/inventory/2025-forest-river-rockwood-geo-pro-g20bh-frw3048-downey-ca-id", outputfile='travel_trailers.json',type="b")

def fifth_wheel():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=Fifth%20Wheel&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="https://giantrv.com/inventory/2025-alliance-rv-avenue-all-access-series-23ml-ave080-downey-ca-id", outputfile='fifth_wheel.json',type="b")

def toy_hauler():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=Travel%20Trailer%20Toy%20Hauler&filters[$and][1][unitClassification][name][$in][1]=Fifth%20Wheel%20Toy%20Hauler&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="http://giantrv.com/inventory/2025-forest-river-stealth-2630sle-fsl2127-colton-ca-id", outputfile='toy_hauler.json',type="b")

def destination():
    extract_data(url = "https://inventory.coasttechnology.org/api/v3/inventory/?filters[$and][0][displayOnWebsite][$eq]=true&filters[$and][1][unitClassification][name][$in][0]=destination%20trailer&sort[0]=lot%3Aasc&sort[1]=condition.name%3Aasc&sort[2]=year%3Aasc&page=2&company[0]=32&withUnitData=0", 
                detail_url="https://giantrv.com/inventory/2026-forest-river-sierra-destination-40duplex-bb55665-city-state-id", outputfile='destinations.json',type="b")
    
print("Extracting Class A Diesel Data")
#class_a_diesel()
print("Extracting Class A Data")
#class_a_data()
print("Extracting Class B Data")
#class_b()
print("Extracting Class C Data")
#class_c()
print("Extracting Super Class C Data")
#super_class_c()
print("Extracting Travel Trailers Data")
#travel_trailers()
print("Extracting Fifth Wheel Data")
#fifth_wheel()
print("Extracting Toy Hauler Data")
#toy_hauler()
print("Extracting Destinations Data")
destination()