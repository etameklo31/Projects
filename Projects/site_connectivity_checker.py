# import urllib2 
# use urllib.request to get the data from the url
# write a function that takes a url and returns a response

import urllib.request as urllib

def main(url):
    print("Checking connectivity... ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you would like checked: ")

main(input_url)