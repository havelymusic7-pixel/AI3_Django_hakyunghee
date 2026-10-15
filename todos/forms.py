from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "할 일을 입력해 주세요.", "autofocus": True}
            ),
            "content": forms.Textarea(
                attrs={"rows": 5, "placeholder": "세부 내용을 입력하세요. (선택)"}
            ),
        }
        error_messages = {
            "title": {
                "required": "할 일 제목을 입력해 주세요.",
                "max_length": "제목은 200자 이하로 입력해 주세요.",
            }
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("할 일 제목을 입력해 주세요.")
        return title
