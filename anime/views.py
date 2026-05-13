from django.shortcuts import render,redirect
from .models import Anime_List
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



def Home(request):
    return render(request, "home.html",{})

@login_required
def create_new(request):
    edit_item = None
    edit_id = request.GET.get("edit")

    if edit_id:
        edit_item = get_object_or_404(Anime_List, id=edit_id, owner=request.user)
    if request.method == "POST":
        anime_name = request.POST.get("post")  #to get the data from the form to store in the db name of the html field
        edit_id = request.POST.get("edit_id")

        if edit_id:
            item = get_object_or_404(Anime_List, id=edit_id, owner=request.user)
            item.title = anime_name
            item.save()
            messages.success(request,message="Data Updated Successfully!")
            return redirect("/edit/")
        elif anime_name:
            Anime_List.objects.create(title=anime_name,is_completed=False,owner=request.user )
            messages.success(request,message="Data Added Successfully!")
            return redirect("/edit/")

    data = Anime_List.objects.filter(owner=request.user) #we have written this in the botton because if we use it on top then the list will display the values even after deleted because list is retrieved before deletion
    # print(request.POST)
    return render(request,"create.html",
    {"data":data,"edit_item":edit_item})

@login_required

def edit(request):
    # Get the edit_id from GET parameters
    edit_id = request.GET.get("edit")
    
    # Handle POST requests (deletions)
    if request.method == "POST":
        delete_item = request.POST.get("delete_id")             
        if delete_item:
            get_object_or_404(Anime_List, id=delete_item, owner=request.user).delete()
            messages.success(request,message="Data Deleted Successfully!")
        return redirect("/edit/")  # Redirect back to edit page after deletion
    
    # For GET requests - redirect to home with edit parameter
    if edit_id:
        return redirect(f"/?edit={edit_id}")
    
    # If no edit_id, just show the edit page with all items
    data = Anime_List.objects.filter(owner=request.user)
    paginator = Paginator(data, 4)  #the paginator takes all data and shows how many entries you want to show from that data
    page = request.GET.get("page")  #this "page" is what we will see in the url 


    page_obj = paginator.get_page(page)
    context = {
        "data": data,
        'page_obj':page_obj,
    }

    return render(request, "edit.html", context)

@login_required

def delete(request):
    title_name = get_object_or_404(Anime_List, id=delete_id, owner=request.user)
    title_name.delete()
    messages.success(request, f"{title_name} is deleted successfully")


@login_required

def animelist(request):
    anime_name = request.POST.get("post")  #to get the data from the form to store in the db name of the html field
    data = Anime_List.objects.filter(owner=request.user)

    paginator = Paginator(data, 4)  #the paginator takes all data and shows how many entries you want to show from that data
    page = request.GET.get("page")  #this "page" is what we will see in the url 


    page_obj = paginator.get_page(page)
    context = {
        "data": data,
        'page_obj':page_obj,
    }
    return render(request,"animelist.html",context)
    
    #"data" is the name which is used in the template and the other data is the data set of all the values present in the database which is being passed to the template to be rendered on the webpage

@login_required

def complete_task(request,complete_id):
   
    task = get_object_or_404(Anime_List,id=complete_id,owner=request.user)
    task.is_completed=True
    task.save()
    messages.success(request, "Task updated to completed successfully!!")
    return redirect("animelist")

@login_required


def pending_task(request,pending_id):
    
    task = get_object_or_404(Anime_List, id=pending_id, owner=request.user)
    task.is_completed=False
    task.save()
    messages.success(request, "Task updated to Pending successfully!!")
    return redirect("animelist")



    







































# # Create your views here.
# from django.http import HttpResponse
# from .models import anime

# def index(request):
#     edit_post = None

#     edit_id = request.GET.get("edit")
#     if edit_id:
#         edit_post = anime.objects.get(id=edit_id)


#     if request.method == 'POST':        

#         delete_id = request.POST.get("delete_id")
#         edit_id = request.POST.get('edit_id')
#         title = request.POST.get("title")

#         #DELETE Logic
#         if delete_id:
#             anime.objects.get(id=delete_id).delete()
#             return redirect("/")

#         #EDIT Logic
#         if edit_id and edit_id.strip():
#             post = anime.objects.get(id=edit_id)
#             post.title = title
#             post.save()
#             return redirect("/")

#         #CREATE Logic
#         if title:
#             anime.objects.create(title=title)
#             return redirect("/")  #this is to avoid duplicate submission otherwise every time we reload the same post get added again and again

#     posts = anime.objects.all()
#     return render(request , "index.html",
#      {'posts':posts,
#         "edit_post":edit_post,
#      })

