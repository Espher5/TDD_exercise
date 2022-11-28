from datetime import datetime


class RTC:
    def __init__(self, RTC_PIN):
        self.pin = RTC_PIN

    @staticmethod
    def get_current_time_string() -> str:
        """
        Retrieves the current time
        :return: The time as a string in the format "hh:mm:ss"
        """
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    @staticmethod
    def get_current_day() -> str:
        """
        Retrieves the current day of the week
        :return: The day as an uppercase string
        """
        days = {
            1: 'MONDAY',
            2: 'TUESDAY',
            3: 'WEDNESDAY',
            4: 'THURSDAY',
            5: 'FRIDAY',
            6: 'SATURDAY',
            7: 'SUNDAY'
        }
        today = datetime.today().weekday()
        return days.get(today + 1)
