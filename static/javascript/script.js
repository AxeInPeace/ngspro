YMaps.jQuery(function () {
            // Создает экземпляр карты и привязывает его к созданному контейнеру
            var map = new YMaps.Map(YMaps.jQuery("#YMapsID")[0]);

            // Устанавливает начальные параметры отображения карты: центр карты и коэффициент масштабирования
            map.setCenter(new YMaps.GeoPoint(37.64, 55.76), 10);

            /*
            var styleBalloon = new YMaps.Style();
            styleBalloon.balloonContentStyle = new YMaps.BalloonContentStyle(
                new YMaps.Template("<div style=\"color:#0A0\">$[description]</div>")
            );
            */
            var placemark = new YMaps.Placemark(new YMaps.GeoPoint(57.43, 31.41));
            placemark{{ baloon.id }}.setBalloonContent(
                "<div class=\"boldtext coordinates\">57.43N, 31.41E</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Дата:</div> " +
                    "<div class=\"inlineblock info-date\">01-01-2015</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Подземные коммуникации:</div> " +
                    "<div class=\"inlineblock info-communicate\">Yes</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Высотные отметки:</div> " +
                    "<div class=\"inlineblock info-mark\">Yes</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Элементы рельефа:</div>" +
                    "<div class=\"inlineblock info-element\">No</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Система координат:</div>" +
                    "<div class=\"inlineblock info-coorsystem\">Geocentrical</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Система высот:</div>" +
                    "<div class=\"inlineblock info-highsystem\">Sea level</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Вид:</div>" +
                    "<div class=\"inlineblock info-view\">pdf</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock nickname bluetext\">Tool </div>" +
                    "<div class=\"inlineblock info-instr\">GPS</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Kд =</div>" +
                    "<div class=\"inlineblock info-kd\"> 921</div>" +
                "</div>"

            );
            map.addOverlay(placemark);
            placemark1.openBalloon();
        })
