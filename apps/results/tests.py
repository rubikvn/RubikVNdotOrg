from django.test import TestCase
from django.urls import reverse

from . import views

import json


class ApiRankingViewTest(TestCase):
    def test_api_access_url(self):
        response = self.client.get("/results/api/ranking")
        self.assertEquals(response.status_code, 200)

    def test_api_access_by_name(self):
        response = self.client.get(reverse("results:api_ranking"))
        self.assertEquals(response.status_code, 200)

    def test_api_get_returns_success(self):
        response = self.client.get("/results/api/ranking")
        results = json.loads(response.content.decode())
        self.assertEquals(results.get("success"), True)

    def test_api_post_returns_error(self):
        response = self.client.post("/results/api/ranking")
        results = json.loads(response.content.decode())
        self.assertEquals(results.get("error"), "Method not supported")

    def test_api_valid_get_params(self):
        pass

    def test_api_invalid_get_params(self):
        pass

    def test_api_pagination(self):
        pass
