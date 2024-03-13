// Função para encontrar o maior número entre dois números
function encontrarMaiorNumero() {
    // Obtém os números informados pelo usuário
    const numero1 = parseFloat(document.getElementById("numero1").value);
    const numero2 = parseFloat(document.getElementById("numero2").value);
    
    // Verifica se as entradas do usuário são números válidos
    if (isNaN(numero1) || isNaN(numero2)) {
        document.getElementById("resultado").innerText = "Por favor, insira números válidos.";
        return;
    }
    
    // Encontra o maior número
    let maiorNumero;
    if (numero1 > numero2) {
        maiorNumero = numero1;
    } else {
        maiorNumero = numero2;
    }
    
    // Exibe o resultado na tela
    document.getElementById("resultado").innerText = "O maior número é: " + maiorNumero;
}
