#!/usr/bin/python
"""
Content:	checkRobots: Checking the HTTP response Codes of robots.txt entries
Author: 	Florian Hansemann | @HanseSecure | https://hansesecure.de
Date: 		06/2018

Usage:		python checkRobots.py -u http://hansesecure.de/robots.txt
"""
import requests, optparse, signal

def start(url):
    if "robots.txt" in url:
        content = (requests.get(url)).text
    else:
        url = url+"/robots.txt"
        content = (requests.get(url)).text

    i = 0
    url_snippets = []
    url_list = []
    url_200 = []
    for item in content.split():
        if item == "Disallow:":
            url_snippets.append(content.split()[i+1])
            i = i + 1
        else:
            i = i + 1
    for url_snippet in url_snippets:
        url_list.append(url[:-11]+url_snippet)
    print("\n\nNo HTTP 200 OK URLs:\n")
    for test in url_list:
        r = requests.get(test)
        code = r.status_code
        if code == 200:
            url_200.append(test)
        else:
            print(str(code) + " URL: " + test)
    print("\nHTTP 200 OK URLs:\n")
    for item in url_200:
        print("200 URL: "+item)


def main():
    parser = optparse.OptionParser('checkRobots.py -u <URL>')
    parser.add_option('-u', dest='url', type='string', help='specify URL')
    (options, args) = parser.parse_args()
    url = options.url
    if url == None:
        print(parser.usage)
        exit(0)
    else:
        start(url)




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("\n\nNo time? ;-)")