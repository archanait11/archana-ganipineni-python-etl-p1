import sql
import read
from pgsql import query


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # insert data
    # query(sql.test_insert, ["My Insert!"])

    # select data
    results = query(sql.staff_select)
    print("results: ", results)

    # create petl1 schema
    query(sql.petl1_schema, 'create schema')

    # create table
    query(sql.AnnualTicketSales_Create, 'create table')
    # truncate table
    # query(sql.AnnualTicketSales_Truncate, 'truncate table')
    # insert data
    # read.load_AnnualTicketSales_csv()

    query(sql.HighestGrossers_Create, 'create table')
    # query(sql.HighestGrossers_Truncate, 'truncate table')
    # read.load_HighestGrossers_csv()

    query(sql.PopularCreativeTypes_Create, 'create table')
    # query(sql.PopularCreativeTypes_Truncate, 'truncate table')
    # read.load_PopularCreativeTypes_csv()

    query(sql.TopDistributors_Create, 'create table')
    # query(sql.TopDistributors_Truncate, 'truncate table')
    # read.load_TopDistributors_csv()

    query(sql.TopGenres_Create, 'create table')
    # query(sql.TopGenres_Truncate, 'truncate table')
    # read.load_TopGenres_csv()

    query(sql.TopGrossingRatings_Create, 'create table')
    # query(sql.TopGrossingRatings_Truncate, 'truncate table')
    # read.load_TopGrossingRatings_csv()

    query(sql.TopGrossingSources_Create, 'create table')
    # query(sql.TopGrossingSources_Truncate, 'truncate table')
    # read.load_TopGrossingSources_csv()

    query(sql.TopProductionMethods_Create, 'create table')
    # query(sql.TopProductionMethods_Truncate, 'truncate table')
    # read.load_TopProductionMethods_csv()

    query(sql.WideReleasesCount_Create, 'create table')
    # query(sql.WideReleasesCount_Truncate, 'truncate table')
    # read.load_WideReleasesCount_csv()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
