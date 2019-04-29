import xml.etree.ElementTree as ET

# reading the xml object from a file
tree = ET.parse('youtube-feed-example.xml')
root = tree.getroot()

# reading the xml object from a string
with open("youtube-feed-example.xml", "r") as f:
    root = ET.fromstring(f.read())


def getNamespaces():
    # return a mapping from namespace prefix to full name
    ns = dict([node for _, node in ET.iterparse("youtube-feed-example.xml", events=['start-ns'])])
    # ns = dict([node for _, node in ET.iterparse(io.StringIO(string), events=['start-ns'])])
    ns.update({"atom": ns['']})
    return ns


ns = getNamespaces()
# loop through the xml object to get the values
for entry in root.findall("atom:entry", namespaces=ns):
    print(entry.findtext("yt:videoId", namespaces=ns))
