
import urllib, os

from urllib.request import urlretrieve

myLoc = "C:\\Users\\Nikhil\Desktop\Pics"

key = "&key=AIzaSyDmYlto41CkS1kkXGWqELLJD--4Z8h3TbU" + ""


def GetStreet(Add, SaveLoc):

    base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
    Myurl = base + Add + key
    fi = Add + ".jpg"
    urllib.request.urlretrieve(Myurl, os.path.join(SaveLoc, fi))

Tests = {"230 Harrison Avenue, Harrison, New Jersey 07029",
         "2021 Astom Mill place, charlotte, North Carolina 28273"}


for i in Tests:
    GetStreet(Add= i, SaveLoc=myLoc)



