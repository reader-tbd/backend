from django.contrib import admin

from apps.core.admin_mixins import AuthorLinkMixin, ImagePreviewMixin
from apps.readmanga_parser.models import Author, Genre, Manga, Translator
import easy


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin, AuthorLinkMixin, ImagePreviewMixin):
    search_fields = ("name",)
    list_display = (
        "name",
        "get_image",
        "status",
        "year",
        "genres_list",
        "genres_list",
        "screenwriters_list",
        "illustrators_list",
        "author_link"
    )
    list_filter = ("categories",)

    @easy.smart(short_description='Genres')
    def genres_list(self, obj):
        return ",\n".join([g.name for g in obj.genres.all()])

    @easy.smart(short_description='Screenwriters')
    def screenwriters_list(self, obj):
        return ",\n".join([s.name for s in obj.screenwriters.all()])

    @easy.smart(short_description='Illustrators')
    def illustrators_list(self, obj):
        return ",\n".join([i.name for i in obj.illustrators.all()])

    @easy.smart(short_description='Author', admin_order_field="author__name")
    def author_link(self, obj) -> str:
        return (
            format_html(f"<a href='{obj.author.get_admin_url()}'>{obj.author.name}</a>")
            if obj.author
            else "-"
        )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
