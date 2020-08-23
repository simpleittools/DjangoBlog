const modal = document.getElementById("confirm")

window.onclick = function(e){
    if(e.target == modal) {
        modal.style.display = 'none';
    }
}