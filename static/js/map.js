ymaps.ready(init);
function init () {
    var myMap = new ymaps.Map("YMapsID", {
        center: [54.75, 37.60],
        zoom: 9,
        controls: ['zoomControl', 'rulerControl', 'geolocationControl', 'fullscreenControl', 'typeSelector']
        }, {
          searchControlProvider: 'yandex#search'
        }),
        loadingObjectManager = new ymaps.LoadingObjectManager('http://test2.enggeo.ru/map/trg/?bbox=%b', {   
            // Включаем кластеризацию.
            clusterize: true,
            // Опции кластеров задаются с префиксом cluster.
            clusterHasBalloon: true,
            // Опции объектов задаются с префиксом geoObject
            geoObjectOpenBalloonOnClick: true,
            clusterDisableClickZoom: true
        }),
        loadingObjectManager = new ymaps.LoadingObjectManager('http://test2.enggeo.ru/map/material/?bbox=%b', {   
            // Включаем кластеризацию.
            clusterize: true,
            // Опции кластеров задаются с префиксом cluster.
            clusterHasBalloon: true,
            // Опции объектов задаются с префиксом geoObject
            geoObjectOpenBalloonOnClick: true,
            clusterDisableClickZoom: true
        });

    loadingObjectManager.objects.options.set('preset', 'islands#greenDotIcon');
    loadingObjectManager.clusters.options.set('preset', 'islands#greenClusterIcons');
    myMap.geoObjects.add(loadingObjectManager);

    myMap.events.add('contextmenu', function (e) {
    var coords = e.get('coords');  
    myMap.balloon.open(coords, {
     contentHeader:'Добавить материал',
     contentBody:
         '<p>Координаты щелчка: ' + [
         coords[0].toPrecision(6),
         coords[1].toPrecision(6)
         ].join(', ') + '</p>' +
         '<p><a href="#modal_material" role="button" class="btn btn-primary" data-toggle="modal">Добавить материал</a></p>' + 
         '<p><a href="#trigpoint" role="button" class="btn btn-primary" data-toggle="modal">Добавить тригапункт</a></p>',
    }); 

    $("#xcoord").replaceWith("<input type=\"text\" id=\"xcoord\" name=\"coord1\" value=\"" + coords[0].toPrecision(6) + "\">");
    $("#ycoord").replaceWith("<input type=\"text\" id=\"ycoord\" name=\"coord2\" value=\"" + coords[1].toPrecision(6) + "\">");
    $(".trgcoordx").attr('value', coords[0].toPrecision(6));
    $(".trgcoordy").attr('value', coords[1].toPrecision(6));
    });
    var filterYear = new ymaps.control.Button({
      data: {
        content: "Отфильтровать по годам",
      },
      options: {
        selectOnClick: false,
        maxWidth: 200
      }
    });
    filterYear.events.add('click', function() { $("#filteryears_form").modal('show') });
    myMap.controls.add(filterYear);
}

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
  $("#modal_material").find(".alert").hide().remove()
  $.post('/map/send_balloon/', $("#mapballoon_form").serialize(), function(event) {
    if (event.status != 200)
        $("#modal_material").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>" + event.message +"</div>")
    else
        $("#modal_material").modal("toggle");
  })
  .fail(function (event) {
    $("#modal_material").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Тут что-то не так! Гоблины уже работают!</div>")
  })
});
