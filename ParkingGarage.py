import mock.GPIO as GPIO
from mock.RTC import RTC
from ParkingGarageError import ParkingGarageError


class ParkingGarage:
    # Pin number declarations
    INFRARED_PIN1 = 11
    INFRARED_PIN2 = 12
    INFRARED_PIN3 = 13
    RTC_PIN = 15
    SERVO_PIN = 16
    LED_PIN = 18

    def __init__(self):
        """
        Constructor
        """
        pass

    def check_occupancy(self, pin: int) -> bool:
        """
        Checks whether one of the infrared distance sensor detects something in front of it.
        :param pin: The data pin of the sensor that is being checked (e.g., INFRARED_PIN1).
        :return: True if the infrared sensor detects something, False otherwise.
        """
        pass

    def get_occupied_spots(self) -> int:
        """
        Calculates the number of occupied parking spots in the garage.
        :return: The number of occupied spots.
        """
        pass

    def calculate_parking_fee(self, entry_time: str) -> float:
        """
        Uses the RTC to calculate the amount of money to be paid by the customer of the garage
        For each hour spent in the garage, there is a flat cost of 2.50 €;
        additionally, during the weekend (Saturday and Sunday)
        an additional 25% fee is applied to the total of the parking ticket.
        Even when customers do not exceed a full hour, they will still be charged 2.50 €.
        :param entry_time: A string in the format "hh:mm:ss" containing the entry time of a
        vehicle in the garage
        :return: The total amount to be paid by the customer
        """
        pass

    def open_garage_door(self) -> None:
        """
        Opens the garage door using the servo motor
        """
        pass

    def close_garage_door(self) -> None:
        """
        Closes the garage door using the servo motor
        """
        pass

    def turn_light_on(self) -> None:
        """
        Turns on the smart lightbulb
        """
        pass

    def turn_light_off(self) -> None:
        """
        Turns off the smart lightbulb
        """
        pass
