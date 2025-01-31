document.addEventListener("DOMContentLoaded", function () {
    // Seleciona os elementos do formulário e botões
    const form = document.querySelector("form");
    const submitButton = form.querySelector("button[type='submit']");
    const categorySpan = document.getElementById("category"); // Exibição da categoria
    const categoryIcon = document.getElementById("category-icon"); // Ícone da categoria
    const responseSpan = document.getElementById("response"); // Resposta gerada
    let fileInput = document.getElementById("file"); // Input de arquivo

    // Evento acionado ao enviar o formulário
    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Impede submissão padrão do formulário

        const formData = new FormData(form); // Cria um objeto FormData com os dados do formulário
        
        // Verifica se há um arquivo e adiciona ao FormData
        if (file) { 
            formData.append("file", file); 
        } else if (fileInput.files.length > 0) {
            formData.append("file", fileInput.files[0]); 
        }

        // Obtém o texto digitado no formulário
        const emailText = formData.get("email_text") ? formData.get("email_text").trim() : "";

        // Caso não haja texto nem arquivo, exibe um alerta e cancela o envio
        if (!emailText && !formData.has("file")) {
            alert("Por favor, insira um texto ou selecione um arquivo.");
            return;
        }

        // Desabilita o botão enquanto processa a requisição
        submitButton.disabled = true;
        submitButton.textContent = "Processando...";

        try {
            // Faz uma requisição assíncrona para o backend com os dados do formulário
            const response = await fetch("/classify", { method: "POST", body: formData });

            // Se a resposta não for bem-sucedida, lança um erro
            if (!response.ok) {
                throw new Error(`Erro no servidor: ${response.status}`);
            }

            // Converte a resposta para JSON
            const data = await response.json();

            // Atualiza os elementos na página com os dados retornados
            categorySpan.textContent = data.category || "Erro ao processar";
            responseSpan.textContent = data.response || "Erro ao processar";

            // Atualiza o ícone da categoria
            updateCategoryIcon(data.category);

        } catch (error) {
            // Em caso de erro, exibe mensagens de erro apropriadas
            console.error("Erro ao classificar email:", error);
            categorySpan.textContent = "Erro ao processar";
            responseSpan.textContent = "Tente novamente mais tarde.";
            categoryIcon.innerHTML = ""; // Remove o ícone se houver erro
        } finally {
            // Habilita o botão e restaura o texto original
            submitButton.disabled = false;
            submitButton.textContent = "Gerar";
        }
    });

    /**
     * Atualiza o ícone da categoria com base no resultado da classificação.
     * @param {string} category - Categoria classificada (Produtivo ou Improdutivo).
     */
    function updateCategoryIcon(category) {
        categoryIcon.innerHTML = ""; // Remove ícones antigos

        if (category === "Produtivo") {
            categoryIcon.innerHTML = " ✅"; 
            categoryIcon.style.color = "green"; 
        } else if (category === "Improdutivo") {
            categoryIcon.innerHTML = " ❌"; 
            categoryIcon.style.color = "red"; 
        }
    }
});
