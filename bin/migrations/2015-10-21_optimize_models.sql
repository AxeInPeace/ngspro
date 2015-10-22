CREATE SEQUENCE mapbaloon_triangulationstation_publisher_id;
ALTER TABLE mapbaloon_balloon 
    ADD COLUMN title varchar(255) NOT NULL DEFAULT 'balloon'; 
ALTER TABLE mapbaloon_balloon 
    RENAME COLUMN coord2 TO lng;
ALTER TABLE mapbaloon_balloon 
    RENAME COLUMN coord1 TO lat; 
ALTER TABLE mapbaloon_triangulationstation
    ALTER COLUMN lat TYPE double precision, 
    ALTER COLUMN lng TYPE double precision, 
    ALTER COLUMN center_height SET DATA TYPE integer USING (center_height::integer),
    ADD COLUMN publisher_id integer NOT NULL REFERENCES "ngsproauth_customuser" ("id") DEFERRABLE INITIALLY DEFERRED DEFAULT 1,
    ADD COLUMN "date" date NOT NULL DEFAULT now();
CREATE INDEX "mapbaloon_triangulationstation_publisher_id" ON "mapbaloon_triangulationstation" ("publisher_id");
