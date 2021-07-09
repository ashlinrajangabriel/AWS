CREATE OR REPLACE STREAM "CAPTAIN_SCORES" ("favoritecaptain" varchar(32), "average_rating" DOUBLE, "total_rating" INTEGER);

CREATE OR REPLACE PUMP "STREAM_PUMP" as
INSERT INTO "CAPTAIN_SCORES"
SELECT STREAM "favoritecaptain", avg("rating"), sum("rating")
FROM SOURCE_SQL_STREAM_001
GROUP BY "favoritecaptain", STEP ("SOURCE_SQL_STREAM_001".ROWTIME BY INTERVAL '1' MINUTE)
ORDER BY STEP("SOURCE_SQL_STREAM_001".ROWTIME BY INTERVAL '1' MINUTE), avg("rating") desc;

CREATE 
OR REPLACE STREAM "RAW_ANOMALIES" ("favoritecaptain" varchar(32), "rating" INTEGER, "ANOMALY_SCORE" DOUBLE);
CREATE 
OR REPLACE PUMP "RAW_PUMP" as INSERT 
INTO
    "RAW_ANOMALIES"
    SELECT
        "favoritecaptain",
        "rating",
        "ANOMALY_SCORE" 
    FROM
        TABLE(     RANDOM_CUT_FOREST(CURSOR(SELECT
            STREAM "favoritecaptain",
            "rating" 
        FROM
            "SOURCE_SQL_STREAM_001")) );
CREATE 
OR REPLACE STREAM "ORDERED_ANOMALIES" ("favoritecaptain" varchar(32),
"rating" INTEGER,
"ANOMALY_SCORE" DOUBLE);
CREATE 
OR REPLACE PUMP "ORDERED_PUMP" as INSERT 
INTO
    "ORDERED_ANOMALIES"
    SELECT
        STREAM * 
    FROM
        RAW_ANOMALIES 
    ORDER BY
        FLOOR("RAW_ANOMALIES".ROWTIME TO SECOND),
        "ANOMALY_SCORE" desc;


