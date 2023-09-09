# caption_app/views.py

from django.shortcuts import render
from .forms import CaptionForm
from .caption import generate_caption  # caption.py에서 캡션 생성 함수 가져오기
from .models import Caption

def caption_generator(request):
    generated_caption = None

    if request.method == 'POST':
        form = CaptionForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            caption = generate_caption(image)
            instance = form.save(commit=False)
            instance.generated_caption = caption
            instance.save()
            generated_caption = caption
    else:
        form = CaptionForm()
    
    captions = Caption.objects.all()
    
    return render(request, 'caption_app/caption_generator.html', {'form': form, 'generated_caption': generated_caption})
