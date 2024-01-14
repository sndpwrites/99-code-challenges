function handleAddWord() {
    var word = document.getElementById("input-word").value;
    document.getElementById("filter-words").textContent = word;
    document.getElementById("input-word").value="";
}

function applyFilter() {
    var rawText = document.getElementById("raw-text").value;
    var filterWord = document.getElementById("filter-words").textContent;
    var updatedText = rawText.replace(filterWord, "");
    document.getElementById("filtered-text").value = updatedText;
}