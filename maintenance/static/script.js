document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const status = this.getAttribute('data-status');

            console.log('Status selecionado:', status); // Verifique se o status está sendo corretamente obtido

            // Mostra todos os cards
            document.querySelectorAll('.card').forEach(card => {
                card.style.display = 'block';
            });

            // Teste de lógica de ocultação
            if (status !== 'todos') {
                document.querySelectorAll('.card').forEach(card => {
                    const cardStatus = card.getAttribute('data-status');
                    console.log('Status do card:', cardStatus); // Verifique se o status do card está correto

                    if (cardStatus !== status) {
                        card.style.display = 'none';
                    }
                });
            }
        });
    });
});
