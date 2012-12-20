from django.db import models
from django.contrib.auth.models import User

class Code(models.Model):

    LANG =(
        ('bash','BASH'),
        ('c','C'),
        ('c++','C++'),
        ('c#','C#'),
        ('html','HTML'),
        ('java','JAVA'),
        ('matlab','MATLAB'),
        ('perl','PERL'),
        ('php','PHP'),
        ('python','PYTHON'),
        ('ruby','RUBY'),
        ('scheme','SCHEME'), 
        ('scilab','SCILAB')
    )

    lang = models.CharField(max_length=10, choices=LANG, verbose_name="Language")
    snippet  = models.TextField(verbose_name="Your code here")
    name = models.CharField(max_length=20, verbose_name="Save as", unique=True)
    owner = models.ForeignKey(User)
    
    def get_absolute_url(self):
        #return "/static/%s/%s" %(self.owner.username, self.name)
        return "/codes/%s/%s" %(self.owner.username, self.name)

    def get_file_url(self):
        #return "/static/%s/%s" %(self.owner.username, self.name)
            return "%s/%s" %(self.owner.username, self.name)