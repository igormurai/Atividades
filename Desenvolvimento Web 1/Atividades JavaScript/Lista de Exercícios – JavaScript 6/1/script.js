// Função para converter temperatura de Fahrenheit para Celsius
function fahrenheitParaCelsius(temperaturaFahrenheit) {
    // Aplica a fórmula de conversão
    const temperaturaCelsius = (temperaturaFahrenheit - 32) * 5/9;
    // Retorna a temperatura em Celsius
    return temperaturaCelsius;
}

// Função para ser chamada ao clicar no botão "Converter"
function converterParaCelsius() {
    // Obtém a temperatura em Fahrenheit informada pelo usuário
    const temperaturaFahrenheit = parseFloat(document.getElementById("fahrenheitInput").value);
    
    // Verifica se a entrada do usuário é um número válido
    if (isNaN(temperaturaFahrenheit)) {
        document.getElementById("resultado").innerText = "Por favor, insira uma temperatura válida em Fahrenheit.";
        return;
    }
    
    // Converte a temperatura para Celsius usando a função fahrenheitParaCelsius
    const temperaturaCelsius = fahrenheitParaCelsius(temperaturaFahrenheit);
    
    // Exibe o resultado na tela
    document.getElementById("resultado").innerText = temperaturaFahrenheit + "°F é equivalente a " + temperaturaCelsius.toFixed(2) + "°C.";
}
