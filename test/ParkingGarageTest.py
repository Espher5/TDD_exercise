import unittest
from unittest.mock import patch

from ParkingGarage import ParkingGarage
from ParkingGarageError import ParkingGarageError

import mock.GPIO as GPIO
from mock.RTC import RTC


class ParkingGarageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.pg = ParkingGarage()

    @patch.object(GPIO, 'input')
    def test_occupancy_spot1_parked(self, mock_input):
        mock_input.return_value = 52
        occ = self.pg.check_occupancy(ParkingGarage.INFRARED_PIN1)
        self.assertTrue(occ)

    @patch.object(GPIO, 'input')
    def test_occupancy_spot1_not_parked(self, mock_input):
        mock_input.return_value = 0
        occ = self.pg.check_occupancy(ParkingGarage.INFRARED_PIN1)
        self.assertFalse(occ)

    def test_occupancy_invalid_pin(self):
        self.assertRaises(ParkingGarageError, self.pg.check_occupancy, -1)

    @patch.object(GPIO, 'input')
    def test_occupied_spots_3(self, mock_input):
        mock_input.side_effect = [20, 56, 89]
        num_occ = self.pg.get_occupied_spots()
        self.assertEqual(3, num_occ)

    @patch.object(GPIO, 'input')
    def test_occupied_spots_0(self, mock_input):
        mock_input.side_effect = [0, 0, 0]
        num_occ = self.pg.get_occupied_spots()
        self.assertEqual(0, num_occ)

    @patch.object(RTC, 'get_current_day')
    @patch.object(RTC, 'get_current_time_string')
    def test_parking_fee_example1(self, mock_rtc_time, mock_rtc_day):
        mock_rtc_time.return_value = '15:24:54'
        mock_rtc_day.return_value = 'MONDAY'
        fee = self.pg.calculate_parking_fee('12:30:15')
        self.assertEqual(7.5, fee)

    @patch.object(RTC, 'get_current_day')
    @patch.object(RTC, 'get_current_time_string')
    def test_parking_fee_example2(self, mock_rtc_time, mock_rtc_day):
        mock_rtc_time.return_value = '18:12:28'
        mock_rtc_day.return_value = 'SATURDAY'
        fee = self.pg.calculate_parking_fee('10:15:08')
        self.assertEqual(25, fee)

    @patch.object(RTC, 'get_current_day')
    @patch.object(RTC, 'get_current_time_string')
    def test_parking_fee_example3(self, mock_rtc_time, mock_rtc_day):
        mock_rtc_time.return_value = '11:20:28'
        mock_rtc_day.return_value = 'MONDAY'
        fee = self.pg.calculate_parking_fee('10:15:08')
        self.assertEqual(5, fee)