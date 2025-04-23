from sqlalchemy import create_engine, text


eng = create_engine('sqlite:///ecommerce.db', echo=True)


# Test connection
with eng.connect() as conn:
    res = conn.execute(text('SELECT 1;'))
    print(res.scalar())
