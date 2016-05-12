from response import *

class TenDay(Response):

    def get_day1(response):
        day1 = response['forecast']['simpleforecast']['forecastday'][0]
        date = day1['date']['pretty']
        temp_high = day1['high']['fahrenheit']
        temp_low = day1['low']['fahrenheit']
        conditions = day1['conditions']
        print("\nYour 10 day forecast:")
        print("\nDay 1")
        print("{}".format(date))
        print("Day 1 high: {} degrees".format(temp_high))
        print("Day 1 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")



    def get_day2(response):
        day2 = response['forecast']['simpleforecast']['forecastday'][1]
        date = day2['date']['pretty']
        temp_high = day2['high']['fahrenheit']
        temp_low = day2['low']['fahrenheit']
        conditions = day2['conditions']
        print("Day 2")
        print("{}".format(date))
        print("Day 2 high: {} degrees".format(temp_high))
        print("Day 2 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")



    def get_day3(response):
        day3 = response['forecast']['simpleforecast']['forecastday'][2]
        date = day3['date']['pretty']
        temp_high = day3['high']['fahrenheit']
        temp_low = day3['low']['fahrenheit']
        conditions = day3['conditions']
        print("Day 3")
        print("{}".format(date))
        print("Day 3 high: {} degrees".format(temp_high))
        print("Day 3 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")


    def get_day4(response):
        day4 = response['forecast']['simpleforecast']['forecastday'][3]
        date = day4['date']['pretty']
        temp_high = day4['high']['fahrenheit']
        temp_low = day4['low']['fahrenheit']
        conditions = day4['conditions']
        print("Day 4")
        print("{}".format(date))
        print("Day 4 high: {} degrees".format(temp_high))
        print("Day 4 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")

    def get_day5(response):
        day5 = response['forecast']['simpleforecast']['forecastday'][4]
        date = day5['date']['pretty']
        temp_high = day5['high']['fahrenheit']
        temp_low = day5['low']['fahrenheit']
        conditions = day5['conditions']
        print("Day 5")
        print("{}".format(date))
        print("Day 5 high: {} degrees".format(temp_high))
        print("Day 5 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")

    def get_day6(response):
        day6 = response['forecast']['simpleforecast']['forecastday'][5]
        date = day6['date']['pretty']
        temp_high = day6['high']['fahrenheit']
        temp_low = day6['low']['fahrenheit']
        conditions = day6['conditions']
        print("Day 6")
        print("{}".format(date))
        print("Day 6 high: {} degrees".format(temp_high))
        print("Day 6 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")

    def get_day7(response):
        day7 = response['forecast']['simpleforecast']['forecastday'][6]
        date = day7['date']['pretty']
        temp_high = day7['high']['fahrenheit']
        temp_low = day7['low']['fahrenheit']
        conditions = day7['conditions']
        print("Day 7")
        print("{}".format(date))
        print("Day 7 high: {} degrees".format(temp_high))
        print("Day 7 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")

    def get_day8(response):
        day8 = response['forecast']['simpleforecast']['forecastday'][7]
        date = day8['date']['pretty']
        temp_high = day8['high']['fahrenheit']
        temp_low = day8['low']['fahrenheit']
        conditions = day8['conditions']
        print("Day 8")
        print("{}".format(date))
        print("Day 8 high: {} degrees".format(temp_high))
        print("Day 8 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")

    def get_day9(response):
        day9 = response['forecast']['simpleforecast']['forecastday'][8]
        date = day9['date']['pretty']
        temp_high = day9['high']['fahrenheit']
        temp_low = day9['low']['fahrenheit']
        conditions = day9['conditions']
        print("Day 9")
        print("{}".format(date))
        print("Day 9 high: {} degrees".format(temp_high))
        print("Day 9 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")

    def get_day10(response):
        day10 = response['forecast']['simpleforecast']['forecastday'][9]
        date = day10['date']['pretty']
        temp_high = day10['high']['fahrenheit']
        temp_low = day10['low']['fahrenheit']
        conditions = day10['conditions']
        print("Day 10")
        print("{}".format(date))
        print("Day 10 high: {} degrees".format(temp_high))
        print("Day 10 low: {} degrees".format(temp_low))
        print("Conditions: {}".format(conditions))
        return ("\n")
