$(".menu-btn").click(function(){
  $(".menu").animate({width: 'toggle'});
})

$( "#auth_form" ).on('submit', function( event ) {
  event.preventDefault();
  if ($("#auth_form").find(".alert")) {
    $("#auth_form").find(".alert").remove();
    var no_timer = true;
  }
  $.post('{% url 'login' %}', $('#auth_form').serialize(), function(event) {
    $("#auth_form").find(".modal-header").append("<div class=\"alert alert-success\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Еще секундочку!</div>");
    $("#auth_form").hide()
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
  $.post('/reg/', $('#reg_form').serialize(), function(event) {
    $("#reg_form").find(".modal-header").append("<div class=\"alert alert-success\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Еще секундочку!</div>")
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
