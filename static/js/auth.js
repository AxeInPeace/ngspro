$( "#auth_form" ).on('submit', function( event ) {
  event.preventDefault();
  if ($("#auth_form").find(".alert")) {
    $("#auth_form").find(".alert").remove();
    var no_timer = true;
  }
  $.post('/auth/login/', $('#auth_form').serialize(), function(event) {
    if (event.status == 200) {
      window.location.replace(event.redirect);
    }
    else {
      $("#auth_form").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>" + event.message + "</div>")
    }
  })
  .fail(function () {
    $("#auth_form").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Ой! Что-то пошло не так! :(</div>")
  });
  if (!no_timer) {
    setTimeout(function() {
      $("div.alert").remove();
    }, 5000);
  }
});

$( "#reg_form" ).on('submit', function( event ) {
  event.preventDefault();
  if ($("#reg_form").find(".alert")) {
    $("#reg_form").find(".alert").remove();
    var no_timer = true;
  }
  $.post('/auth/reg/', $('#reg_form').serialize(), function(event) {
    if (event.status == 200) {
      window.location.replace(event.redirect);
    }
    else {
      $("#reg_form").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>" + event.message + "</div>")
    }
  })
  .fail(function () {
    $("#reg_form").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Ой! Что-то пошло не так! :(</div>")
  });
  if (!no_timer) {
    setTimeout(function() {
      $("div.alert").remove();
    }, 5000);
  }
});

$( document ).ready(function(){
    if (window.location.hash == '#login') {
      $('#auth_form').modal('show');
    }
    if (window.location.hash == '#reg') {
      $('#reg_form').modal('show');
    }
});