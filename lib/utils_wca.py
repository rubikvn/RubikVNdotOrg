from apps.results.models.wca.event import FORMAT_TIME, FORMAT_MULTI, FORMAT_NUMBER

class Formatter():
    def __init__(self):
        self.actions = [
            (FORMAT_TIME, self.__format_wca_time),
            (FORMAT_MULTI, self.__format_wca_multi),
            (FORMAT_NUMBER, self.__format_wca_number)
        ]

    def format_wca_result(self, iterable, key_name, eventid, category):
        try:
            for official_events, action in self.actions:
                if eventid in official_events:
                    self.__format = action
                    return self.__format(iterable, key_name, category)
        except Error:
            return None

    def __format_wca_time(self, iterable, key_name, category=None):
        for time in iterable:
            seconds = time[key_name] / 100
            if seconds >= 60:
                time[key_name] = f"{int(seconds/60):02d}:{seconds%60:05.2f}"
            else:
                time[key_name] = f"{seconds:.2f}"
        return iterable

    def __format_wca_multi(self, iterable, key_name, category=None):
        for time in iterable:
            # Decoding WCA notations
            res = time[key_name]
            DD = res // 10000000
            TTTTT = (res // 100) % 100000
            MM = res % 100

            difference = 99 - DD
            seconds = TTTTT
            solved = difference + MM
            attempted = solved + MM

            if seconds == 3600:
                time[key_name] = f"{solved}/{attempted} 1:00:00"
            else:
                time[key_name] = f"{solved}/{attempted} {int(seconds/60):02d}:{seconds%60:02d}"
        return iterable

    def __format_wca_number(self, iterable, key_name, category="single"):
        if category == "single":
            return iterable
        else:
            for num in iterable:
                num[key_name] = f"{num[key_name]/100:05.2f}"
            return iterable
