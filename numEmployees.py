def getNumEmployees(intro, totalEmployees):
    try:
        totalEmployeesNum = intro.find("span", {'class': "org-top-card-secondary-content__see-all t-normal t-black--light link-without-visited-state link-without-hover-state"})
        totalEmployees.append(totalEmployeesNum.get_text().strip().replace(",",""))
    except:
        totalEmployees.append("No Employee Information");
    return totalEmployees;