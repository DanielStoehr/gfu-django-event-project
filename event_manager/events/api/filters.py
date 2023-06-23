from sre_constants import CATEGORY_DIGIT

from rest_framework.filters import BaseFilterBackend


class EventFilterBackend(BaseFilterBackend):
    """/api/events?category=Sport"""

    def filter_queryset(self, request, queryset, view):
        category = request.query_params.get("category")
        min_group = request.query_params.get("min_group")

        if category:
            queryset = queryset.filter(category__name=category)

        if min_group:
            queryset = queryset.filter(min_group__gte=int(min_group))
        return queryset

    def get_schema_operation_parameters(self, view):
        # return super().get_schema_operation_parameters(view)
        return [
            {
                "name": "category",
                "required": False,
                "schema": {"type": "str"},
                "in": "query",
            },
            {
                "name": "min_group",
                "required": False,
                "schema": {"type": "int"},
                "in": "query",
            },
        ]
