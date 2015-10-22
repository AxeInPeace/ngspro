CREATE TABLE mapbaloon_Instrument(
    id SERIAL,
    name VARCHAR(512),
    PRIMARY KEY (id)
);

CREATE TABLE mapbaloon_Format(
    id SERIAL,
    name VARCHAR(16),
    PRIMARY KEY (id)
);

CREATE TABLE ngsproauth_CustomUser(
    id SERIAL,
    userid INTEGER REFERENCES auth_user(id),
    cash FLOAT NOT NULL DEFAULT 0,
    rating INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE mapbaloon_Balloon(
    id SERIAL,
    coord1 FLOAT NOT NULL,
    coord2 FLOAT NOT NULL,
    date DATE NOT NULL,
    syscoord VARCHAR(256) DEFAULT 'None',
    sysaltit VARCHAR(256) DEFAULT 'None',

    isugrshoot BOOLEAN NOT NULL DEFAULT False,
    isaltmark BOOLEAN NOT NULL DEFAULT False,
    isrelelems BOOLEAN NOT NULL DEFAULT False,

    publisher INTEGER REFERENCES ngsproauth_CustomUser(id),
    myFormat INTEGER REFERENCES mapbaloon_Format(id),
    instrument INTEGER REFERENCES mapbaloon_Instrument(id),
    PRIMARY KEY (id)
);

CREATE TABLE mapbaloon_Polygon(
    id SERIAL,
    date DATE NOT NULL,
    syscoord VARCHAR(256) DEFAULT 'None',
    sysaltit VARCHAR(256) DEFAULT 'None',

    isugrshoot BOOLEAN NOT NULL DEFAULT False,
    isaltmark BOOLEAN NOT NULL DEFAULT False,
    isrelelems BOOLEAN NOT NULL DEFAULT False,

    publisher INTEGER REFERENCES ngsproauth_CustomUser(id),
    myFormat INTEGER REFERENCES mapbaloon_Format(id),
    instrument INTEGER REFERENCES mapbaloon_Instrument(id),
    PRIMARY KEY (id)
);

CREATE TABLE mapbaloon_PolygonCoord(
    id SERIAL,
    pgowner INTEGER REFERENCES mapbaloon_Polygon(id),
    coord1 FLOAT NOT NULL,
    coord2 FLOAT NOT NULL,
    PRIMARY KEY (id)
);
