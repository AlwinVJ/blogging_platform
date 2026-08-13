from .models import Category
from about_social.models import SocialMedia

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_media(request):
    social_medias = SocialMedia.objects.all()
    return dict(social_medias=social_medias)