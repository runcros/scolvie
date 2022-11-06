var timeDisplay = document.getElementById("time");
function refreshTime() {
    var datetime = new Date().toLocaleString('fr-FR', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
    });;
    timeDisplay.innerHTML = datetime;
}
setInterval(refreshTime, 1000);