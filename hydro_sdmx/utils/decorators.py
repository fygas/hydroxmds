from django.db import models

def add_affairs(affairs):
    def wrapper(cls):
        for key in affairs:
            field = models.ForeignKey(key, on_delete=models.CASCADE, null=True, blank=True)
            field.contribute_to_class(cls, key.lower())
        return cls
    return wrapper
