// Load the outline box
$(".toggle-btn" ).on( "click", function(event) {
    event.preventDefault();
    $( this ).toggleClass( "active" );
  });
$(window).width() < 768 ? $(".outline-box-container").addClass("invisible") : $(".outline-box-container").removeClass("invisible");

document.querySelector('#contact-form').addEventListener('submit', (e) => {
  e.preventDefault();
  e.target.elements.name.value = '';
  e.target.elements.email.value = '';
  e.target.elements.message.value = '';
});


