// Validação básica de formulário
const form = document.querySelector('.signup-section form');

form.addEventListener('submit', function(event) {
    const name = form.querySelector('input[name="name"]').value;
    const email = form.querySelector('input[name="email"]').value;
    const phone = form.querySelector('input[name="phone"]').value;
    const subject = form.querySelector('input[name="subject"]').value;
    const message = form.querySelector('textarea[name="message"]').value;

    if (!name || !email || !phone || !subject || !message) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        event.preventDefault();  // Impede o envio do formulário
    }
});
