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

$('.js-submitmaterial').click(function(){
  document.forms['material_form'].submit();
});


function isNumber(n) {
    if (!isNaN(parseFloat(n)) && isFinite(n)) 
        return true
    else
        return false;
}

function isCoord(n) {
    if (isNumber(n)) {
        if (parseFloat(n)>-180 && parseFloat(n)<180)
            return true
        else
            return false;
    }
    else
        return false;
}
