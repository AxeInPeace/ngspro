# EngGeo

####Резюме за 3 дня: <br>
Паша 4+.
Маша на 4-

## Следующий спринт заканчивается в вс вечером
В 22:00 собираемся. Следовательно все Pull Requests должны стоять на мне в обед, чтобы успели исправить замечания
## Маша
####Лендинг 
1. Гамму ярче
2. Верстаем

####Ajax авторизация и регистрация.
В файле lib/auth/views.py есть логика авторизации с сообщениями.<br>
В папке tpl/inc/ есть reg_form.html и auth_form.html.
Нужно:
1. сделать так, чтобы после регистрации/авторизации появляся исчезали кнопки и появлялся профиль пользователя
2. Корректная обработка ошибок

## Паша
0. Перевести ошибки регистрации на русский язык
1. Разобраться с urls.py (В каждом приложении свой urls.py в основной собираем)<br>
2. Протухает CSRF. Найти решения. (Как вариант получать форму после клика по SignIn)<br>
3. Продумать тему что бы при клике по карте выпадало меню, с различными действиями (объекты рядом, добавить материал в этой точке) <br>
4. Хостинг аватарок
5. Фильтрация по годам
6. Валидация форм
