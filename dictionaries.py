# dictionaries are structure in python which allows us to store information
#  in what are called key value pairs. the key must be unique. we can't duplicate the key word.
month_conversions = {"Jan":"January",    # Jan is key and January is value
                     "Feb": "February",
                      "Mar": "March",
                      "May": "May",
                      "Jun":"June",
                      "Jul": "July",
                      "Sep": "September",
                      "Oct ": "october",
                      "Nov": "November",
                      "Dec": "December"   }
print (month_conversions["Nov"])
print (month_conversions.get("Run") ) # get is if we call with out fun it called none
print (month_conversions.get("Run","not a valid key") )

print ("Jan" in month_conversions.keys() )
print ("March" in month_conversions.keys() )
print ("Jan" in month_conversions.values() )
print ("July" in month_conversions.values() )

print (month_conversions.items() )
print (month_conversions.update({"J":"January"}))
print (month_conversions.items() )
print (month_conversions )


