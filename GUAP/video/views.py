from django.shortcuts import render, get_object_or_404
from .models import Video
from django.http import StreamingHttpResponse
from django.http import HttpResponse
from .services import open_file


def video(request):
    vid = Video.objects.order_by('-create_at')[:3]
    return render(request, 'video/video_home.html', {'video': vid})


def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    return render(request, "main/video.html", {"video": _video})

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response