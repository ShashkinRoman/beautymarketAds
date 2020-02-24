from datetime import datetime, timedelta

#
class Weekday():
    # yesterday = ''
    # day_before_yesterday = ''
    def __init__(self):
        self.today_datetime = datetime.now()
        self.yesterday_datetime = self.today_datetime + timedelta(days=-1)
        self.day_before_yesterday_datetime = self.yesterday_datetime + timedelta(days=-1)

    #     переводить из time data в номер дня недели
    def text_day(self, datetime_day):
        number_day = datetime_day.isoweekday()
        if number_day == 1:
            monday = 'Понедельник'
            return monday
        if number_day == 2:
            tuesday = 'Вторник'
            return tuesday
        if number_day == 3:
            wednesday = 'Среда'
            return wednesday
        if number_day == 4:
            thursday = 'Четверг'
            return thursday
        if number_day == 5:
            Friday = 'Пятница'
            return Friday
        if number_day == 6:
            Saturday = 'Суббота'
            return Saturday
        if number_day == 7:
            Sunday = 'Воскресенье'
            return Sunday

    # def yesterday(self, yesterday_datetime):
    #     numb_yesterday = Weekday.number_day(yesterday_datetime)
    #     yesterday = Weekday.correct_yesterday(numb_yesterday)
    #     return yesterday
    #
    # def day_before_yesterday(self):
    #     numb_day_before_yesterday = Weekday.number_day(self.day_before_yesterday())
    #     day_before_yesterday = Weekday.correct_yesterday(numb_day_before_yesterday)
    #     return day_before_yesterday

# def main():
#     weekdays = Weekday()
#     numb_yesterday = weekdays.number_day(weekdays.yesterday_datetime)
#     yesterday = weekdays.correct_yesterday(numb_yesterday)
#     numb_day_before_yesterday = weekdays.number_day(weekdays.day_before_yesterday_datetime)
#     day_before_yesterday = weekdays.correct_yesterday(numb_day_before_yesterday)
#     return yesterday, day_before_yesterday
#
#
# if __name__ == '__main__':
#     main()
