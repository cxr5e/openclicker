projects = 0; 
function incrementProjects() {
    projects++; 
    countDiv = document.getElementById('count'); 
    countDiv.innerHTML = projects+" open source projects made!"
}