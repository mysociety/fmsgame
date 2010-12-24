import feedparser

import pprint
pp = pprint.PrettyPrinter(indent=4)

def find_nearby_issues( lat=None, lon=None):    
    fms_rss_url = "http://www.fixmystreet.com/rss/l/" + str(lat) + "/" + str(lon) + '?d=1&state=open'
    data = feedparser.parse( fms_rss_url )

    entries = data['entries']
    issues  = []
    
    for entry in entries:
        # I have a horrible feeling this is due to different versions of feedparser
        # dealing differently with the georss namespace.
        try:
            rss_lat, rss_lon = [float(x) for x in entry['georss_point'].split()]
        except:
            rss_lat, rss_lon = [float(x) for x in entry['point'].split()]
            
        rss_id = int( entry['id'].rsplit( '/', 1 )[1] )
    
        name = entry['title'].rsplit( ',', 1)[0]
    
        issue = {
            'id':   rss_id,
            'name': name,
            'link': entry['link'],
            'lat':  rss_lat,
            'lon':  rss_lon,
            'summary': entry['summary'],
        }
        
        issues.append( issue )

    return issues


# pp.pprint( 
# find_nearby_issues( lat=51.5159573, lon=-0.1223774 )
# )



# http://maps.google.co.uk/maps
# ?f=q
# &source=s_q&hl=en&geocode=
# &q=http:%2F%2Fwww.fixmystreet.com%2Frss%2Fl%2F51.5159573%2F-0.1223774
# &sll=53.800651,-4.064941
# &sspn=16.99462,27.158203
# &ie=UTF8
# &z=13
