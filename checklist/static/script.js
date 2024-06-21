document.addEventListener('DOMContentLoaded', () => {
    // Alterna a classe ativa para os itens do menu lateral
    const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

    allSideMenu.forEach(item => {
        const li = item.parentElement;

        item.addEventListener('click', function () {
            allSideMenu.forEach(i => {
                i.parentElement.classList.remove('active');
            });
            li.classList.add('active');
        });
    });

    // Alterna a visibilidade do menu lateral
    const menuBar = document.querySelector('#content nav .bx.bx-menu');
    const sidebar = document.getElementById('sidebar');

    menuBar.addEventListener('click', function () {
        sidebar.classList.toggle('hide');
    });

    // Funcionalidade de pesquisa
    const searchButton = document.querySelector('#content nav form .search-btn');
    const searchInput = document.querySelector('#content nav form input[type="search"]');
    if (searchButton) {
        searchButton.addEventListener('click', function (e) {
            e.preventDefault();
            alert(`Você pesquisou por: ${searchInput.value}`);
            // Implementar lógica de pesquisa aqui
        });
    }

    // Alternância do modo escuro
    const switchMode = document.getElementById('switch-mode');

    switchMode.addEventListener('change', function () {
        if (switchMode.checked) {
            document.body.classList.add('dark');
        } else {
            document.body.classList.remove('dark');
        }
    });

    // Alterna a conclusão de itens da lista de tarefas
    const todoItems = document.querySelectorAll('.todo-list li');
    todoItems.forEach(item => {
        item.addEventListener('click', function () {
            item.classList.toggle('completed');
            item.classList.toggle('not-completed');
        });
    });

    // Manipula a redimensionamento da janela
    window.addEventListener('resize', function () {
        if (this.innerWidth < 800) {
            sidebar.classList.add('hide');
        } else {
            sidebar.classList.remove('hide');
        }
    });

    // Verificação inicial do redimensionamento
    if (window.innerWidth < 800) {
        sidebar.classList.add('hide');
    }
});

