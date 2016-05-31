import unittest

from sunriseset import sun_time, convert_time, ZENITH_OFFICIAL, ZENITH_CIVIL, ZENITH_NAUTICAL, ZENITH_ASTRONOMICAL


class SunriseSunsetTest(unittest.TestCase):

    def test_tallinn(self):
        print
        print "Tallinn -----------------------------------------"
        # 59.433900 24.754900
        year = 2016
        srise = sun_time(ZENITH_OFFICIAL, True, year, 2, 17, 24.754900, 59.433900, 3)
        sset = sun_time(ZENITH_OFFICIAL, False, year, 2, 17, 24.754900, 59.433900, 3)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)
        srise = sun_time(ZENITH_OFFICIAL, True, year, 2, 17, 24.754900, 59.433900, 0)
        sset = sun_time(ZENITH_OFFICIAL, False, year, 2, 17, 24.754900, 59.433900, 0)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

        srise = sun_time(ZENITH_OFFICIAL, True, year, 2, 17, 59.433900, 24.754900, 0)
        sset = sun_time(ZENITH_OFFICIAL, False, year, 2, 17, 59.433900, 24.754900, 0)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

        srise = sun_time(ZENITH_OFFICIAL, True, 2016, 3, 17, 24.754900, 59.433900, 0)
        sset = sun_time(ZENITH_OFFICIAL, False, 2016, 3, 17, 24.754900, 59.433900, 0)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

    def test_2016(self):
        print
        print "Tallinn 2016 -----------------------------------"
        # 59.433900 24.754900
        year = 2016
        srise = sun_time(ZENITH_OFFICIAL, True, year, 3, 29, 24.754900, 59.433900, 3)
        sset = sun_time(ZENITH_OFFICIAL, False, year, 3, 29, 24.754900, 59.433900, 3)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

        srise = sun_time(ZENITH_OFFICIAL, True, year, 3, 30, 24.754900, 59.433900, 3)
        sset = sun_time(ZENITH_OFFICIAL, False, year, 3, 30, 24.754900, 59.433900, 3)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

        srise = sun_time(ZENITH_OFFICIAL, True, year, 3, 31, 24.754900, 59.433900, 3)
        sset = sun_time(ZENITH_OFFICIAL, False, year, 3, 31, 24.754900, 59.433900, 3)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)

        srise = sun_time(ZENITH_OFFICIAL, True, year, 4, 1, 24.754900, 59.433900, 3)
        sset = sun_time(ZENITH_OFFICIAL, False, year, 4, 1, 24.754900, 59.433900, 3)
        print "Sunrise %s(%.6f), sunset %s(%.6f)" % (convert_time(srise), srise, convert_time(sset), sset)
