#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click

dtype = {
    "LocationID"      : "Int64",
    "Borough"         : "string",
    "Zone"            : "string",
    "service_zone"    : "string"
}


def ingest_data(
        url: str,
        engine,
        target_table: str,
) -> None:
    df = pd.read_csv(
        url,
        dtype=dtype,
        keep_default_na=False
    )

    df.to_sql(
        name=target_table,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Inserted {len(df)} rows into {target_table}")


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--url', default='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv', help='URL or local path of the CSV')
@click.option('--target-table', default='zones', help='Target table name')
def main(pg_user, pg_pass, pg_host, pg_port, pg_db, url, target_table):

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    ingest_data(
        url=url,
        engine=engine,
        target_table=target_table
    )


if __name__ == '__main__':
    main()