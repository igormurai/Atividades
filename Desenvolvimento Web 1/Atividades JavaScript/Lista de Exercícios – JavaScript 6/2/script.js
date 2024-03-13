// Função para calcular a média semestral e verificar se o aluno foi aprovado
function calcularMedia() {
    // Obtém as notas das duas avaliações informadas pelo usuário
    const nota1 = parseFloat(document.getElementById("nota1").value);
    const nota2 = parseFloat(document.getElementById("nota2").value);
    
    // Verifica se as entradas do usuário são números válidos
    if (isNaN(nota1) || isNaN(nota2)) {
        document.getElementById("resultado").innerText = "Por favor, insira notas válidas.";
        return;
    }
    
    // Calcula a média semestral
    const media = (nota1 + nota2) / 2;
    
    // Verifica se o aluno foi aprovado (média >= 6.0)
    if (media >= 6.0) {
        document.getElementById("resultado").innerText = "Sua média semestral é " + media.toFixed(2) + ". PARABÉNS! Você foi aprovado!";
    } else {
        document.getElementById("resultado").innerText = "Sua média semestral é " + media.toFixed(2) + ". Infelizmente, você não foi aprovado.";
    }
}
