CREATE SEQUENCE mapbaloon_triangulationstation_id_seq; 

CREATE TABLE "mapbaloon_triangulationstation" (
    "id" serial NOT NULL PRIMARY KEY,
    "lat" integer NOT NULL,
    "lng" integer NOT NULL,
    "title" varchar(255) NOT NULL,
    "type" varchar(7) NOT NULL,
    "precision" integer NOT NULL,
    "national" boolean NOT NULL,
    "height" integer NOT NULL,
    "backsight" boolean NOT NULL,
    "outer" boolean NOT NULL,
    "center" boolean NOT NULL,
    "center_height" boolean NOT NULL,
    "center_photo_id" integer NOT NULL REFERENCES "photo_photo" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "mapbaloon_triangulationstation_center_photo_id" ON "mapbaloon_triangulationstation" ("center_photo_id");

ALTER SEQUENCE mapbaloon_triangulationstation_id_seq OWNED BY mapbaloon_triangulationstation.id;

INSERT INTO django_content_type (app_label, model) VALUES ('mapbaloon', 'triangulationstation');
