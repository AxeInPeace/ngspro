$( "#auth_form" ).on('submit', function( event ) {
  event.preventDefault();
  if ($("#auth_form").find(".alert")) {
    $("#auth_form").find(".alert").remove();
    var no_timer = true;
  }
  $.post('/auth/login/', $('#auth_form').serialize(), function(event) {
    window.location.replace(event.redirect);
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
  if ($("#reg_form").find(".alert")) {
    $("#reg_form").find(".alert").remove();
    var no_timer = true;
  }
  $.post('/auth/reg/', $('#reg_form').serialize(), function(event) {
    $("#reg_form").find(".modal-header").append("<div class=\"alert alert-success\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Еще секундочку!</div>")
  })
  .fail(function () {
    event.preventDefault();
    $("#reg_form").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Ой! Что-то пошло не так! :(</div>")
  });
  if (!no_timer) {
    setTimeout(function() {
      $("div.alert").remove();
    }, 5000);
  }
});

$(".menu-btn").click(function(){
  $(".menu").animate({width: 'toggle'});
})
