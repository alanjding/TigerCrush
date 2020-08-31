from lxml import etree

def getLocalStudents():
    # parse out fields we want
    parser = etree.HTMLParser()
    tree = etree.parse('students.html', parser)
    name_and_year = \
        tree.xpath('//li' +
                   '/div[@class="card-body text-left pl-0 pt-1 student-list"]' +
                   '/div[@class="font-weight-bold"]' +
                   '/text()')
    emails = \
        tree.xpath('//li' +
                   '/div[@class="card-body text-left pl-0 pt-1 student-list"]' +
                   '/div/a/text()')

    name = [s.split(" '")[0] for s in name_and_year]
    year = [s.split(" '")[1] for s in name_and_year]
    netid = [email.split("@")[0] for email in emails]

    # construct and return data structure (list of dictionaries)
    if len(name) != len(year) or len(year) != len(netid):
        return

getLocalStudents()