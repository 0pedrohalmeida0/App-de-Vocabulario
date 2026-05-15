self.addEventListener('activate', (event) => {
    // Quando o app ativa, ele busca a palavra na nossa API
    fetch('/api/palavra/')
        .then(response => response.json())
        .then(data => {
            if (data.termo) {
                self.registration.showNotification('Palavra do Dia: ' + data.termo, {
                    body: 'Significado: ' + data.significado + '\nExemplo: ' + data.exemplo,
                    icon: '/static/core/images/icon-192.png',
                    badge: '/static/core/images/icon-192.png',
                    tag: 'palavra-do-dia',
                    renotify: true
                });
            }
        })
        .catch(err => console.error('Erro ao buscar palavra para notificação:', err));
});