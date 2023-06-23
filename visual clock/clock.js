function displayClock() {
  var now = new Date();
  var hours = now.getHours();
  var minutes = now.getMinutes();
  var seconds = now.getSeconds();

  // Pad single digits with leading zeros
  if (hours < 10) {
    hours = "0" + hours;
  }
  if (minutes < 10) {
    minutes = "0" + minutes;
  }
  if (seconds < 10) {
    seconds = "0" + seconds;
  }

  var timeString = hours + ":" + minutes + ":" + seconds;
  //   document.getElementById("clock").textContent = timeString;
  var date = new Date().toDateString();
  document.getElementById("clock").textContent = `${timeString}\n${date}`;
}

// Call the displayClock function every second
setInterval(displayClock, 1000);
