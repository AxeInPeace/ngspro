$(".profile-btn").click(function(){
    if ($(".profile-short").css("display") == "none")
        $(".profile-short").css("display", "block");
    else
        $(".profile-short").css("display", "none");
})
$(".avataradd").click(function () {
    $("#avatar_form").modal('show');
});

$('.js-submitformat').click(function(){
    document.forms['filterformats_form'].submit();
});

$('.js-submityear').click(function(){
    getValue = $('#year').val();
    if (!isYear(getValue)){
        $(".errormsg").removeClass('hide');
    }
    else{
        $(".errormsg").addClass('hide');
        document.forms['filteryears_form'].submit();
    }
});

function isYear(n) {
    if(!isNaN(parseInt(n)) && isFinite(n)){
        if (parseInt(n)>1900 && parseInt(n)<2100)
            return true
        else
            return false;}
    else
        return false;
} 
/*************** YMAPS *****************/
