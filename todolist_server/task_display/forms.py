from django import forms
from api.models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Layout


class AddTaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        required=False
    )

    importance = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'type': 'range', 'min': 0, 'max': 100}
        )
    )

    urgency = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'type': 'range', 'min': 0, 'max': 100}
        )
    )

    modifier_function = forms.ChoiceField(
        choices=Task.MODIFIER_FUNCTIONS
    )

    m = forms.FloatField(
        required=False,
        label='coefficient'
    )

    exponent = forms.FloatField(
        required=False,
        label='lambda'
    )

    helper = FormHelper()
    helper.form_class = "col z-depth-3"
    helper.add_input(Submit('submit', 'Create', css_class='btn waves-effect waves-light'))
    helper.form_method = 'POST'

    helper.layout = Layout(
        'title',
        'description',
        Div(
            css_id='eisenhower_matrix'
        ),
        Div(
            'importance',
            css_class='range-field',
        ),
        Div(
            'urgency',
            css_class='range-field',
        ),
        'base_importance',
        'due_date',
        'category',
        'modifier_function',
        'm',
        'exponent',
    )

    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'importance',
            'urgency',
            'base_importance',
            'due_date',
            'category',
            'modifier_function',
            'm',
            'exponent'
        )
