from django.forms import SelectMultiple
from django.utils.datastructures import MultiValueDict

class ArrayFieldSelectMultiple(SelectMultiple):

    def __init__(self, *args, **kwargs):
        self.delimiter = kwargs.pop("delimiter", ",")
        super().__init__(*args, **kwargs)

    def render(self, name, value):
        if isinstance(value, str):
            value = value.split(self.delimiter)
        return super().render(name, value)

    def value_from_datadict(self, data, files, name):
        if isinstance(data, MultiValueDict):
            return self.delimiter.join(data.getlist(name))
        return data.get(name, None)
