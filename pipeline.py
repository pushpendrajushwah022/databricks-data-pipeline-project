from pyspark import pipelines as dp

@dp.expect_or_drop("valid_age", "age >= 18")
@dp.expect_or_drop("valid_salary", "salary > 0")
@dp.table
def people_with_department_v2():
    return spark.sql("""
        SELECT
            p.person_id,
            p.name,
            p.age,
            p.salary,
            d.department
        FROM people_pipeline p
        LEFT JOIN department_lookup d
            ON p.person_id = d.person_id
        WHERE p.age >= 18
    """)
