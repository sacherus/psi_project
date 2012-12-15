# Create your models here.
from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.v2 import MediaFileContent
from feincms.content.raw.models import RawContent
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.image.models import ImageContent
from feincms.content.file.models import FileContent

Page.register_templates({
	'key': 'base',
    'title': 'Standard template',
    'path': 'base.html',
    'regions': (
        ('main', 'Main content area'),
        ('sidebar', 'Sidebar', 'inherited'),
        ),
    })

Page.create_content_type(RichTextContent)
Page.create_content_type(RawContent)
Page.create_content_type(FileContent)
MediaFileContent.default_create_content_type(Page)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
    ('default', 'Default position'),
    ))


Page.register_extensions('navigation', 'changedate')
