from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    # on_delete=models.CASCADE author가 삭제돨때 관련 다 삭제
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="timeline_photo/%Y/%m/%d")  # 알아서 연월일
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add => 한 번
    update = models.DateTimeField(auto_now=True)  # auto_now => 매번
    cat = models.CharField(max_length=20, null=True, editable=False)
    tag = models.TextField(blank=True, null=True, editable=False)

    def __str__(self):
        return "text: " + self.text

    class Meta:
        ordering = ["-created"]