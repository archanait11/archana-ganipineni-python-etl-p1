test_select = ('''
  SELECT *
  FROM public.test_table;
''')

staff_select = ('''
  SELECT first_name || ' ' || last_name
  FROM public.staff;
''')

test_insert = ('''
  INSERT INTO public.test_table
  VALUES(%s);
''')

petl1_schema = ('''
  CREATE SCHEMA IF NOT EXISTS petl1;
''')

AnnualTicketSales_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.annualticketsales(
    sales_year int,
    ticket_sold varchar(20),
    total_box_office money ,
    total_inflation_adjusted_box_office money ,
    average_ticket_price money)
''')

AnnualTicketSales_Truncate = ('''
    TRUNCATE TABLE petl1.annualticketsales;
''')

AnnualTicketSales_Insert = ('''
    INSERT INTO petl1.annualticketsales
    VALUES(%s,%s,%s,%s,%s);
''')

HighestGrossers_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.highestgrossers(
    sales_year int,
    movie varchar(50),
    genre varchar(20),
    mpaa_rating varchar(10),
    distributor varchar(100),
    total_for_year money,
    total_in_2019_dollars money,
    tickets_sold varchar(25))
''')

HighestGrossers_Truncate = ('''
    TRUNCATE TABLE petl1.highestgrossers;
''')

HighestGrossers_Insert = ('''
    INSERT INTO petl1.highestgrossers
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
''')

PopularCreativeTypes_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.popularcreativetypes(
    rank varchar(25),
    creative_types varchar(25),
    movies varchar(20),
    total_gross varchar(25),
    average_gross varchar(25),
    market_share varchar(15))
''')

PopularCreativeTypes_Truncate = ('''
    TRUNCATE TABLE petl1.popularcreativetypes;
''')

PopularCreativeTypes_Insert = ('''
    INSERT INTO petl1.popularcreativetypes
    VALUES(%s,%s,%s,%s,%s,%s);
''')

TopDistributors_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.topdistributors(
    rank varchar(25),
    distributors varchar(25),
    movies varchar(20),
    total_gross varchar(25),
    average_gross varchar(25),
    market_share varchar(15))
''')

TopDistributors_Truncate = ('''
    TRUNCATE TABLE petl1.topdistributors;
''')

TopDistributors_Insert = ('''
    INSERT INTO petl1.topdistributors
    VALUES(%s,%s,%s,%s,%s,%s);
''')

TopGenres_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.topgenres(
    rank varchar(25),
    genres varchar(25),
    movies varchar(20),
    total_gross varchar(25),
    average_gross varchar(25),
    market_share varchar(15))
''')

TopGenres_Truncate = ('''
    TRUNCATE TABLE petl1.topgenres;
''')

TopGenres_Insert = ('''
    INSERT INTO petl1.topgenres
    VALUES(%s,%s,%s,%s,%s,%s);
''')

TopGrossingRatings_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.topgrossingratings(
    rank varchar(25),
    mpaa_ratings varchar(25),
    movies varchar(20),
    total_gross varchar(25),
    average_gross varchar(25),
    market_share varchar(15))
''')

TopGrossingRatings_Truncate = ('''
    TRUNCATE TABLE petl1.topgrossingratings;
''')

TopGrossingRatings_Insert = ('''
    INSERT INTO petl1.topgrossingratings
    VALUES(%s,%s,%s,%s,%s,%s);
''')

TopGrossingSources_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.topgrossingsources(
    rank varchar(25),
    sources varchar(50),
    movies varchar(20),
    total_gross varchar(25),
    average_gross varchar(25),
    market_share varchar(15))
''')

TopGrossingSources_Truncate = ('''
    TRUNCATE TABLE petl1.topgrossingsources;
''')

TopGrossingSources_Insert = ('''
    INSERT INTO petl1.topgrossingsources
    VALUES(%s,%s,%s,%s,%s,%s);
''')

TopProductionMethods_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.topproductionmethods(
    rank varchar(25),
    production_methods varchar(50),
    movies varchar(20),
    total_gross varchar(25),
    average_gross varchar(25),
    market_share varchar(15))
''')

TopProductionMethods_Truncate = ('''
    TRUNCATE TABLE petl1.topproductionmethods;
''')

TopProductionMethods_Insert = ('''
    INSERT INTO petl1.topproductionmethods
    VALUES(%s,%s,%s,%s,%s,%s);
''')

WideReleasesCount_Create = ('''
    CREATE TABLE IF NOT EXISTS petl1.widereleasescount(
    release_year int,
    warner_bros int,
    walt_disney int,
    twentieth_century_fox int,
    paramount_pictures int,
    sony_pictures int,
    universal int,
    total_major_6 int,
    total_other_studios int)
''')

WideReleasesCount_Truncate = ('''
    TRUNCATE TABLE petl1.widereleasescount;
''')

WideReleasesCount_Insert = ('''
    INSERT INTO petl1.widereleasescount
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);
''')