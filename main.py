import xml.etree.ElementTree as ET
import requests
import wget;
import subprocess
import os;

r = requests.get('http://miniature-calendar.com/feed/');
root = ET.fromstring(r.content);
items = root.find('channel/item');
ns = {'content': 'http://purl.org/rss/1.0/modules/content/'}
content = items.find('content:encoded', ns).text;
i = content.rfind('>')+1;
content = content[:i];
html = ET.fromstring(content);
img = html.find('img');
src = img.attrib.get('src');
i = src.rfind('-');
src = src[:i] + '.jpg';
print src
filename = 'todays-img.jpg'
if os.path.exists(filename):
        os.remove(filename)
wget.download(src, filename);
with open('./set-desktop.sh', 'r') as appleScriptFile:
    appleScript = appleScriptFile.read();
    subprocess.Popen(appleScript, shell=True);
