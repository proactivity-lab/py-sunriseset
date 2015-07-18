import unittest

from sunriseset import sun_time, convert_time, ZENITH_OFFICIAL, ZENITH_CIVIL, ZENITH_NAUTICAL, ZENITH_ASTRONOMICAL

class SunriseSunsetTest(unittest.TestCase):

    def test_zenith(self):
        print
        for zenith in [ZENITH_OFFICIAL, ZENITH_CIVIL, ZENITH_NAUTICAL, ZENITH_ASTRONOMICAL]:
            print "----------------------------------------------------------------------"
            print "zenith %f" % (zenith)
            srise = sun_time(zenith, True, 2015, 7, 18, 24.7453, 59.4372, 3)
            sset = sun_time(zenith, False, 2015, 7, 18, 24.7453, 59.4372, 3)
            print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

    def test_rovaniemi(self):
        print
        print "Rovaniemi 66.5014N, 25.7347E -----------------------------------------"
        srise = sun_time(ZENITH_OFFICIAL, True, 2013, 7, 6, 25.7347, 66.5014, 3)
        sset = sun_time(ZENITH_OFFICIAL, False, 2013, 7, 6, 25.7347, 66.5014, 3)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)
        srise = sun_time(ZENITH_OFFICIAL, True, 2013, 7, 7, 25.7347, 66.5014, 3)
        sset = sun_time(ZENITH_OFFICIAL, False, 2013, 7, 7, 25.7347, 66.5014, 3)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)
        srise = sun_time(ZENITH_OFFICIAL, True, 2013, 7, 8, 25.7347, 66.5014, 3)
        sset = sun_time(ZENITH_OFFICIAL, False, 2013, 7, 8, 25.7347, 66.5014, 3)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

    def test_janmayen(self):
        print
        print "Jan Mayen 70.9833N, 7.5333E ------------------------------------------"
        srise = sun_time(ZENITH_OFFICIAL, True, 2015, 8, 1, 7.5333, 70.9833, 0)
        sset = sun_time(ZENITH_OFFICIAL, False, 2015, 8, 1, 7.5333, 70.9833, 0)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)
        srise = sun_time(ZENITH_OFFICIAL, True, 2015, 7, 31, 7.5333, 70.9833, 0)
        sset = sun_time(ZENITH_OFFICIAL, False, 2015, 7, 31, 7.5333, 70.9833, 0)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

    def test_husavik(self):
        print
        print "Husavik 66.0500N, 17.3167E -------------------------------------------"
        # 2015-06-02  sunrise 02:17, no sunset
        srise = sun_time(ZENITH_OFFICIAL, True, 2015, 6, 2, 17.3167, 66.0500, 0)
        sset = sun_time(ZENITH_OFFICIAL, False, 2015, 6, 2, 17.3167, 66.0500, 0)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)
        srise = sun_time(ZENITH_OFFICIAL, True, 2015, 6, 3, 17.3167, 66.0500, 0)
        sset = sun_time(ZENITH_OFFICIAL, False, 2015, 6, 3, 17.3167, 66.0500, 0)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)
