import os
from django.conf import settings
import django_rq
def render_animation_task(pk, params):
    from .models import Animation  

    animation = Animation.objects.get(pk=pk)
    path = os.path.join(settings.MEDIA_ROOT, str(pk))
    os.makedirs(path, exist_ok=True)
    output_path = os.path.join(path, "out.gif")

    command = f'ffmpeg -framerate 60 -pattern_type glob -y -i "{path}/*.png" -r 15 -vf ...'  # Your FFmpeg command here
    os.system(command)

    animation.rendered_animation = os.path.relpath(output_path, settings.MEDIA_ROOT)
    animation.save()   


def mk_gif_ffmpeg(params):
    from .models import Animation
    animation = Animation.objects.get(pk=params['pk'])  # Assuming Animation model
    path = os.path.join(settings.MEDIA_ROOT, str(params["pk"]))  # Use MEDIA_ROOT
    os.makedirs(path, exist_ok=True)
    output_path = os.path.join(path, "out.gif")

    command = f'ffmpeg -framerate 60 -pattern_type glob -y -i "{path}/*.png" -r 15 -vf scale=512:-1 "{output_path}"'
    os.system(command)

    # Save the path as a relative URL
    animation.rendered_animation = os.path.relpath(output_path, settings.MEDIA_ROOT)
    animation.save()
