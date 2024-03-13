// Função para analisar os números
function analisarNumeros() {
    // Array para armazenar os números
    const numeros = [];

    // Loop para preencher o array com os números informados pelo usuário
    for (let i = 0; i < 20; i++) {
        const input = document.getElementById("input" + i);
        const numero = parseInt(input.value);
        numeros.push(numero);
    }

    // Array para armazenar os números negativos
    const numerosNegativos = [];

    // Variável para armazenar a soma dos números positivos
    let somaPositivos = 0;
    // Variável para contar a quantidade de números positivos
    let contadorPositivos = 0;

    // Loop para analisar os números
    for (let i = 0; i < numeros.length; i++) {
        const numero = numeros[i];
        if (numero < 0) {
            numerosNegativos.push(numero);
        } else {
            somaPositivos += numero;
            contadorPositivos++;
        }
    }

    // Exibir os números negativos
    document.getElementById("numerosNegativos").innerText = "Números negativos: " + numerosNegativos.join(", ");

    // Calcular a média dos números positivos
    let mediaPositivos = 0;
    if (contadorPositivos > 0) {
        mediaPositivos = somaPositivos / contadorPositivos;
    }

    // Exibir a média dos números positivos
    document.getElementById("mediaPositivos").innerText = "Média dos números positivos: " + mediaPositivos.toFixed(2);
}

// Criar as caixas de entrada para os números dinamicamente
window.onload = function() {
    const inputsDiv = document.getElementById("inputs");
    for (let i = 0; i < 20; i++) {
        const input = document.createElement("input");
        input.type = "number";
        input.id = "input" + i;
        input.placeholder = "Número " + (i + 1);
        inputsDiv.appendChild(input);
    }
}
