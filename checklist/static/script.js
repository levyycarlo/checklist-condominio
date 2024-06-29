document.addEventListener('DOMContentLoaded', () => {
    const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');
    const menuBar = document.querySelector('#content nav .bx.bx-menu');
    const sidebar = document.getElementById('sidebar');
    const switchMode = document.getElementById('switch-mode');
    const todoItems = document.querySelectorAll('.todo-list li');

    // Alterna a classe ativa para os itens do menu lateral
    allSideMenu.forEach(item => {
        const li = item.parentElement;
        item.addEventListener('click', function () {
            allSideMenu.forEach(i => {
                i.parentElement.classList.remove('active');
            });
            li.classList.add('active');
        });
    });

    // Event listener para toggle do menu lateral
    menuBar.addEventListener('click', function () {
        sidebar.classList.toggle('show'); // Altere para a classe que controla a exibição do sidebar
    });

    // Alternância do modo escuro
    switchMode.addEventListener('change', function () {
        document.body.classList.toggle('dark-mode'); // Altere para a classe que alterna o modo escuro
    });

    // Alterna a conclusão de itens da lista de tarefas (exemplo)
    todoItems.forEach(item => {
        item.addEventListener('click', function () {
            item.classList.toggle('completed');
        });
    });

    // Manipula o redimensionamento da janela
    window.addEventListener('resize', function () {
        if (window.innerWidth < 768) {
            sidebar.classList.add('hide'); // Adicione a classe que oculta o sidebar em telas menores
        } else {
            sidebar.classList.remove('hide');
        }
    });

    // Verificação inicial do redimensionamento
    if (window.innerWidth < 768) {
        sidebar.classList.add('hide');
    }
});



//MÁSCARA DE CPF

