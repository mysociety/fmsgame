# coding: utf-8
# GeoRSS.py

# from http://workplace.keizie.net/reference/georss

from PyRSS2Gen import RSSItem, Guid, RSS2, _opt_element

class GeoRSS(RSS2):
    rss_attrs = {
        "version": "2.0",
        "xmlns:geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
        "xmlns:ymaps": "http://api.maps.yahoo.com/Maps/V2/AnnotatedMaps.xsd"
    }

    def publish_extensions(self, handler):
        if hasattr(self, 'geo_lat'):
            _opt_element(handler, "geo:lat", self.geo_lat)
        if hasattr(self, 'geo_long'):
            _opt_element(handler, "geo:long", self.geo_long)

        if hasattr(self, 'ymaps_ZoomLevel'):
            _opt_element(handler, "ymaps:ZoomLevel", self.ymaps_ZoomLevel)
        if hasattr(self, 'ymaps_IntlCode'):
            _opt_element(handler, "ymaps:IntlCode", self.ymaps_IntlCode)
        if hasattr(self, 'ymaps_Groups'):
            _opt_element(handler, "ymaps:Groups", self.ymaps_Groups)

class GeoRSSItem(RSSItem):
    # def __init__(self, *args, geo_lat=None, geo_long=None, **kwargs):
    #     super(GeoRSSItem, self).__init__(*args, **kwargs)
    #     
    #     self.geo_lat = geo_lat
    #     self.geo_long = geo_long
    def __init__(self, geo_lat=None, geo_long=None, *args, **kwargs):
        RSSItem.__init__(self, *args, **kwargs)
        self.geo_lat = geo_lat
        self.geo_long = geo_long
        
    def publish_extensions(self, handler):
        if hasattr(self, 'geo_lat'):
            _opt_element(handler, "geo:lat", self.geo_lat)
        if hasattr(self, 'geo_long'):
            _opt_element(handler, "geo:long", self.geo_long)

        if hasattr(self, 'georss_point'):
            _opt_element(handler, "georss:point", self.georss_point)
        if hasattr(self, 'georss_line'):
            _opt_element(handler, "georss:line", self.georss_line)
        if hasattr(self, 'georss_polygon'):
            _opt_element(handler, "georss:polygon", self.georss_polygon)
