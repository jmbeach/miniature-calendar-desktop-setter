import xml.etree.ElementTree as ET
import requests
import wget;
import os
import re

r = requests.get('http://miniature-calendar.com/feed/');
root = ET.fromstring(r.content);
items = root.find('channel/item');
ns = {'content': 'http://purl.org/rss/1.0/modules/content/'}
content = items.find('content:encoded', ns).text
content = '<root>{content}<root>'.format(content=content)

# remove non-ascii chars
src = re.findall(r'srcset=\"([^ ]+)', content)[0]
filename = 'todays-img.jpg'
if os.path.exists(filename):
        os.remove(filename)
wget.download(src, filename);
with open('./set-desktop.sh', 'r') as appleScriptFile:
    appleScript = appleScriptFile.read();
    subprocess.Popen(appleScript, shell=True);
