from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class FooFilter(DjangoFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)

        if filter_class:
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset
class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.get_queryset.get('StationName', 'StationCode'):
            return ['StationName', 'StationCode']
        return super(CustomSearchFilter, self).get_search_fields(view, request)