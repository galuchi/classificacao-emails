document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const submitButton = form.querySelector("button");
    const categorySpan = document.getElementById("category");
    const responseSpan = document.getElementById("response");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        const formData = new FormData(form);

        // Desativa o botão enquanto a requisição está em andamento
        submitButton.disabled = true;
        submitButton.textContent = "Processando...";

        try {
            const response = await fetch("/classify", { method: "POST", body: formData });

            if (!response.ok) {
                throw new Error(`Erro no servidor: ${response.status}`);
            }

            const data = await response.json();

            // Atualiza os resultados de forma segura
            categorySpan.textContent = data.category || "Erro ao processar";
            responseSpan.textContent = data.response || "Erro ao processar";

        } catch (error) {
            console.error("Erro ao classificar email:", error);
            categorySpan.textContent = "Erro ao processar";
            responseSpan.textContent = "Tente novamente mais tarde.";
        } finally {
            // Reativa o botão após o processamento
            submitButton.disabled = false;
            submitButton.textContent = "Classificar";
        }
    });
});
