import unittest

from lane import Lane

class TestLane(unittest.TestCase):
    def test_set_lane_number(self):
        lane = Lane()
        lane.set_lane_number(1)
        self.assertEqual(lane.get_lane_number(), 1)

    def test_set_hourly_lane_cost(self):
        lane = Lane()
        lane.set_hourly_lane_cost(10.0)
        self.assertEqual(lane.get_hourly_lane_cost(), 10.0)

    def test_get_hourly_lane_cost(self):
        lane = Lane()
        lane.set_hourly_lane_cost(10.0)
        self.assertEqual(lane.get_hourly_lane_cost(), 10.0)

    def test_get_lane_number(self):
        lane = Lane()
        lane.set_lane_number(1)
        self.assertEqual(lane.get_lane_number(), 1)

    def test_get_total(self):
        lane = Lane()
        lane.set_lane_number(1)
        lane.set_hourly_lane_cost(10.0)
        self.assertEqual(lane.get_total(10.0, 8, 12), 80.0)

if __name__ == '__main__':
    unittest.main()