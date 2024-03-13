// Função para calcular a diferença entre o valor pago pelo ingresso e a proposta recebida
function calcularDiferenca() {
    // Valor pago pelo ingresso
    const valorPagoPeloIngresso = 170.00;
    
    // Valor da proposta recebida informado pelo usuário
    const propostaRecebida = parseFloat(document.getElementById("propostaRecebida").value);
    
    // Verificar se o usuário inseriu um valor
    if (isNaN(propostaRecebida)) {
        document.getElementById("resultado").innerText = "Por favor, insira um valor válido.";
        return;
    }
    
    // Calcular a diferença entre o valor pago pelo ingresso e a proposta recebida
    const diferenca = propostaRecebida - valorPagoPeloIngresso;
    
    // Exibir a diferença na tela
    document.getElementById("resultado").innerText = "A diferença entre o valor pago pelo ingresso e a proposta recebida é de R$" + diferenca.toFixed(2);
}
