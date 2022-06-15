def getCountry(items, country):
    try:
        country.append(items[1].get_text().strip().replace(",", ";"))
    except:
        country.append("No Country");
    
    return country;