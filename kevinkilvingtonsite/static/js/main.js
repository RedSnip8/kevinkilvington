
// Message time out
setTimeout(function() {
    $('#message').fadeOut('slow');
  }, 3000);

 //Masonry JS
 var elem = document.querySelector('.grid');
 var msnry = new Masonry( elem, {
 // options
 itemSelector: '.grid-item',
 columnWidth: 200
 });

 // element argument can be a selector string
 //   for an individual element
 var msnry = new Masonry( '.grid', {
     iitemSelector: '.grid-item',
     isFitWidth: true
 });


 //Modal Pop
 var myModal = document.getElementById('requestModal')
 var myInput = document.getElementById('modalInput')

 myModal.addEventListener('shown.bs.modal', function () {
 myInput.focus()
 })