# uses the archive.org search API to look for shows within a year the user defined from a number (passed from GUI)
import array
import webScraper
from internetarchive import search_items


def findYear(year_in):
    year_raw = year_in
    year_str = str(year_raw)
    i = 0  # counts the num of shows returned

    year_int = int(year_raw)

    if (year_int >= 1965) and (year_int <= 1995) and year_int != None:  # check the date is valid
        query_str = 'collection:(GratefulDead) AND date:[%s-01-01 TO %s-12-30]' % (year_str, year_str)
        for item in search_items(query_str):  # searches archive.org for identifiers specified by user
            i = i + 1
            stringed_item = str(item)
            stringed_item = stringed_item[16:100]  # cut off unnecessary text
            stringed_item = stringed_item.replace("'}", "")  # strings are immutable. get rid of formatting
            shows_link = "http://archive.org/details/%s" % stringed_item

            webScraper.findTitle(year_int)
            #print(shows_link + "   ")


        print("Found %i shows! start exploring!" % i)

    else:
        print("ERROR: GD ONLY PLAYED FROM 1965 to 1995!! TRY AGAIN")


()