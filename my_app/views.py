from django.shortcuts import render
from django.views.generic import View
from my_app.data import groups, groups_dict


class GroupsView(View):
    def get(self, request):
        return render(request, 'main_page.html', {'groups': groups})


class GroupView(View):
    def get(self, request, id):
        group = groups_dict.get(int(id))
        return render(request, 'group.html', {'group': group})
