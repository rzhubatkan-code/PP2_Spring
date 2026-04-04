CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN 
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts (name , phone) VALUES (p_name, p_phone);
    END IF;
END;$$;

CREATE OR REPLACE PROCEDURE insert_members(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql AS $$DECLARE
    i INTEGER;
BEGIN
    IF p_names IS NULL OR array_upper(p_names, 1) IS NULL THEN
        RETURN;
    END IF;

    FOR i IN 1 .. array_upper(p_names, 1) LOOP
        IF length(p_phones[i]) >= 5 THEN
            INSERT INTO contacts (name , phone) VALUES (p_names[i], p_phones[i]);
         ELSE
       RAISE NOTICE 'VALID %' , p_names[i] , p_phones[i];
         END IF;
    END LOOP;
END;$$;

CREATE OR REPLACE PROCEDURE delete_contact(p_search VARCHAR)
LANGUAGE plpgsql AS $$BEGIN
    DELETE FROM contacts WHERE name = p_seacrh OR phone = p_search;
END;$$;

CREATE OR REPLACE PROCEDURE delete_contact(p_search VARCHAR)
LANGUAGE plpgsql AS $$
    DELETE FROM contacts WHERE name = p_search OR phone = p_search;
EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'ERROR' , SQLERRM;
END;$$;


