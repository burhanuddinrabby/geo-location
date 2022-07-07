import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
number = input("What is your number? : ")
print("Tracking", number + "...")
pepnumber = phonenumbers.parse(number)
locatoin = geocoder.description_for_number(pepnumber, "en")
print(locatoin)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = '57b552e1c8e44e6186694afa3ff4fceb'

geocoder = OpenCageGeocode(key)
query = str(locatoin)
result = geocoder.geocode(query)
print(result)
lat = result[0]['geometry']['lat']
lang = result[0]['geometry']['lng']
print(lat, lang, number)
#[{'annotations': {'DMS': {'lat': "24° 28' 36.94368'' N", 'lng': "90° 17' 36.38868'' E"}, 'MGRS': '46RBN2566909716', 'Maidenhead': 'NL54dl54fl', 'Mercator': {'x': 10051419.907, 'y': 2793935.02}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?relation=184640#map=17/24.47693/90.29344', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/24.47693/90.29344&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=24.47693&mlon=90.29344#map=17/24.47693/90.29344'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh25nxvsmwjxwhscb3y4', 'qibla': 276.9, 'roadinfo': {'drive_on': 'left', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829360, 'astronomical': 1652824320, 'civil': 1652827860, 'nautical': 1652826120}, 'set': {'apparent': 1652790900, 'astronomical': 1652795940, 'civil': 1652792340, 'nautical': 1652794140}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'suffix.riddled.outsmarted'}, 'wikidata': 'Q902'}, 'bounds': {'northeast': {'lat': 26.6382534, 'lng': 92.6802967}, 'southwest': {'lat': 20.3679092, 'lng': 88.007915}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', '_category': 'place', '_type': 'country', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd'}, 'confidence': 1, 'formatted': 'Bangladesh', 'geometry': {'lat': 24.4769288, 'lng': 90.2934413}}, {'annotations': {'DMS': {'lat': "22° 41' 2.20128'' N", 'lng': "91° 47' 20.90040'' E"}, 'MGRS': '46QCL7561509040', 'Maidenhead': 'NL52vq44qd', 'Mercator': {'x': 10217920.211, 'y': 2577369.879}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=554827034#map=17/22.68394/91.78914', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/22.68394/91.78914&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=22.68394&mlon=91.78914#map=17/22.68394/91.78914'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh1309qz9cy9ybst3g2r', 'qibla': 278.97, 'roadinfo': {'drive_on': 'left', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829180, 'astronomical': 1652824200, 'civil': 1652827740, 'nautical': 1652826000}, 'set': {'apparent': 1652790360, 'astronomical': 1652795280, 'civil': 1652791800, 'nautical': 1652793540}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'conducted.airbag.attaching'}}, 'bounds': {'northeast': {'lat': 22.6840541, 'lng': 91.7892902}, 'southwest': {'lat': 22.6838708, 'lng': 91.7890006}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-B'], '_category': 'place', '_type': 'hamlet', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'locality': 'Fatikchhari, Chittagong, Bangladesh', 'state': 'Chattogram Division', 'state_district': 'Chattogram District', 'town': 'Fatikchhari'}, 'confidence': 9, 'formatted': 'Fatikchhari, Chattogram District, Bangladesh', 'geometry': {'lat': 22.6839448, 'lng': 91.789139}}, {'annotations': {'DMS': {'lat': "23° 48' 57.14748'' N", 'lng': "90° 25' 39.43740'' E"}, 'MGRS': '46QBM3792936218', 'Maidenhead': 'NL53ft15ht', 'Mercator': {'x': 10066356.779, 'y': 2713740.043}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=4568162690#map=17/23.81587/90.42762', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/23.81587/90.42762&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=23.81587&mlon=90.42762#map=17/23.81587/90.42762'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh0r3xx3s29xyqmv1229', 'qibla': 277.57, 'roadinfo': {'drive_on': 'left', 'road': 'Road No. 12', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829360, 'astronomical': 1652824380, 'civil': 1652827920, 'nautical': 1652826180}, 'set': {'apparent': 1652790780, 'astronomical': 1652795820, 'civil': 1652792280, 'nautical': 1652794020}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'hourglass.decorated.draining'}}, 'bounds': {'northeast': {'lat': 23.8159243, 'lng': 90.4276715}, 'southwest': {'lat': 23.8158243, 'lng': 90.4275715}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-C', 'BD-13'], '_category': 'education', '_type': 'school', 'city': 'Dhaka', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'house_number': 'Plot-16', 'municipality': 'Dhaka Metropolitan', 'postcode': '1229', 'road': 'Road No. 12', 'school': 'Independent University, Bangladesh', 'state': 'Dhaka Division', 'state_code': 'C', 'state_district': 'Dhaka District', 'suburb': 'Kuril'}, 'confidence': 9, 'formatted': 'Independent University, Bangladesh, Plot-16 Road No. 12, Kuril, Dhaka - 1229, Bangladesh', 'geometry': {'lat': 23.8158743, 'lng': 90.4276215}}, {'annotations': {'DMS': {'lat': "23° 47' 53.25000'' N", 'lng': "90° 21' 13.75848'' E"}, 'MGRS': '46QBM3037134390', 'Maidenhead': 'NL53et21ln', 'Mercator': {'x': 10058141.434, 'y': 2711592.555}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=6512539565#map=17/23.79812/90.35382', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/23.79812/90.35382&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=23.79812&mlon=90.35382#map=17/23.79812/90.35382'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh0r2h3dhsh9kbpctfcr', 'qibla': 277.56, 'roadinfo': {'drive_on': 'left', 'road': 'Mirpur-1 Footover Bridge', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829420, 'astronomical': 1652824380, 'civil': 1652827920, 'nautical': 1652826180}, 'set': {'apparent': 1652790780, 'astronomical': 1652795820, 'civil': 1652792280, 'nautical': 1652794020}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'rooftop.leave.ogre'}}, 'bounds': {'northeast': {'lat': 23.798175, 'lng': 90.3538718}, 'southwest': {'lat': 23.798075, 'lng': 90.3537718}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-C', 'BD-13'], '_category': 'commerce', '_type': 'shop', 'city': 'Dhaka', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'house_number': 'Unnamed Road, Dhaka, Bangladesh', 'municipality': 'Dhaka Metropolitan', 'neighbourhood': 'Kolwala Para', 'postcode': '1216', 'road': 'Mirpur-1 Footover Bridge', 'shop': 'GLOWSIGHT-BD', 'state': 'Dhaka Division', 'state_code': 'C', 'state_district': 'Dhaka District', 'suburb': 'Shah Ali Bagh'}, 'confidence': 9, 'formatted': 'GLOWSIGHT-BD, Unnamed Road, Dhaka, Bangladesh Mirpur-1 Footover Bridge, Shah Ali Bagh, Dhaka - 1216, Bangladesh', 'geometry': {'lat': 23.798125, 'lng': 90.3538218}}, {'annotations': {'DMS': {'lat': "23° 49' 37.74252'' N", 'lng': "90° 21' 49.70700'' E"}, 'MGRS': '46QBM3144837586', 'Maidenhead': 'NL53et38pm', 'Mercator': {'x': 10059253.037, 'y': 2715104.529}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=437540970#map=17/23.82715/90.36381', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/23.82715/90.36381&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=23.82715&mlon=90.36381#map=17/23.82715/90.36381'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh0r838gjqfd317xmnqj', 'qibla': 277.54, 'roadinfo': {'drive_on': 'left', 'road': 'Begum Rokeya Sharani', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829420, 'astronomical': 1652824380, 'civil': 1652827920, 'nautical': 1652826180}, 'set': {'apparent': 1652790780, 'astronomical': 1652795820, 'civil': 1652792280, 'nautical': 1652794020}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'liberated.lawyer.beast'}}, 'bounds': {'northeast': {'lat': 23.8272346, 'lng': 90.3639774}, 'southwest': {'lat': 23.8270669, 'lng': 90.3636376}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-C', 'BD-13'], '_category': 'building', '_type': 'building', 'borough': 'Mirpur 7', 'building': 'BSMR Maritime University, Bangladesh', 'city': 'Dhaka', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'municipality': 'Dhaka Metropolitan', 'postcode': '1216', 'quarter': 'Mirpur 7', 'road': 'Begum Rokeya Sharani', 'state': 'Dhaka Division', 'state_code': 'C', 'state_district': 'Dhaka District'}, 'confidence': 10, 'formatted': 'BSMR Maritime University, Bangladesh, Begum Rokeya Sharani, Dhaka District, Dhaka - 1216, Bangladesh', 'geometry': {'lat': 23.8271507, 'lng': 90.3638075}}, {'annotations': {'DMS': {'lat': "23° 49' 13.05516'' N", 'lng': "90° 22' 15.74688'' E"}, 'MGRS': '46QBM3217136813', 'Maidenhead': 'NL53et46mu', 'Mercator': {'x': 10060058.244, 'y': 2714274.72}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=5312899821#map=17/23.82029/90.37104', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/23.82029/90.37104&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=23.82029&mlon=90.37104#map=17/23.82029/90.37104'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh0r82q5mbkp47fcvc26', 'qibla': 277.55, 'roadinfo': {'drive_on': 'left', 'road': 'Lane 1', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829420, 'astronomical': 1652824380, 'civil': 1652827920, 'nautical': 1652826180}, 'set': {'apparent': 1652790780, 'astronomical': 1652795820, 'civil': 1652792280, 'nautical': 1652794020}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'diverts.owls.scrambles'}}, 'bounds': {'northeast': {'lat': 23.8203431, 'lng': 90.3710908}, 'southwest': {'lat': 23.8202431, 'lng': 90.3709908}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-C', 'BD-13'], '_category': 'commerce', '_type': 'shop', 'borough': 'Mirpur 11', 'city': 'Dhaka', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'municipality': 'Dhaka Metropolitan', 'postcode': '১২১৬', 'quarter': 'Mirpur 11', 'road': 'Lane 1', 'shop': 'Bangladesh', 'state': 'Dhaka Division', 'state_code': 'C', 'state_district': 'Dhaka District', 'suburb': 'Mirpur 11'}, 'confidence': 9, 'formatted': 'Bangladesh, Lane 1, Mirpur 11, Dhaka - ১২১৬', 'geometry': {'lat': 23.8202931, 'lng': 90.3710408}}, {'annotations': {'DMS': {'lat': "23° 43' 30.05688'' N", 'lng': "90° 23' 17.51208'' E"}, 'MGRS': '46QBM3372626225', 'Maidenhead': 'NL53er64oa', 'Mercator': {'x': 10061968.153, 'y': 2702750.202}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=169460935#map=17/23.72502/90.38820', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/23.72502/90.38820&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=23.72502&mlon=90.38820#map=17/23.72502/90.38820'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh0qbz48jxt20mchctqd', 'qibla': 277.64, 'roadinfo': {'drive_on': 'left', 'road': 'Polashi Road', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829420, 'astronomical': 1652824380, 'civil': 1652827920, 'nautical': 1652826180}, 'set': {'apparent': 1652790780, 'astronomical': 1652795820, 'civil': 1652792280, 'nautical': 1652794020}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'stunts.margin.attention'}}, 'bounds': {'northeast': {'lat': 23.7253331, 'lng': 90.38884}, 'southwest': {'lat': 23.7246985, 'lng': 90.3875556}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-C', 'BD-13'], '_category': 'outdoors/recreation', '_type': 'playground', 'city': 'Dhaka', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'municipality': 'Dhaka Metropolitan', 'neighbourhood': 'Polashi', 'playground': "Azimpur Girls' School, Dhaka, Bangladesh", 'postcode': '1211', 'road': 'Polashi Road', 'state': 'Dhaka Division', 'state_code': 'C', 'state_district': 'Dhaka District', 'suburb': 'Azimpur'}, 'confidence': 9, 'formatted': "Azimpur Girls' School, Dhaka, Bangladesh, Polashi Road, Azimpur, Dhaka - 1211, Bangladesh", 'geometry': {'lat': 23.7250158, 'lng': 90.3881978}}, {'annotations': {'DMS': {'lat': "23° 44' 14.08308'' N", 'lng': "90° 24' 23.61564'' E"}, 'MGRS': '46QBM3562427546', 'Maidenhead': 'NL53er86sw', 'Mercator': {'x': 10064012.214, 'y': 2704228.971}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=226516718#map=17/23.73725/90.40656', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/23.73725/90.40656&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=23.73725&mlon=90.40656#map=17/23.73725/90.40656'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh0r130p3x1p9qr002jw', 'qibla': 277.63, 'roadinfo': {'drive_on': 'left', 'road': 'Segunbagicha Road', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829420, 'astronomical': 1652824380, 'civil': 1652827920, 'nautical': 1652826180}, 'set': {'apparent': 1652790780, 'astronomical': 1652795820, 'civil': 1652792280, 'nautical': 1652794020}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'duplicate.presuming.blazing'}}, 'bounds': {'northeast': {'lat': 23.7374202, 'lng': 90.4067421}, 'southwest': {'lat': 23.7368581, 'lng': 90.4063294}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-C', 'BD-13'], '_category': 'building', '_type': 'building', 'building': 'Institution of Diploma Engineers, Bangladesh', 'city': 'Dhaka', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'house_number': '160/A', 'municipality': 'Dhaka Metropolitan', 'postcode': '1000', 'quarter': 'Kakrail', 'road': 'Segunbagicha Road', 'state': 'Dhaka Division', 'state_code': 'C', 'state_district': 'Dhaka District', 'suburb': 'Segunbagicha'}, 'confidence': 10, 'formatted': 'Institution of Diploma Engineers, Bangladesh, 160/A Segunbagicha Road, Segunbagicha, Dhaka - 1000, Bangladesh', 'geometry': {'lat': 23.7372453, 'lng': 90.4065599}}, {'annotations': {'DMS': {'lat': "23° 47' 8.11068'' N", 'lng': "90° 24' 5.15916'' E"}, 'MGRS': '46QBM3519932911', 'Maidenhead': 'NL53es88em', 'Mercator': {'x': 10063441.5, 'y': 2710075.682}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=367289676#map=17/23.78559/90.40143', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/23.78559/90.40143&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=23.78559&mlon=90.40143#map=17/23.78559/90.40143'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'wh0r34h344djqck3c7df', 'qibla': 277.59, 'roadinfo': {'drive_on': 'left', 'road': 'Road No 3/2', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829420, 'astronomical': 1652824380, 'civil': 1652827920, 'nautical': 1652826180}, 'set': {'apparent': 1652790780, 'astronomical': 1652795820, 'civil': 1652792280, 'nautical': 1652794020}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'vessel.elbow.blanked'}}, 'bounds': {'northeast': {'lat': 23.7856696, 'lng': 90.4015888}, 'southwest': {'lat': 23.7854658, 'lng': 90.4013727}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-C', 'BD-13'], '_category': 'building', '_type': 'building', 'building': 'International Union for Conservation of Nature (IUCN) coubtry office, Bangladesh', 'city': 'Dhaka', 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'house_number': '16', 'municipality': 'Dhaka Metropolitan', 'neighbourhood': 'Chairman Bari', 'postcode': '1213', 'road': 'Road No 3/2', 'state': 'Dhaka Division', 'state_code': 'C', 'state_district': 'Dhaka District', 'suburb': 'Gulshan'}, 'confidence': 10, 'formatted': 'International Union for Conservation of Nature (IUCN) coubtry office, Bangladesh, 16 Road No 3/2, Gulshan, Dhaka - 1213, Bangladesh', 'geometry': {'lat': 23.7855863, 'lng': 90.4014331}}, {'annotations': {'DMS': {'lat': "21° 26' 29.41476'' N", 'lng': "91° 58' 15.57516'' E"}, 'MGRS': '46QCJ9336971361', 'Maidenhead': 'NL51xk65mx', 'Mercator': {'x': 10238164.12, 'y': 2428988.932}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=6241319985#map=17/21.44150/91.97099', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/21.44150/91.97099&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=21.44150&mlon=91.97099#map=17/21.44150/91.97099'}, 'UN_M49': {'regions': {'ASIA': '142', 'BD': '050', 'SOUTHERN_ASIA': '034', 'WORLD': '001'}, 'statistical_groupings': ['LDC', 'LEDC']}, 'callingcode': 880, 'currency': {'alternate_symbols': ['Tk'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'BDT', 'iso_numeric': '050', 'name': 'Bangladeshi Taka', 'smallest_denomination': 1, 'subunit': 'Paisa', 'subunit_to_unit': 100, 'symbol': '৳', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇧🇩', 'geohash': 'w5c3uz71z6nfp2212f1g', 'qibla': 280.12, 'roadinfo': {'drive_on': 'left', 'road': 'Sayman Road', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1652829240, 'astronomical': 1652824380, 'civil': 1652827800, 'nautical': 1652826120}, 'set': {'apparent': 1652790180, 'astronomical': 1652795100, 'civil': 1652791620, 'nautical': 1652793300}}, 'timezone': {'name': 'Asia/Dhaka', 'now_in_dst': 0, 'offset_sec': 21600, 'offset_string': '+0600', 'short_name': '+06'}, 'what3words': {'words': 'surprised.ranted.scouts'}}, 'bounds': {'northeast': {'lat': 21.4415541, 'lng': 91.9710431}, 'southwest': {'lat': 21.4414541, 'lng': 91.9709431}}, 'components': {'ISO_3166-1_alpha-2': 'BD', 'ISO_3166-1_alpha-3': 'BGD', 'ISO_3166-2': ['BD-B'], '_category': 'building', '_type': 'building', 'city': "Cox's Bazar", 'continent': 'Asia', 'country': 'Bangladesh', 'country_code': 'bd', 'county': "Cox's Bazar District", 'house_number': '2', 'office': 'International Rescue Committee, Bangladesh', 'postcode': '4700', 'road': 'Sayman Road', 'state': 'Chattogram Division', 'suburb': 'Hotel Motel Zone'}, 'confidence': 10, 'formatted': "International Rescue Committee, Bangladesh, 2 Sayman Road, Hotel Motel Zone, Cox's Bazar - 4700, Bangladesh", 'geometry': {'lat': 21.4415041, 'lng': 91.9709931}}]
#24.4769288 90.2934413

myMap = folium.Map(locatoin = [21.4415041, 91.9709931], zoom_start=9)
folium.Marker([21.4415041, lang], popup=locatoin).add_to(myMap)

myMap.save('myLocation.html')