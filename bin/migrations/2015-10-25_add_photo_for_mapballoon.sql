ALTER TABLE mapbaloon_balloon ADD COLUMN "material_photo_id" integer NOT NULL REFERENCES "photo_photo" ("id") DEFERRABLE INITIALLY DEFERRED DEFAULT 37;

CREATE INDEX "mapbaloon_balloon_material_photo_id" ON "mapbaloon_balloon" ("material_photo_id");
