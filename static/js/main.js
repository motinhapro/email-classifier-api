document.getElementById('form-email').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const text = document.getElementById('texto-email').value;
    
    if (!text.trim()) {
        alert('Por favor, digite um email!');
        return;
    }
    
    await classificarEmail(text);
});

async function emailClassify(text) {

    // Esconde o resultado antigo
    document.getElementById('resultado').style.display = 'none';

    // Mostrar loading
    document.getElementById('loading').style.display = 'block';

    // Preparar dados para enviar
    const formData = new FormData();
    formData.append('text', text);

    try {

        // Enviar para a api
        const response = await fetch('/classify', {
            method: 'POST',
            body: formData
        });

        // Converte a resposta para JSON
        const res = await response.json();
        
        // Esconde o loading
        document.getElementById('loading').style.display = 'none';

        showResult(res)
    }
    catch (err) {
        document.getElementById('loading').style.display = 'none';
        alert('Erro ao classificar: ' + err.message);
    }
}