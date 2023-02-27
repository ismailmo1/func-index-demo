INSERT INTO public."user" (email, "password", active)
SELECT concat(
        generate_series(0, 100000)::varchar(255),
        '@test.com'::varchar(255)
    ),
    'pass',
    true
