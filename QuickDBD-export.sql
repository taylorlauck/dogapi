-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "User" (
    "UserID" int   NOT NULL,
    "Name" string   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "UserID"
     )
);

CREATE TABLE "Breeds" (
    "BreedsID" int   NOT NULL,
    "UserID" int   NOT NULL,
    "Breed" breed   NOT NULL,
    CONSTRAINT "pk_Breeds" PRIMARY KEY (
        "BreedsID"
     )
);

CREATE TABLE "PickedBreeds" (
    "ID" int   NOT NULL,
    "PickedBreedsID" int   NOT NULL,
    "BreedsID" int   NOT NULL,
    "UserID" int   NOT NULL,
    CONSTRAINT "pk_PickedBreeds" PRIMARY KEY (
        "ID","UserID"
     )
);

ALTER TABLE "Breeds" ADD CONSTRAINT "fk_Breeds_UserID" FOREIGN KEY("UserID")
REFERENCES "User" ("UserID");

ALTER TABLE "PickedBreeds" ADD CONSTRAINT "fk_PickedBreeds_PickedBreedsID" FOREIGN KEY("PickedBreedsID")
REFERENCES "User" ("UserID");

ALTER TABLE "PickedBreeds" ADD CONSTRAINT "fk_PickedBreeds_BreedsID" FOREIGN KEY("BreedsID")
REFERENCES "Breeds" ("BreedsID");

CREATE INDEX "idx_User_Name"
ON "User" ("Name");

