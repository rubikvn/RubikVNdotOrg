import math


class Paginator():
    def __init__(self, object_list, page_limit):
        self.object_list = object_list
        self.page_limit = page_limit
        self.first_page = 1
        self.last_page = math.ceil(len(self.object_list) / self.page_limit)

    def get_page(self, page):
        page = self._clamp(page, self.first_page, self.last_page)
        base_index = self.page_limit * page - 1
        return self.object_list[base_index : base_index + self.page_limit]

    def _clamp(self, value, lower, upper):
        return max(lower, min(value, upper))
