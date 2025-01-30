document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const submitButton = form.querySelector("button[type='submit']");
    const categorySpan = document.getElementById("category");
    const categoryIcon = document.getElementById("category-icon");
    const responseSpan = document.getElementById("response");
    let fileInput = document.getElementById("file");

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Impede submissão padrão

        const formData = new FormData(form);
        if (file) { 
            formData.append("file", file); 
        } else if (fileInput.files.length > 0) {
            formData.append("file", fileInput.files[0]); 
        }

        const emailText = formData.get("email_text") ? formData.get("email_text").trim() : "";
        if (!emailText && !formData.has("file")) {
            alert("Por favor, insira um texto ou selecione um arquivo.");
            return;
        }

        submitButton.disabled = true;
        submitButton.textContent = "Processando...";

        try {
            const response = await fetch("/classify", { method: "POST", body: formData });

            if (!response.ok) {
                throw new Error(`Erro no servidor: ${response.status}`);
            }

            const data = await response.json();

            categorySpan.textContent = data.category || "Erro ao processar";
            responseSpan.textContent = data.response || "Erro ao processar";

            // Atualiza o ícone da categoria
            updateCategoryIcon(data.category);

        } catch (error) {
            console.error("Erro ao classificar email:", error);
            categorySpan.textContent = "Erro ao processar";
            responseSpan.textContent = "Tente novamente mais tarde.";
            categoryIcon.innerHTML = ""; // Remove o ícone se houver erro
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Gerar";
        }
    });

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
