from bs4 import BeautifulSoup

#open new file, read only
with open("home.html", "r") as html_file:
    content = html_file.read()

    #prints the exact content of html file
    #print(content)

    soup = BeautifulSoup(content, "lxml")
    #another way to print
    #print(soup.prettify())

    #find returns first element then stops looking
    #tags = soup.find("h5")
    #print(tags)

    #find all tags and print their text
    #courses_html_tags = soup.find_all("h5")
    #for course in courses_html_tags:
        #print(course.text)
    
    #need to use _ since class is already keyword in python
    course_cards = soup.find_all("div", class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] #split changes string to list, [-1] accesses last item

        print(f"{course_name} costs {course_price}") # f string: f"{put var to display here}"
        




