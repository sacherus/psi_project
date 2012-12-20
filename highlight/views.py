from pygments import (highlight )
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.lexers import (get_lexer_by_name )
from highlight.forms import CodeForm
from highlight.models import Code
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import  render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def addSidebarToContext(request, context):
    context['codes'] = Code.objects.filter(owner=request.user).order_by('lang')
    return context


@login_required
def createCode(request):
    if request.method == 'POST': # If the form has been submitted...

        form = CodeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data

            data = form.cleaned_data
            language = data['lang']
            code = data['snippet']
            fileName = data['name']
            fileNameEncoded = fileName.encode('ascii', 'ignore')
            userName=request.user.username
            user = User.objects.get(username__exact=userName)
            languageFromList = language.encode('ascii', 'ignore').lower()
            lexer = get_lexer_by_name(languageFromList, stripall=True)
            colorized_code = highlight(code, lexer, HtmlFormatter(linenos=True, cssclass="source", style="colorful"))
            record = Code(lang=language, snippet=colorized_code, name=fileNameEncoded, owner=user)
            record.save()
            path = default_storage.save("highlight/static/"+userName+"/"+fileNameEncoded, ContentFile(code))

            return redirect(record)
    else:
        form = CodeForm() # An unbound form

    context = {'form': form}
    addSidebarToContext(request, context)
    return render(request, 'highlight/highlight.html', context)

@login_required
def show(request, user_name, code_name):
    user = User.objects.get(username__exact=user_name)
    code = get_object_or_404(Code, name=code_name, owner=user)
    context = {'code': code, 'user': user}
    addSidebarToContext(request, context)
    return render(request, 'highlight/show.html', context)
