from django.core.exceptions import ValidationError
from django.db import models

from treebeard.mp_tree import MP_Node

from ..settings import api_maxlen_settings as maxlengths 
from ..validators import re_validators, errors

class AnnotableArtefact(models.Model):
    annotations = models.ManyToManyField('Annotation', related_name='+', blank=True)

    class Meta:
        abstract = True

class IdentifiableArtefact(AnnotableArtefact):
    uri = models.URLField('URI', null=True, blank=True)
    id_code = models.CharField('ID', max_length=maxlengths.ID_CODE,
                               validators=[re_validators['IDType']],
                               blank=True)

    class Meta:
        abstract = True
        ordering = ['id_code']
        indexes = [
            models.Index(fields=['id_code']),
        ]

    def __str__(self):
        return self.id_code 

class NameableArtefact(IdentifiableArtefact):
    name = models.CharField(
        max_length=maxlengths.NAME, blank=True,
    )
    description = models.TextField(blank=True)

    class Meta(IdentifiableArtefact.Meta):
        abstract = True
        indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
            models.Index(fields=['name']),
            models.Index(fields=['id_code', 'name']),
        ]

    def __str__(self):
        return '%s - %s' % (self.id_code, self.name)

class Item(NameableArtefact):
    wrapper = models.ForeignKey('MaintainableArtefact', on_delete=models.CASCADE)

    class Meta(NameableArtefact.Meta):
        abstract = True
        indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
            models.Index(fields=['wrapper']),
            models.Index(fields=['wrapper', 'id_code']),
            models.Index(fields=['wrapper', 'name']),
        ]
        unique_together = ('wrapper', 'id_code')

class ItemWithParent(Item, MP_Node):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True)

    class Meta(Item.Meta):
        abstract = True

    def clean(self):
        if self.parent:
            if self.wrapper != self.parent.wrapper:
                raise ValidationError({
                    'parent': errors['parent'],
                })

    def save(self, **kwargs):
        if not self.depth:
            if self.parent_id:
                self.depth = self.parent.depth + 1
                self.parent.add_child(instance=self)
            else:
                self.add_root(instance=self)
            return  #add_root and add_child save as well
        super().save(**kwargs)

class VersionableArtefact(NameableArtefact):
    version = models.CharField(
        max_length=maxlengths.VERSION, 
        validators=[re_validators['VersionType']], 
        default='1.0'
    )
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    class Meta(NameableArtefact.Meta):
        abstract = True
        indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
            models.Index(fields=['id_code', 'version']),
            models.Index(fields=['id_code', 'name', 'version']),
        ]

# class Item(NameableArtefact):
#
#     class Meta(NameableArtefact.Meta):
#         abstract = True
#
# class ItemWithParent(Item, MP_Node):
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
#
#     class Meta(Item.Meta):
#         abstract = True
#
#     def save(self, **kwargs):
#         if not self.depth:
#             if self.parent_id:
#                 self.depth = self.parent.depth + 1
#                 self.parent.add_child(instance=self)
#             else:
#                 self.add_root(instance=self)
#             return  #add_root and add_child save as well
#         super().save(**kwargs)
# from django.core.exceptions import ValidationError
# from django.db import models
#
# from treebeard.mp_tree import MP_Node
#
# from ..settings import api_maxlen_settings 
# from ..validators import re_validators, errors 
#
# class AnnotableArtefact(models.Model):
#     annotations = models.ManyToManyField('Annotation', related_name='+')
#
#     class Meta:
#         abstract = True
#
# class IdentifiableArtefact(AnnotableArtefact):
#     uri = models.URLField('URI', null=True, blank=True)
#     id_code = models.CharField(
#         'ID', max_length=api_maxlen_settings.ID_CODE, 
#         validators=[re_validators['IDType']], 
#         blank=True,
#     )
#
#     class Meta:
#         abstract = True
#         ordering = ['id_code']
#         indexes = [
#             models.Index(fields=['id_code']),
#         ]
#
#     def __str__(self):
#         return self.id_code 
#
# class StructureItem(IdentifiableArtefact):
#
#     class Meta(IdentifiableArtefact.Meta):
#         abstract = True
#         indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
#             models.Index(fields=['wrapper']),
#         ]
#         unique_together = ('wrapper', 'id_code', 'concept')
#
# class NameableArtefact(IdentifiableArtefact):
#     name = models.CharField(
#         max_length=api_maxlen_settings.NAME, blank=True,
#     )
#     description = models.TextField(blank=True)
#
#     class Meta(IdentifiableArtefact.Meta):
#         abstract = True
#         indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
#             models.Index(fields=['name']),
#             models.Index(fields=['id_code', 'name']),
#         ]
#
#     def __str__(self):
#         return '%s - %s' % (self.id_code, self.name)
#
# class Item(NameableArtefact):
#
#     class Meta(NameableArtefact.Meta):
#         abstract = True
#         indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
#             models.Index(fields=['wrapper']),
#             models.Index(fields=['wrapper', 'id_code']),
#             models.Index(fields=['wrapper', 'name']),
#         ]
#         unique_together = ('wrapper', 'id_code')
#
#
# class ItemWithParent(Item, MP_Node):
#
#     class Meta(Item.Meta):
#         abstract = True
#
#     def clean(self):
#         if self.parent:
#             if self.wrapper != self.parent.wrapper:
#                 raise ValidationError({
#                     'parent': errors['parent'],
#                 })
#
#     def save(self, **kwargs):
#         if not self.depth:
#             if self.parent_id:
#                 self.depth = self.parent.depth + 1
#                 self.parent.add_child(instance=self)
#             else:
#                 self.add_root(instance=self)
#             return  #add_root and add_child save as well
#         super().save(**kwargs)
#
# class VersionableArtefact(NameableArtefact):
#     version = models.CharField(
#         max_length=api_maxlen_settings.VERSION, 
#         validators=[re_validators['VersionType']], 
#         default='1.0'
#     )
#     valid_from = models.DateTimeField(null=True, blank=True)
#     valid_to = models.DateTimeField(null=True, blank=True)
#
#     class Meta(NameableArtefact.Meta):
#         abstract = True
#         indexes = IdentifiableArtefact.Meta.indexes[:] + [ 
#             models.Index(fields=['id_code', 'version']),
#             models.Index(fields=['id_code', 'name', 'version']),
#         ]
#
#     def __str__(self):
#         return 'id:%s, id_code:%s, version:%s, name:%s' % (self.id_code, self.version, self.name)
