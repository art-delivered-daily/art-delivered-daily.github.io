import random
import json
import urllib.request
import datetime

def grab_art():
    page_num = random.randrange(1, 10668)
    page_URL = "https://api.artic.edu/api/v1/artworks/?page=" + str(page_num)

    with urllib.request.urlopen(page_URL) as url:
        page_data = json.load(url)

    art_num = random.randrange(1, 12)
    art_ID = page_data["data"][art_num]["id"]
    art_URL = "https://api.artic.edu/api/v1/artworks/" + str(art_ID)
    
    with urllib.request.urlopen(art_URL) as url:
        json_data = json.load(url)

    return json_data
    
current_date = datetime.datetime.now()
current_date_string = str(current_date.year) + "-" + current_date.strftime('%m') + "-" + current_date.strftime('%d')
day_of_week = current_date.strftime("%A")
month_name = current_date.strftime("%B")
day_num = current_date.day

if day_num % 11 == 0:
    exclude_list = ['Print']
elif day_num % 8 == 0:
    exclude_list = ['Decorative Arts', 'Model', 'Mask', 'Architectural fragment', 'Archives (groupings)', 'Vessel', 'Textile', 'Armor', 'Furniture', 'Religious/Ritual Object', 'Furnishings', 'Book', 'Funerary Object', 'Coin', 'Miniature room', 'Ceramics', 'Costume and Accessories', 'Arms']
elif day_num % 5 == 0:
    exclude_list = ['Decorative Arts', 'Model', 'Mask', 'Architectural fragment', 'Archives (groupings)', 'Vessel', 'Textile', 'Armor', 'Furniture', 'Religious/Ritual Object', 'Furnishings', 'Architectural Drawing', 'Book', 'Funerary Object', 'Coin', 'Miniature room', 'Ceramics', 'Costume and Accessories', 'Arms', 'Print', 'Metalwork', 'Design']
else:
    exclude_list = ['Decorative Arts', 'Model', 'Mask', 'Architectural fragment', 'Archives (groupings)', 'Vessel', 'Textile', 'Armor', 'Furniture', 'Religious/Ritual Object', 'Furnishings', 'Architectural Drawing', 'Book', 'Funerary Object', 'Coin', 'Miniature room', 'Ceramics', 'Costume and Accessories', 'Arms', 'Print', 'Photograph', 'Metalwork', 'Design']

start_var = True

while start_var == True or art_imageID == None or art_category == None:
    start_var = False
    json_data = grab_art()
    art_imageID = json_data["data"]["image_id"]
    art_category = json_data["data"]["artwork_type_title"]
    if json_data["data"]["artwork_type_title"] in exclude_list:
        start_var = True

art_ID = json_data["data"]["id"]
art_title = json_data["data"]["title"]
art_date = json_data["data"]["date_display"]
art_creator_display = json_data["data"]["artist_display"]
art_creator = json_data["data"]["artist_title"]
art_medium = json_data["data"]["medium_display"]
art_style = json_data["data"]["style_title"]
art_dimensions = json_data["data"]["dimensions"]
art_description = json_data["data"]["short_description"]
art_alt_text = json_data["data"]["thumbnail"]["alt_text"]
website_URL = "https://www.artic.edu/artworks/" + str(art_ID)

for pixels in [1686, 843, 600, 400, 200]:
    pxl_string = str(pixels)    
    try:
        image_URL = "https://www.artic.edu/iiif/2/" + str(art_imageID) + "/full/" + pxl_string + ",/0/default.jpg"
        urllib.request.urlopen(image_URL)
    except urllib.error.HTTPError as err:
        print(err.code)
    else:
        image_URL = "https://www.artic.edu/iiif/2/" + str(art_imageID) + "/full/" + pxl_string + ",/0/default.jpg"
        break 

blog_title = "Art for " + day_of_week + ", " + month_name + " " + str(current_date.day) + ", " + str(current_date.year)

if art_creator_display == None:
    art_creator_display_break = art_creator
else: 
    art_creator_display_break = art_creator_display.replace("\n", " <br>") 

line1 = "---\n"
line2 = "layout: post\n"
line3 = "title: \"" + str(blog_title) + "\"\n"
line4 = "artTitle: \"" + str(art_title) + "\"\n"
line5 = "pubDate : " + current_date_string + "\n"
line6 = "permalink: /" + current_date_string + "-artic\n"
line7 = "image: \"" + image_URL + "\"\n"
line8 = "category: [\"" + art_category + "\"]\n"
line9 = "altText: \"" + art_alt_text + "\"\n"
if art_style == None:
    line10 = ""
else:
    line10 = "tags: [\"" + art_style.title() +"\"]\n"
if art_creator == None:
    line11 = ""
else:
    line11 = "artist: \"" + art_creator + "\"\n"
line12 = "---\n \n"
line13 =  "<img src='" + image_URL + "' alt='" + art_alt_text + "' style='border-radius=5px'> \n \n" 
line14 = "### " + art_title + "\n \n"
line15 = "**Artist**<br>\n"
if art_creator == None:
    line16 = "Unknown\n \n"
else:
    line16 = art_creator_display_break + "\n \n"
line17 = "**Date**<br>\n"
if art_date == None or art_date == "n.d.":
    line18 = "Exact Date Unknown\n \n"
else:
    line18 = art_date + "\n \n"
if art_medium == None:
    line19 = ""
    line20 = ""
else:
    line19 = "**Medium**<br>\n"
    line20 = art_medium + "\n \n"
if art_dimensions == None:
    line21 = ""
    line22 = ""
else:
    line21 = "**Dimensions**<br>\n"
    line22 = art_dimensions + "\n \n"
line23 = "**Category**<br>\n"
line24 = art_category + "\n \n"
if art_style == None:
    line25 = ""
    line26 = ""
else:
    line25 = "**Style**<br>\n"
    line26 = art_style.title() + "\n \n"
if art_description == None:
    line27 = ""
    line28 = ""
else:
    line27 = "**Description**<br>\n"
    line28 = art_description + "\n \n"

line29 = "**Learn More**<br>\n"
line30 = "To learn more about this artwork, visit [" + website_URL + "](" + website_URL + ")."

fileName = current_date_string + "-artic.md"

f = open(fileName, "a")
f.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18, line19, line20, line21, line22, line23, line24, line25, line26, line27, line28, line29, line30])
f.close()