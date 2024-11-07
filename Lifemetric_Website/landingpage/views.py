from django.shortcuts import render
from django.core.mail import send_mail  # Import necessário para enviar e-mails
from django.conf import settings         # Para acessar configurações de e-mail

def home(request):
    if request.method == 'POST':  # Verifica se o formulário foi enviado
        name = request.POST['name']      # Pega o nome do formulário
        email = request.POST['email']    # Pega o e-mail do formulário
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message'] # Pega a mensagem do formulário

        # Preparando o conteúdo do e-mail
        email_body = (
            f'Nome: {name}\n'
            f'E-mail: {email}\n'
            f'Telefone: {phone}\n'
            f'Assunto: {subject}\n'
            f'Mensagem: {message}'
        )

        # Enviando o e-mail usando o send_mail
        send_mail(
            subject,                # Assunto do e-mail
            email_body,             # Corpo do e-mail
            email,                  # E-mail de quem enviou                            # E-mail de quem enviou
            ['contato@lifemetric.com'],          # E-mail de destino (substitua pelo seu)
            fail_silently=False,                 # Define se deve falhar silenciosamente
        )

    # Retorna a página home com ou sem o formulário preenchido
    return render(request, 'landingpage/home.html')

