 // jquery toggle whole attribute
 $.fn.toggleAttr = function(attr, val) {
    var test = $(this).attr(attr);
    if ( test ) { 
      // if attrib exists with ANY value, still remove it
      $(this).removeAttr(attr);
    } else {
      $(this).attr(attr, val);
    }
    return this;
  };

$("#edit-btn").on("click", function() {
    $(this).parent().find("#accept-btn, #discard-btn, input").toggleAttr("disabled", "true");
    $(this).hide();
    $(this).parent().find("input").trigger("focus");
});
$("#discard-btn").on("click", function() {
    $(this).parent().find("input").val("");
});
$("#accept-btn, #discard-btn").on("click", function() {
    $(this).parent().find("#edit-btn").show();
    $(this).parent().find("#accept-btn, #discard-btn, input").toggleAttr("disabled", "true");
});
$("#name").on("submit", function(event) {
});