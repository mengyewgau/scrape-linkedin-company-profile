def getVertical(items, industry):
    try:  
        items = intro.find_all("div", {'class': 'org-top-card-summary-info-list__info-item'})
        industry.append(items[0].get_text().strip().replace(",", ";"))
    except:
        industry.append("No Industry");
    
    return industry;