from django.shortcuts import render
from django.http import HttpResponse
from .models import Item  # Import the Item model to use in views
from django.template import loader
# Create your views here.


def index(request):  # landing page of food app
    # This function handles the request to the landing page of the food app
    item_list = Item.objects.all()  # Fetch all items from the database
    
    # Load the template for the index page
    # template = loader.get_template('food/index.html')
    
    # Render the template with the item list context
    # template always needs to be rendered with a context
    # context is the data that will be passed to the template from database
    context = {
        'item_list': item_list,  # Pass the item list to the template
    }

    return render(request, "food/index.html", context)
    
    # Return the rendered template as an HttpResponse
    # return HttpResponse(template.render(context, request))


# food/item/ will be handled by this function
def item(request):
    return HttpResponse("This is an item view")
