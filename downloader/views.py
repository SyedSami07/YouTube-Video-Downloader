import subprocess
from django.http import FileResponse, JsonResponse, HttpResponse
from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure you have a 'home.html' template in your templates folder


def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if not url:
            return JsonResponse({'error': 'No URL provided'}, status=400)
        
        try:
            output_path = "downloaded_video.mp4"
            command = [
                "yt-dlp", "-f", "bestvideo+bestaudio", 
                "--merge-output-format", "mp4", 
                "-o", output_path, url
            ]
            subprocess.run(command, check=True)

            return FileResponse(open(output_path, 'rb'), as_attachment=True, filename="video.mp4")
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def about(request):
    return render(request, 'about.html')
