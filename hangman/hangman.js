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
      }
    } else {
      onErrorGuessed();
    }
  }
}

function onErrorGuessed() {
  remaining = Number(document.getElementById("retryLimit").textContent);
  if (remaining <= 0) {
    alert("Game over. Man is hung");
    document.getElementById("btn-guess").hidden = true;
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
  document.getElementById("btn-guess").hidden = false;
  document.getElementById("retryLimit").textContent = 6;
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
    })
    .catch((error) => {
      console.error(error);
    });
}
