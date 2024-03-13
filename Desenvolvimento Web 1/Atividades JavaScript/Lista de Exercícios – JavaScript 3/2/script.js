// Função para verificar se um número é positivo ou negativo
function verificarPositivoNegativo() {
    // Obtém o número informado pelo usuário
    const numero = parseFloat(document.getElementById("numero").value);
    
    // Verifica se a entrada do usuário é um número válido
    if (isNaN(numero)) {
        document.getElementById("resultado").innerText = "Por favor, insira um número válido.";
        return;
    }
    
    // Verifica se o número é positivo, negativo ou zero
    if (numero > 0) {
        document.getElementById("resultado").innerText = "O número é positivo.";
    } else if (numero < 0) {
        document.getElementById("resultado").innerText = "O número é negativo.";
    } else {
        document.getElementById("resultado").innerText = "O número é zero.";
    }
}
