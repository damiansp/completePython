import xml.etree.ElementTree as XML


fst = lambda x: x[0]
snd = lambda x: x[1]


# parsing xml
xml_samp = '''
<Placemark>
    <Point>
        <coordinates>-76.33029518659048,37.54901619777347,0</coordinates>
    </Point>
</Placemark>'''


def row_iter_kml(file_obj):
    ns_map = {'ns0': 'http://www.opengis.net/kml/2.2',
              'ns1': 'http://www.google.com/kml/ext/2.2'}
    doc = XML.parse(file_obj)
    return (
        comma_split(coordinates.text)
        for coordinates in doc.findall(
            './ns0:Document/ns0:Folder/ns0:Placemark/ns0:Point/ns0:coordinates',
            ns_map))


def comma_split(txt):
    return txt.split(',')


def pick_lat_lon(lon, lat, alt):
    return lat, lon


def la_lon_kml(row_iter):
    return (pick_lat_lon(*row) for row in row_iter)


# then, e.g.:
with urllib.request.urlopen('file:./Winter%202012-2013.kml') as source:
    v1 = tuple(lat_lon_kml(row_iter_kml(source)))
    print(v1)



# Pairing up items from a sequence
