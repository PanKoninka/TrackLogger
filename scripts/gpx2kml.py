#!/usr/bin/python

import sys, xml.parsers.expat, xml.dom

xmlHeader = "<?xml version='1.0' encoding='Utf-8' standalone='yes' ?>"
kmlHeader = "<kml xmlns='http://www.opengis.net/kml/2.2'><Placemark>"
nameTag = "<name>generated by gpx2kml</name>"
kmlFooter = "</Placemark></kml>"

usage = "gpx2kml.py infile outfile"

if len(sys.argv) != 3:
	print usage
	exit(1)

descriptionTag="<description>" + sys.argv[1] + "</description>"

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

parser = xml.parsers.expat.ParserCreate()

def gpxStartElementHandler(name, attrs):
	if name == "trkpt":
		outfile.write(attrs.get("lon") + "," + attrs.get("lat") + ",0\n")

lineStringHeader="<LineString><extrude>1</extrude><tessellate>1</tessellate><altitudeMode>absolute</altitudeMode>"
lineStringFooter="</LineString>"
coordinatesHeader="<coordinates>"
coordinatesFooter="</coordinates>"

outfile.write(xmlHeader + "\n")
outfile.write(kmlHeader + "\n")
outfile.write(nameTag + "\n")
outfile.write(descriptionTag + "\n")
outfile.write(lineStringHeader + "\n")
outfile.write(coordinatesHeader + "\n")

parser.StartElementHandler = gpxStartElementHandler
parser.ParseFile(infile)
infile.close()

outfile.write(coordinatesFooter + "\n")
outfile.write(lineStringFooter + "\n")
outfile.write(kmlFooter + "\n")
outfile.close()