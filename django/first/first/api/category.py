from django.views.generic import View
from shop.models import Category
from django.http import HttpResponse
import json


class ItemCategoryView(View):

    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = Category.objects.all()
        data = []
        for category in categories:
            data.append({'name': category.name, 'id': category.id})

        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.create(
            name=data['name']
        )
        category.save()
        return self.ok_status()

    @staticmethod
    def ok_status():
        return HttpResponse(content='ok', status=200, content_type='application/json')

