# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class ExtractAirportLinesMinorRoad(FixtureTest):
    def test_runway(self):
        # Way: 10L/28R (22567191)
        self.generate_fixtures(dsl.way(22567191, wkt_loads('LINESTRING (-122.358088713275 37.61392596858659, -122.358901958102 37.61426717648259, -122.359937625793 37.61470167169559, -122.364526040601 37.61662669830989, -122.366946640966 37.61764216837278, -122.368300222436 37.61820998876551, -122.37057502623 37.61916431572698, -122.376343827322 37.62158437478038, -122.380542642791 37.62334579125329, -122.381857866199 37.6238975593993, -122.382513726187 37.62417269486718, -122.383698424384 37.62466967217838, -122.388359512899 37.62662489167929, -122.389586431914 37.6271394969592, -122.389663417534 37.62717179751739, -122.390313168979 37.6274467785734, -122.391579793529 37.62797567847398, -122.392378036491 37.62831048994419, -122.392482959716 37.62835445784928, -122.393372830836 37.62872775712191)'), {
                               u'source': u'openstreetmap.org', u'surface': u'asphalt', u'width': u'61', u'length': u'3618', u'aeroway': u'runway', u'ref': u'10L/28R'}))

        self.assert_has_feature(
            16, 10490, 25366, 'roads',
            {'id': 22567191, 'kind': 'aeroway', 'kind_detail': 'runway'})

    def test_taxiway(self):
        # Way: Q (23718500)
        self.generate_fixtures(dsl.way(23718500, wkt_loads('LINESTRING (-122.383698424384 37.62466967217838, -122.384119285095 37.62479745564298, -122.384430371678 37.62487820955658, -122.384768946708 37.6249431683679, -122.38505056855 37.62498998421209, -122.385420674447 37.62502399327189, -122.385686216445 37.6250302543523, -122.385903518912 37.6250281910418, -122.387880261695 37.62497938305849, -122.388124423789 37.6249431683679, -122.388285312056 37.6248837591615, -122.388435510372 37.62481147196731, -122.388575018736 37.62472232240759, -122.388679133477 37.62462968643889, -122.389004772767 37.62414160254708, -122.38913952006 37.62393982232248, -122.389217314164 37.6238230656025, -122.389373710855 37.62358869781209)'), {
                               u'source': u'openstreetmap.org', u'aeroway': u'taxiway', u'ref': u'Q'}))

        self.assert_has_feature(
            16, 10488, 25365, 'roads',
            {'id': 23718500, 'kind': 'aeroway', 'kind_detail': 'taxiway'})
