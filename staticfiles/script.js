document.addEventListener('DOMContentLoaded', function() {
    console.log('Document is ready'); // Log para verificar se o DOMContentLoaded está funcionando

    const input = document.querySelector('#cpf');
    if (input) {
        console.log('CPF input found'); // Log para verificar se o input está sendo encontrado

        input.addEventListener('input', function() {
            console.log('Input event triggered'); // Log para verificar se o evento de input está sendo registrado



            if (value.length > 0) {
                formattedValue = value.substring(0, 3);
            }
            if (value.length > 3) {
                formattedValue += '.' + value.substring(3, 6);
            }
            if (value.length > 6) {
                formattedValue += '.' + value.substring(6, 9);
            }
            if (value.length > 9) {
                formattedValue += '-' + value.substring(9, 11);
            }

            input.value = formattedValue;
        });
    } else {
        console.log('CPF input not found'); // Log para caso o input não seja encontrado
    }
});
