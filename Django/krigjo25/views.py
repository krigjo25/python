from multiprocessing import context
from turtle import title
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from krigjo25.forms import CommentForm
from krigjo25.models import DatabaseProjects, DiscordBots, MiscProjects, BlogComments, BlogPost, BlogCategory

def WebIndex(request):

    #   Initializing the database connection
    dBotRepo = DiscordBots.objects.all().order_by('id')
    mdb = DatabaseProjects.objects.all().order_by('id')
    
    context = {
                'databases':mdb,
                'dBots': dBotRepo,
                
}

    templateName = 'home/index.html'

    return render(request, templateName, context)


def ProjectDetail(request, pk):

    project = DiscordBots.objects.get(pk=pk)

    context = {
                'discBot': project
            }

    templateName = 'home/projectDetail.html'

    return render(request, templateName, context)

#   The blog page
def BlogIndex(request):

    blogCategory = BlogCategory.objects.all()

    context = {

                'Tag':blogCategory,

    }

    templateName = 'blog/blogIndex.html'

    return render(request, templateName, context)

def blogPost(request, category):


    
    post = BlogPost.objects.filter(category__name__contains=category). order_by('-created')

    bots = DiscordBots.objects.all()


    context = {
                
                'tag':category,
                'blogPost':post,
                'DBots':bots,

    }

    templateName = 'blog/blogDetail.html'

    return render(request, templateName, context)



