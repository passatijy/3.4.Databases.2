from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tags, Scopes
# user admin, pass admin

'''
class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            data_dict = form.cleaned_data
            for k in data_dict:
                print('form.cleaned_data:', k)
                for n in k:
                    print('something inside:', n)
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода
'''
#@admin.register(Category)
class ScopesInline(admin.TabularInline):
    model = Scopes
#    formset = ScopesInlineFormset
    extra = 0
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopesInline,]
    pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
#   inlines = [ CategoryInline,]
    pass



#admin.site.register(Article, Tags)