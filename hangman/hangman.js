function handleGuess() {
  var guessedLetter = document.getElementById("inputLetter").value;
  if (guessedLetter.length < 1) return;
  actualWord = document.getElementById("actualWord").textContent;

  position = actualWord.indexOf(guessedLetter);
  if (position < 0) {
    remaining = Number(document.getElementById("retryLimit").textContent);
    remaining -= 1;
    document.getElementById("retryLimit").textContent = remaining;
  } else {
    hiddenWord = document.getElementById("word").textContent;
    updatedHiddenWord = replaceCharacterAt(hiddenWord, position, guessedLetter);
    document.getElementById("word").textContent = updatedHiddenWord;
  }
  document.getElementById("inputLetter").value = "";
  return 0;
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
