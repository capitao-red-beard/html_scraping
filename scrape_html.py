from bs4 import BeautifulSoup
import re
import locale
import currency_conversion

data_list = []

# read the page HTML from a text file
with open(r'\\lebrun\Data\admin\leo119\text_data\html.txt', 'r') as f:
    html_doc = f.read()

# parse the HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# find the DnB number in the HTML and append to list
dnb_number_data = soup.find_all('li', attrs={'class': 'first'})
dnb_number = dnb_number_data[1].get_text().strip()
data_list.append(dnb_number)

# find the max credit recommendation location in the HTML
max_credit_data = soup.find_all('div', attrs={'class': 'solidBottomBlankLine'})

# find the max credit and currency in the located area
for p in max_credit_data:
    if 'D&B Max Credit Recommendation' in p.get_text():
        max_credit = p.get_text()
        max_credit = max_credit[36:].strip()
        values = re.split(' ', max_credit)
        data_list.append(values[0].replace('.', ''))
        data_list.append(values[1])

# if the currency returned is not euros convert it to euros
if data_list[2] != 'EUR':
    currency_conversion.get_conversion('USD', 1000000)

# convert the returned int into a formatted version
locale.setlocale(locale.LC_ALL, '')
data_list[1] = format(int(data_list[1]), 'n')

# return the complete data list
print(data_list)
