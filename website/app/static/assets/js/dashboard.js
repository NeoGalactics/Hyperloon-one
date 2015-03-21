window.onload = function() {
  [].map.call(document.querySelectorAll('.card, span.card-title'), function(card) {
  	card.classList.add('animate');
  	card.classList.add('intro');
  });

  document.querySelector('#loading-icon').classList.add('hidden');
};