from django.forms import ModelChoiceField


class UserModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.role_to_name()
