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

            var placemark = new YMaps.Placemark(new YMaps.GeoPoint(37.7,55.7));
            placemark.setBalloonContent(
                "<div class=\"boldtext coordinates\">55°45.35'N, 37°37.06'E</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Дата:</div> " +
                    "<div class=\"inlineblock info-date\">15.03.2015</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Подземные коммуникации:</div> " +
                    "<div class=\"inlineblock info-communicate\">да</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Высотные отметки:</div> " +
                    "<div class=\"inlineblock info-mark\">да</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Элементы рельефа:</div>" +
                    "<div class=\"inlineblock info-element\">да</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Система координат:</div>" +
                    "<div class=\"inlineblock info-coorsystem\">WGS 84</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Система высот:</div>" +
                    "<div class=\"inlineblock info-highsystem\">bla</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Вид:</div>" +
                    "<div class=\"inlineblock info-view\">pdf</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock nickname bluetext\">Nick </div>" +
                    "<div class=\"inlineblock info-instr\"> с помощью тахеометра</div>" +
                "</div>" +
                "<div class=\"nowrap\"> " +
                    "<div class=\"inlineblock boldtext\">Kд =</div>" +
                    "<div class=\"inlineblock info-kd\"> 1</div>" +
                "</div>"
            );
            map.addOverlay(placemark);
            placemark.openBalloon();
        })