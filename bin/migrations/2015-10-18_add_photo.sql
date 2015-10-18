CREATE SEQUENCE photo_id_seq;
CREATE TABLE photo_photo (
    id      integer PRIMARY KEY DEFAULT nextval('photo_id_seq'),
    url     varchar(255)
);
ALTER SEQUENCE photo_id_seq OWNED BY photo_photo.id;

-- Создали новую сущность
INSERT INTO django_content_type (app_label, model) VALUES ('photo', 'photo'):

