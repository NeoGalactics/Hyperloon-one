window.onbeforeunload = function(e){
    document.getElementById('splash').classList.toggle('outro');
	document.querySelector('loading-icon').classList.toggle('hidden');
}

window.onload = function(e){
	document.querySelector('loading-icon').classList.toggle('hidden');
    document.getElementById('splash').classList.toggle('outro');
}