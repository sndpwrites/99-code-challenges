function handleUpgrade() {
  var { currentWealth, currentRate, currentCost } = getValues();
  if (currentWealth >= currentCost) {
    currentRate += 1;
    currentWealth -= currentCost;
    currentCost *= 2;
    setValues({ currentWealth, currentRate, currentCost });
  } else {
    alert("Not enough funds");
  }
}

function setValues({ currentWealth, currentRate, currentCost }) {
  document.getElementById("rate").textContent = currentRate;
  document.getElementById("cost").textContent = currentCost;
  document.getElementById("wealth").textContent = currentWealth;
}

function getValues() {
  rate = 1;
  wealth = 0;
  cost = 10;
  currentWealth = document.getElementById("wealth").textContent
    ? Number(document.getElementById("wealth").textContent)
    : wealth;
  currentRate = document.getElementById("rate").textContent
    ? Number(document.getElementById("rate").textContent)
    : rate;
  currentCost = document.getElementById("cost").textContent
    ? Number(document.getElementById("cost").textContent)
    : cost;

  return { currentWealth, currentRate, currentCost };
}

function startMining() {
  var { currentWealth, currentRate, currentCost } = getValues();
  currentWealth += currentRate;
  setValues({ currentWealth, currentRate, currentCost });
}

setInterval(startMining, 1000);
