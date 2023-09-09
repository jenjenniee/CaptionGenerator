from django.db import models

class Caption(models.Model):
    image = models.ImageField(upload_to='images/')
    generated_caption = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'caption_app'  # 앱 이름을 명시적으로 지정
