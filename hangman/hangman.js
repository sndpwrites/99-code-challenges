// Execute a function when the user presses a key on the keyboard
document.getElementById("inputLetter").addEventListener("keypress", function(event) {
  // If the user presses the "Enter" key on the keyboard
  if (event.key === "Enter") {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("btn-guess").click();
  }
});
function handleGuess() {
  var guessedLetter = getValueAndClearTextBox("inputLetter");

  if (guessedLetter.length === 1) {
    actualWord = document.getElementById("actualWord").textContent;
    position = getMultipleIndexes(actualWord, guessedLetter);
    if (position.length > 0) {
      position.forEach((element) => {
        hiddenWord = document.getElementById("word").textContent;
        updatedHiddenWord = replaceCharacterAt(
          hiddenWord,
          element,
          guessedLetter
        );
        document.getElementById("word").textContent = updatedHiddenWord;
      });
      if (document.getElementById("word").textContent === actualWord) {
        alert("Congratulations! You've won!");
        document.getElementById("btn-guess").disabled = true;
        document.getElementById("inputLetter").disabled = true;
      }
    } else {
      onErrorGuessed();
    }
  }
  document.getElementById("inputLetter").focus()
}

function onErrorGuessed() {
  remaining = Number(document.getElementById("retryLimit").textContent);
  if (remaining <= 0) {
    alert("Game over. Man is hung");
    document.getElementById("btn-guess").disabled = true;
    document.getElementById("inputLetter").disabled = true;
    document.getElementById("word").textContent =
      document.getElementById("actualWord").textContent;
    return;
  }
  remaining -= 1;
  document.getElementById("retryLimit").textContent = remaining;
}

function getValueAndClearTextBox(id) {
  var value = document.getElementById(id).value;
  document.getElementById(id).value = "";
  guessedHistory = document.getElementById("guessed-history").textContent;
  guessedHistory = `${value}-${guessedHistory}`;
  document.getElementById("guessed-history").textContent = guessedHistory;
  return value;
}

function getMultipleIndexes(string, character) {
  const regex = new RegExp(character, "g");
  const indices = [];

  let match;
  while ((match = regex.exec(string)) !== null) {
    indices.push(match.index);
  }
  return indices;
}

function replaceCharacterAt(str, index, newChar) {
  var charArray = str.split("");
  charArray[index] = newChar;
  var modifiedString = charArray.join("");
  return modifiedString;
}

function getRandomString(strings) {
  var randomIndex = Math.floor(Math.random() * strings.length);
  return strings[randomIndex];
}

function getRandomWord() {
  fetch("https://random-word-api.herokuapp.com/word?lang=en")
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Request failed.");
      }
    })
    .then((data) => {
      randomWord = data[0];
      document.getElementById("actualWord").textContent = randomWord;
      document.getElementById("actualWord").hidden = true;
      document.getElementById("word").textContent = hideWord(randomWord);
      document.getElementById(
        "wordLength"
      ).textContent = `${randomWord.length} letters`;
    })
    .catch((error) => {
      // Handle any errors
      console.error(error);
    });
}

function hideWord(data) {
  var numberOfHints = data.length - 4;
  var asteriskString = data
    .split("")
    .map(function () {
      return "_";
    })
    .join("");
  return asteriskString;
}

function handleStart() {
  getRandomWord();
  clearScreen();
}

function clearScreen() {
  document.getElementById("btn-guess").disabled = false;
  document.getElementById("btnShowMeaning").disabled = false;
  document.getElementById("inputLetter").disabled = false;
  document.getElementById("hint-area").textContent = "";
  document.getElementById("guessed-history").textContent = "";
  document.getElementById("retryLimit").textContent = 6;
  document.getElementById("inputLetter").focus();
}

function handleMeaning() {
  word = document.getElementById("actualWord").textContent;
  fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`)
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Request failed.");
      }
    })
    .then((data) => {
      hints = data[0].meanings[0].definitions
        .map((obj) => obj.definition)
        .join("\t ");
      document.getElementById("hint-area").textContent = hints;
      document.getElementById("inputLetter").focus();
      document.getElementById("btnShowMeaning").disabled = true;
    })
    .catch((error) => {
      console.error(error);
      document.getElementById("hint-area").textContent = error;
    });
}
