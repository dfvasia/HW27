from msilib.schema import ListView

from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from HW27 import settings
from user_continued.models import ContinuedUser


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):

    def get(self, request):
        user = User.objects.all()

        paginator = Paginator(user, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        advertisements = []
        for user in page_obj:
            advertisements.append(
                {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    # "role": user.groups.,
                    # "age": user.role,
                    "location": list(map(str, ContinuedUser.user)),
                }
            )

        response = {
            "items": advertisements,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
        }
        return JsonResponse(response, status=200, safe=False)
