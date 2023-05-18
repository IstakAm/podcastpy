from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime


def image_validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.jpg', '.png']
    if not ext.lower() in valid_extension:
        raise ValidationError('Unsupported file extension')


def audio_validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.mp3', '.m4a']
    if not ext.lower() in valid_extension:
        raise ValidationError('Unsupported file extension')


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=True, blank=True,
                              validators=[image_validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.username


class Podcast(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    description = RichTextField()
    cover = models.FileField(upload_to='files/podcast_covers/', null=False, blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    audio = models.FileField(upload_to='files/podcast_files/', null=False, blank=False,
                             validators=[audio_validate_file_extension])

    def __str__(self):
        return self.title


class Liking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'podcast')


class Following(models.Model):
    following_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followers')
    followed = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('following_user', 'followed'), )