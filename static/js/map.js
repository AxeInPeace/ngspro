ymaps.ready(init);
function init () {
    var myMap = new ymaps.Map("YMapsID", {
        center: [54.75, 37.60],
        zoom: 9,
        controls: ['zoomControl', 'rulerControl', 'geolocationControl', 'fullscreenControl', 'typeSelector']
        }, {
          searchControlProvider: 'yandex#search'
        }),
        loadingObjectManager = new ymaps.LoadingObjectManager('/map/material/?bbox=%b', {
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
         '<p><a href="#trigpoint" role="button" class="btn btn-primary" data-toggle="modal">Добавить тригопункт</a></p>',
    }); 

    $("#xcoord").replaceWith("<input type=\"text\" id=\"xcoord\" name=\"coord1\" value=\"" + coords[0].toPrecision(6) + "\">");
    $("#ycoord").replaceWith("<input type=\"text\" id=\"ycoord\" name=\"coord2\" value=\"" + coords[1].toPrecision(6) + "\">");
    $(".trgcoordx").attr('value', coords[0].toPrecision(6));
    $(".trgcoordy").attr('value', coords[1].toPrecision(6));
    });
    // TODO: load years from server
    var yearList = new ymaps.control.ListBox({
            data: {
                content: 'Отфильтровать по году добавления материала'
            },
            items: [
                new ymaps.control.ListBoxItem('2015'),
                new ymaps.control.ListBoxItem('2016')
            ],
            options: {
                popupFloat: 'right'
            }
        });

    var years = [];
    function update_manager() {
        loadingObjectManager.objects.removeAll();
        loadingObjectManager.setUrlTemplate('/map/material/?bbox=%b&year=' + years.join("&year="));
        loadingObjectManager.reloadData();
    }

    function pop_year(year) {
        for(var i = years.length - 1; i >= 0; i--) {
            if(years[i] === year) {
               years.splice(i, 1);
            }
        }
    }
    yearList.get(0).events.add('select', function () {
        years.push(2015);
        update_manager()
    });
    yearList.get(1).events.add('select', function () {
        years.push(2016);
        update_manager()
    });
    yearList.get(0).events.add('deselect', function () {
        pop_year(2015);
        update_manager()
    });
    yearList.get(1).events.add('deselect', function () {
        pop_year(2016);
        update_manager()
    });
    myMap.controls.add(yearList);
}

function isNumber(n) {
    return !!(!isNaN(parseFloat(n)) && isFinite(n));
}
function isCoord(n) {
    if (isNumber(n)) {
        return !!(parseFloat(n) > -180 && parseFloat(n) < 180);
    }
    else
        return false;
}

$(".js-submittrgpoint").on('click', function( event ) {
  $("#trigpoint").find(".alert").hide().remove();
  var formData = new FormData(document.forms['trgpoint_form']);  // TODO: migrate to AJAX
  $.ajax({
    type: "POST",
    contentType: false,
    processData: false,
    url: "/map/send_trgpoint/",
    data:  formData
  })
  .success(function( data ) {
    console.log(data);
    if (data.status == 200) {
      window.location.replace(data.redirect);
    }
    else {
      $("#trigpoint").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>" + data.message + "</div>")
    }
    setTimeout(function() {
      $("div.alert").remove();
    }, 5000);
  })
  .fail(function () {
    $("#trigpoint").find(".modal-header").append("<div class=\"alert alert-danger\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>Ой! Что-то пошло не так! :(</div>")
    setTimeout(function() {
      $("div.alert").remove();
    }, 5000);
  });
  event.preventDefault();
});