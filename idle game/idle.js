function handleUpgrade() {
  currentRate = Number(document.getElementById("rate").textContent);
  currentCost = Number(document.getElementById("cost").textContent);
  currentWealth = Number(document.getElementById("wealth").textContent);
  if (currentWealth >= currentCost) {
    currentRate += 1;
    currentWealth -= currentCost;
    currentCost *= 2;
  } else {
    alert("Not enough funds");
  }
  document.getElementById("rate").textContent = currentRate;
  document.getElementById("cost").textContent = currentCost;
  document.getElementById("wealth").textContent = currentWealth;
}

function startMining() {
  rate = 1;
  wealth = 0;
  cost = 10;
  currentWealth = Number(document.getElementById("wealth").textContent)
    ? Number(document.getElementById("wealth").textContent)
    : wealth;
  currentRate = document.getElementById("rate").textContent
    ? Number(document.getElementById("rate").textContent)
    : rate;
  currentCost = document.getElementById("cost").textContent
    ? Number(document.getElementById("cost").textContent)
    : cost;
  currentWealth += currentRate;
  document.getElementById("wealth").textContent = String(currentWealth);
  document.getElementById("rate").textContent = currentRate;
  document.getElementById("cost").textContent = currentCost;
}

setInterval(startMining, 1000);
