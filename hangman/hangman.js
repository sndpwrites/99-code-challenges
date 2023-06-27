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
    } else {
      remaining = Number(document.getElementById("retryLimit").textContent);
      remaining -= 1;
      document.getElementById("retryLimit").textContent = remaining;
    }
  }
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
  words = ["apple", "ball", "orange"];
  randomWord = getRandomString(words);
  document.getElementById("actualWord").textContent = randomWord;
  document.getElementById("word").textContent = hideWord(randomWord);
  document.getElementById("retryLimit").textContent = 6;
}
