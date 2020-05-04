import xml.dom.minidom as xml

parse = xml.parse("xml file path")

print(parse.nodeName)
print(parse.getElementsByTagName("html"))


