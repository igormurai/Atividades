// Função para verificar se um número é par ou ímpar
function verificarParOuImpar() {
    // Array para armazenar os números
    const numeros = [];

    // Loop para preencher o array com os números informados pelo usuário
    for (let i = 0; i < 15; i++) {
        const input = document.getElementById("input" + i);
        const numero = parseInt(input.value);
        numeros.push(numero);
    }

    // String para armazenar o resultado
    let resultado = "";

    // Loop para verificar se cada número é par ou ímpar
    for (let i = 0; i < numeros.length; i++) {
        const numero = numeros[i];
        if (numero % 2 === 0) {
            resultado += numero + " é par.<br>";
        } else {
            resultado += numero + " é ímpar.<br>";
        }
    }

    // Exibir o resultado na tela
    document.getElementById("resultado").innerHTML = resultado;
}

// Criar as caixas de entrada para os números dinamicamente
window.onload = function() {
    const inputsDiv = document.getElementById("inputs");
    for (let i = 0; i < 15; i++) {
        const input = document.createElement("input");
        input.type = "number";
        input.id = "input" + i;
        input.placeholder = "Número " + (i + 1);
        inputsDiv.appendChild(input);
    }
}
