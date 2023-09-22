import os
import shutil
from django.shortcuts import render, get_object_or_404
from .models import Animation, Image
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
@login_required
def index(request):
    if request.method == 'POST':
       if 'name' in request.POST:
          user = request.user
          anim = Animation.objects.create(name=request.POST['name'], user=user)
          for img in request.FILES.getlist('imgs'):
              Image.objects.create(animation=anim, image=img)


       else:
         pk = request.POST.get('pk')
         if pk:
            anim = get_object_or_404(Animation, pk=pk)
            if request.user == anim.user:
               anim.delete()
               media_path = os.path.join(settings.MEDIA_ROOT, str(pk))
               if os.path.exists(media_path):
                  shutil.rmtree(media_path)    
               return JsonResponse({'message': 'Animation deleted successfully'})
            else:
                return JsonResponse({'error': 'Unauthorized access'}, status=403)

    anims = Animation.objects.all()
    context = {
        'anims': anims
    }
    return render(request, 'mkgif/index.html', context)


@login_required
def details(request, pk):
    anim = get_object_or_404(Animation, pk=pk)
    images = Image.objects.filter(animation=pk)
    gif_path = f'{anim.pk}/out.gif'    
    context = {
         'anim': anim,
         'images': images,
         'gif_path': gif_path,
        }
    return render(request, 'mkgif/details.html', context)
