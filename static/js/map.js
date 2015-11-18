$('.js-submittrgpoint').click(function(){
    xValue = $('.trgcoordx').val();
    yValue = $('.trgcoordy').val();
    accuracyClass = $('.trgaccuracy').val();
    trgHeight = $('.trgheight').val();
    centerHeight = $('.ctrheight').val();
    console.log(isNumber(xValue)); 
    console.log(isNumber(yValue));
    console.log($('.trgaccuracy').val());
    console.log(isNumber(accuracyClass));
    console.log(isNumber(trgHeight));
    console.log(isNumber(centerHeight));
    if(isNumber(xValue) && isNumber(yValue) && isNumber(accuracyClass) && isNumber(trgHeight) && isNumber(centerHeight)){
        $(".errormsg.addtrgpoint").addClass('hide');
        document.forms['trgpoint_form'].submit()
    }
    else
        $(".errormsg.addtrgpoint").removeClass('hide');
});


function isNumber(n) {
    if (!isNaN(parseFloat(n)) && isFinite(n)) 
        return true
    else
        return false;
};

function isCoord(n) {
    if (isNumber(n)) {
        if (parseFloat(n)>-180 && parseFloat(n)<180)
            return true
        else
            return false;
    }
    else
        return false;
};

$("#mapballoon_send").click( function( event ) {
  $.post('/mapbaloon/send_balloon/', $("#mapballoon_form").serialize(), function(event) {
    if (event.status != 200)
        $("#modal_material").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>" + event.message +"</div>")
    else
        $("#modal_material").modal("toggle");
  })
  .fail(function (event) {
    $("#modal_material").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Тут что-то не так! Гоблины уже работают!</div>")
  })
});
