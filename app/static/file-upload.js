const dropArea = document.querySelector(".file-upload"),
    dragText = dropArea.querySelector("header"),
    button = dropArea.querySelector("button"),
    input = dropArea.querySelector("input");

let file = null; // Variável para armazenar o arquivo

// Clique no botão "Procurar"
dropArea.querySelector("button").addEventListener("click", function () {
    input.click();
});

// Quando um arquivo for escolhido via "Procurar"
input.addEventListener("change", function () {
    if (this.files.length > 0) {
        file = this.files[0]; // Atualiza a variável de arquivo
        dropArea.classList.add("active");
        showFile();
    }
});

// Quando o arquivo é arrastado para a área
dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add("active");
    dragText.textContent = "Solte para Carregar";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("active");
    dragText.textContent = "Arraste o Arquivo";
});

dropArea.addEventListener("drop", (event) => {
    event.preventDefault();
    if (event.dataTransfer.files.length > 0) {
        file = event.dataTransfer.files[0]; // Atualiza a variável de arquivo
        showFile();
    }
});

// Exibir o arquivo selecionado
function showFile() {
    let fileName = file.name;
    let validExtensions = ["pdf", "txt"];

    if (validExtensions.some(ext => fileName.endsWith(ext))) {
        dropArea.innerHTML = `
            <div style="display: flex; align-items: center; gap: 10px;">
                <img src="https://via.placeholder.com/50" alt="file icon">
                <span>${fileName}</span>
                <button id="removeFile" style="background: red; color: white; border: none; padding: 5px 10px; cursor: pointer;">X</button>
            </div>
        `;

        // Evento para remover o arquivo
        document.getElementById("removeFile").addEventListener("click", function () {
            file = null;
            resetUploadArea();
        });
    } else {
        alert("Tipo de arquivo inválido. Apenas PDFs e arquivos de texto são permitidos.");
        dropArea.classList.remove("active");
        dragText.textContent = "Arraste o Arquivo";
    }
}

// Restaura a área de upload corretamente
function resetUploadArea() {
  dropArea.innerHTML = `
      <header>Arraste o arquivo</header>
      <p>ou</p>
      <button type="button" id="browseButton">Procurar</button>
      <input type="file" id="file" name="file" style="display: none;">
  `;

  file = null; // Resetamos o arquivo
  const newInput = dropArea.querySelector("input"); // Pegamos o novo input
  const browseButton = dropArea.querySelector("#browseButton"); // Pegamos o novo botão

  // Reatribuir evento ao input de arquivos
  newInput.addEventListener("change", function () {
      if (this.files.length > 0) {
          file = this.files[0]; // Atualiza o arquivo
          dropArea.classList.add("active");
          showFile();
      }
  });

  // Garantir que o botão de procurar funcione sempre
  browseButton.addEventListener("click", function () {
      newInput.click();
  });

  // Reatribuir eventos de arrastar e soltar
  dropArea.addEventListener("dragover", (event) => {
      event.preventDefault();
      dropArea.classList.add("active");
      dragText.textContent = "Solte para Carregar";
  });

  dropArea.addEventListener("dragleave", () => {
      dropArea.classList.remove("active");
      dragText.textContent = "Arraste o Arquivo";
  });

  dropArea.addEventListener("drop", (event) => {
      event.preventDefault();
      if (event.dataTransfer.files.length > 0) {
          file = event.dataTransfer.files[0];
          showFile();
      }
  });
}
