import math


class Paginator():
    def __init__(self, object_list, page_limit):
        self.object_list = object_list
        if page_limit.isdigit():
            self.page_limit = max(1, int(page_limit))
        else:
            self.page_limit = 1
        self.first_page = 1
        self.last_page = math.ceil(len(self.object_list) / self.page_limit)

    def get_page(self, page):
        if not page.isdigit():
            return []
        else:
            page = self._clamp(int(page), self.first_page, self.last_page)
            base_index = self.page_limit * (page - 1)

            return self.object_list[base_index : base_index + self.page_limit]

    def get_last_page(self):
        return self.last_page

    def _clamp(self, value, lower, upper):
        return max(lower, min(value, upper))
