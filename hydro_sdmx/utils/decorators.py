from django.db import models


def add_affairs(affairs):
    def wrapper(cls):
        for affair in affairs:
            if not isinstance(affair, tuple):
                model, related_name, field_name = affair, None, affair.lower()
            else: model, related_name, field_name = affair 
            field = models.ForeignKey(model, on_delete=models.CASCADE, null=True, blank=True, related_name=related_name)
            field.contribute_to_class(cls, field_name)

        return cls

    return wrapper
