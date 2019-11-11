from django.contrib import admin

from .models import Article, Tags, Scopes
# user admin, pass admin

#@admin.register(Category)
class ScopesInline(admin.TabularInline):
	model = Scopes
	extra = 0
	pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	inlines = [ScopesInline,]
	pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
#	inlines = [ CategoryInline,]
	pass



#admin.site.register(Article, Tags)