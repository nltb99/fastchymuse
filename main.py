import requests
import base64
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("-i",'--image', required=True, help="define the path to image desire to upload")
parser.add_argument("-n",'--name', required=False, help="define the name of the image")
parser.add_argument("-e",'--expiration', required=False, help='define the expiration time')
args = parser.parse_args()

if args.image.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
    with open(args.image,'rb') as imagefile:base64_image = base64.b64encode(imagefile.read())
    url='\x68\x74\x74\x70\x73\x3A\x2F\x2F\x61\x70\x69\x2E\x69\x6D\x67\x62\x62\x2E\x63\x6F\x6D\x2F\x31\x2F\x75\x70\x6C\x6F\x61\x64'
    API_KEY='\x63\x62\x33\x64\x63\x38\x63\x37\x63\x64\x36\x36\x64\x34\x39\x64\x30\x34\x33\x62\x61\x32\x38\x33\x63\x34\x35\x62\x30\x38\x37\x30'
    data={
        '\x6B\x65\x79': API_KEY,
        '\x69\x6D\x61\x67\x65': base64_image,
        '\x6E\x61\x6D\x65': args.name,
        '\x65\x78\x70\x69\x72\x61\x74\x69\x6F\x6E':args.expiration,
    }
    print("Uploading...")
    r=requests.post(url,data=data)
    data=r.json()
    table_obj={
        "id": data["data"]["id"],
        "title": data["data"]["title"],
        "url": data["data"]["url"],
        "expiration": data["data"]["expiration"]
    }
    if data["status"]>=300:
        print("Cannot upload image")
    else:
        print("Success!!!")
    table = [["id",table_obj["id"]],["title",table_obj["title"]],
          ["url",table_obj["url"]],["expiration",table_obj["expiration"]]]
    print(tabulate(table))
else:
    print("Invalid image format!")
