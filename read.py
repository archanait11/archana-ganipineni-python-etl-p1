import csv
import sql
from pgsql import query


def load_AnnualTicketSales_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv',
              newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            row.pop()
            if i > 0:
                query(sql.AnnualTicketSales_Insert, row)
                # print(row)
            i += 1


def load_HighestGrossers_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/HighestGrossers.csv',
              newline='', encoding='utf-8-sig') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            if i > 0:
                # print(row)
                query(sql.HighestGrossers_Insert, row)
            i += 1


def load_PopularCreativeTypes_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/PopularCreativeTypes.csv',
              newline='', encoding='utf-8-sig') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            # row.pop()
            if i > 0:
                # print(row)
                query(sql.PopularCreativeTypes_Insert, row)
            i += 1


def load_TopDistributors_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopDistributors.csv',
              newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            # row.pop()
            if i > 0:
                # print(row)
                query(sql.TopDistributors_Insert, row)
            i += 1


def load_TopGenres_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGenres.csv',
              newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            # row.pop()
            if i > 0:
                # print(row)
                query(sql.TopGenres_Insert, row)
            i += 1


def load_TopGrossingRatings_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingRatings.csv',
              newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            # row.pop()
            if i > 0:
                # print(row)
                query(sql.TopGrossingRatings_Insert, row)
            i += 1


def load_TopGrossingSources_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingSources.csv',
              newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            # row.pop()
            if i > 0:
                # print(row)
                query(sql.TopGrossingSources_Insert, row)
            i += 1


def load_TopProductionMethods_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopProductionMethods.csv',
              newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            # row.pop()
            if i > 0:
                # print(row)
                query(sql.TopProductionMethods_Insert, row)
            i += 1

def load_WideReleasesCount_csv():
    i = 0
    with open('./datasets/hollywood-theatrical-market-synopsis-1995-to-2021/WideReleasesCount.csv',
              newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            row.pop()
            if i > 0:
                # print(row)
                query(sql.WideReleasesCount_Insert, row)
            i += 1

