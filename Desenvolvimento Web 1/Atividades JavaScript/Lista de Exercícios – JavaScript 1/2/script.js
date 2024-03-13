// Função para calcular a quantidade total de curtidas
function calcularCurtidas() {
    // Obtém a quantidade de dias informada pelo usuário
    const quantidadeDias = parseInt(document.getElementById("quantidadeDias").value);
    
    // Verifica se a entrada do usuário é um número válido
    if (isNaN(quantidadeDias) || quantidadeDias <= 0) {
        document.getElementById("resultado").innerText = "Por favor, insira um número válido de dias.";
        return;
    }
    
    // Calcula a quantidade total de curtidas
    const curtidasPorLink = 8; // Número de curtidas por link
    const linksPorDia = 6; // Número de links compartilhados por dia
    const totalCurtidas = quantidadeDias * linksPorDia * curtidasPorLink;
    
    // Exibe o resultado na tela
    document.getElementById("resultado").innerText = "Total de curtidas recebidas em " + quantidadeDias + " dias: " + totalCurtidas;
}
