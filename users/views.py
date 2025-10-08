from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.contrib.auth import login
from django.conf import settings
from .forms import CustomUserCreationForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        self.send_welcome_email(user.email)
        return response

    def send_welcome_email(self, user_email):
        try:
            subject = 'Добро пожаловать в Sky Auto!'
            message = f'''
            Благодарим за регистрацию в нашем сервисе Sky Auto!

            Теперь вы можете:
            - Просматривать полные описания товаров
            - Добавлять новые товары в каталог
            - Редактировать и удалять товары

            С уважением,
            Команда Sky Auto
            '''
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user_email]

            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False
            )
            print(f"Email отправлен на: {user_email}")
        except Exception as e:
            print(f"Ошибка отправки email: {e}")