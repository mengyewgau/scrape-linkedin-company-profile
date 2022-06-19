def getVertical(items, industry):
    try:  
        industry.append(items[0].get_text().strip().replace(",", ";"))
    except:
        industry.append("No Industry");
    
    return industry;