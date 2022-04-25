import json
from msilib.schema import ListView

from django.contrib.auth.models import User, Group, Permission
from django.core.paginator import Paginator
from django.db.models import Count, Avg
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from HW27 import settings
from user_continued.models import ContinuedUser


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):

    def get(self, request):
        user = User.objects.all()

        self.object_list = self.object_list.order_by("username")

        paginator = Paginator(user, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        advertisements = []

        get_2 = ContinuedUser.objects.all().filter(user=2).values_list("location_id", flat=True)
        print(get_2)

        for user in page_obj:
            advertisements.append(
                {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    # "role": list(User.objects.all().filter(pk=user.id).values_list("user_permissions__group__name", flat=True)),
                    "age": list(ContinuedUser.objects.all().filter(user=user.id).values_list("age", flat=True)),
                    "location": list(ContinuedUser.objects.all().filter(user=user.id).values_list("location__name", flat=True)),
                }
            )

        response = {
            "items": advertisements,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
        }
        return JsonResponse(response, status=200, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse(
            {
                "id": user.id,
                "name": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                # "role": list(User.objects.all().filter(pk=user.id).values_list("user_permissions__group__name", flat=True)),
                "age": list(ContinuedUser.objects.all().filter(user=user.id).values_list("age", flat=True)),
                "location": list(ContinuedUser.objects.all().filter(user=user.id).values_list("location__name", flat=True)),
            }, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ["username", "first_name", "last_name"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
        )
        perm = Permission.objects.get(content_type__app_label='tag', content_type__model='tag', codename='add_tag')
        user.user_permissions.add(perm)

        return JsonResponse(
            {
                "id": user.id,
                "name": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                # "role": list(User.objects.all().filter(pk=user.id).values_list("user_permissions__group__name", flat=True)),
                "age": list(ContinuedUser.objects.all().filter(user=user.id).values_list("age", flat=True)),
                "location": list(ContinuedUser.objects.all().filter(user=user.id).values_list("location__name", flat=True)),
            }, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["username", "first_name", "last_name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        user = self.object
        user.username = user_data["username"]
        user.first_name = user_data["first_name"]
        user.last_name = user_data["last_name"]

        user.save()

        return JsonResponse(
            {
                "id": user.id,
                "name": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                # "role": list(User.objects.all().filter(pk=user.id).values_list("user_permissions__group__name", flat=True)),
                "age": list(ContinuedUser.objects.all().filter(user=user.id).values_list("age", flat=True)),
                "location": list(ContinuedUser.objects.all().filter(user=user.id).values_list("location__name", flat=True)),
            }, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "delete/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "OK"}, status=200)


class UserAdsView(View):
    def get(self, request):
        # user_qs = User.objects.annotate(ads=Count("ads"))
        user_qs = User.objects.annotate(ads=Count('advertisement'))

        paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        users = []

        for user in page_obj:
            users.append(
                {
                    "id": user.id,
                    "name": user.username,
                    "total_ads": user.ads,
                }
            )

        response = {
            "items": users,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
            "avg": user_qs.aggregate(avg=Avg("ads"))["avg"],
        }

        return JsonResponse(response, safe=False)